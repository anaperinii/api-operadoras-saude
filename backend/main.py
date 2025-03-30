import numpy as np
import pandas as pd
from fastapi import FastAPI, Response, logger
import csv
from io import StringIO
import re
import os
from typing import Dict, Union, List

from typing import List, Dict, Union
from fastapi.middleware.cors import CORSMiddleware
from unidecode import unidecode

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8086"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],  
    allow_headers=["*"]
)

@app.options("/buscar_operadoras")
async def options_handler():
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "http://localhost:8086",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )


print(f"\nArquivo CSV existe? {os.path.exists('operadoras.csv')}")
print(f"Caminho absoluto: {os.path.abspath('operadoras.csv')}")

def reparar_csv(filepath: str, num_colunas: int = 20) -> pd.DataFrame:
    
    linhas_validas = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        leitor = csv.reader(f, delimiter=',', quotechar='"', escapechar='\\')
        
        for i, linha in enumerate(leitor, 1):
            try:
                # Limpeza básica dos campos
                linha = [campo.strip() for campo in linha]
                
                # Corrige número de colunas
                if len(linha) > num_colunas:
                    linha = linha[:num_colunas-1] + [','.join(linha[num_colunas-1:])]
                elif len(linha) < num_colunas:
                    linha += [''] * (num_colunas - len(linha))
                
                linhas_validas.append(linha)
                
            except Exception as e:
                print(f"Linha {i} ignorada devido a erro: {str(e)}")
                continue
    
    if linhas_validas:
        colunas = linhas_validas[0] if len(linhas_validas) > 1 else [f'col{i}' for i in range(num_colunas)]
        dados = linhas_validas[1:] if len(linhas_validas) > 1 else []
        return pd.DataFrame(dados, columns=colunas)
    return pd.DataFrame()

# Carregamento dos dados
try:
    print("Carregando dados com reparo avançado...")
    df = reparar_csv('operadoras.csv', num_colunas=20)
    
    if not df.empty:
        print("Dados carregados com sucesso!")
        print(f"Total de registros: {len(df)}")
        print(f"Colunas disponíveis: {list(df.columns)}")
        
        print("\nExemplo do primeiro registro:")
        print(df.iloc[0].to_dict())
    else:
        print("AVISO: Nenhum dado válido foi carregado")
except Exception as e:
    print(f"ERRO CRÍTICO: {str(e)}")
    df = pd.DataFrame()

@app.get("/buscar_operadoras", response_model=Dict[str, Union[bool, str, int, List[Dict]]])
async def buscar_operadoras(termo: str = "") -> Dict[str, Union[bool, str, int, List[Dict]]]:

    if df.empty:
        return {"success": False, "error": "Dataset não carregado", "count": 0}
    
    # Validação do termo
    termo = termo.strip()
    if not termo or len(termo) < 2:
        return {"success": False, "error": "Termo deve conter 2+ caracteres", "count": 0}
    
    try:
        # Pré-processamento do termo
        search_term = unidecode(termo).lower()
        
        # Função de normalização
        def normalize_text(text):
            return unidecode(str(text)).lower()
        
        # Busca em múltiplos campos
        mask = (
            df['razao_social'].apply(normalize_text).str.contains(search_term, regex=False) |
            df['nome_fantasia'].apply(normalize_text).str.contains(search_term, regex=False) |
            df['cnpj'].astype(str).str.contains(termo)  
        )
        
        # Filtra e formata resultados
        resultados = df[mask].fillna('').replace({np.nan: None}).to_dict('records')
        
        return {
            "success": True,
            "count": len(resultados),
            "data": resultados,
            "search_term": termo  
        }
        
    except Exception as e:
        logger.error(f"Erro na busca: {str(e)}") 
        return {
            "success": False,
            "error": "Erro interno no servidor",
            "count": 0
        }
    
    