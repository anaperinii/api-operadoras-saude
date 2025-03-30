# API de Busca de Operadoras de Saúde Ativas

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)

API para busca eficiente de operadoras de saúde com integração front-end Vue.js e testes automatizados via Postman.

## 🔎 Visão Geral

Sistema completo para consulta de operadoras de saúde com:

- **Back-end**: FastAPI (Python) para processamento de requisições
- **Front-end**: Vue.js para interface dinâmica
- **Dados**: Processamento eficiente com Pandas
- **Testes**: Coleção Postman para validação

## 🚀 Como executar

### Instalação

#### 1. **Clone o repositório:**
   ```bash
   git clone https://github.com/anaperinii/api-operadoras-saude
   cd api-operadoras-saude
   ```

#### 2. **Back-end**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

#### 3. **Front-end**:
   ```bash
   cd ../frontend
   npm install
   ```


## 🛠️ Configuração

### Back-end

#### 1. Execute o servidor FastAPI:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

#### 2. Acesse a documentação interativa:
   - Swagger UI: `http://localhost:8000/docs`
   - Redoc: `http://localhost:8000/redoc`

### Front-end

#### 1. Inicie o servidor de desenvolvimento:
   ```bash
   npm run serve
   ```

#### 2. Acesse: `http://localhost:8086`

## 📡 Endpoints da API

### GET `/buscar_operadoras`

Busca operadoras por termo (razão social, nome fantasia ou CNPJ).

**Parâmetros**:
- `termo` (obrigatório): String com pelo menos 2 caracteres

**Exemplo**:
```bash
curl "http://localhost:8000/buscar_operadoras?termo=Amil"
```

**Resposta de sucesso**:
```json
{
  "count": 5,
  "data": [
    {
      "cnpj": "12.345.678/0001-90",
      "razao_social": "AMIL ASSISTENCIA MEDICA INTERNACIONAL LTDA",
      "nome_fantasia": "AMIL SAÚDE"
    }
  ]
}
```

**Resposta de erro**:
```json
{
  "success": false,
  "error": "Termo deve ter 2+ caracteres"
}
```

## ⚡ Otimizações

- **Desempenho**:
  - Processamento vetorizado com Pandas
  - Cache do dataset em memória
  - Operações assíncronas

- **Segurança**:
  - CORS restrito ao frontend
  - Validação de inputs
  - Tratamento de erros padronizado

## 🧪 Testes

A coleção Postman inclui testes para:

- Buscas válidas
- Validação de inputs
- Testes de performance
- Validação de CORS

**Para executar**:
- Importe `postman/Operadoras_API.json` no Postman
- Execute a coleção
