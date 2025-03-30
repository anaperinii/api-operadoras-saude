const API_URL = 'http://localhost:8000'  // Ou use proxy se configurado

export const buscarOperadoras = async (termo) => {
  try {
    const response = await fetch(`${API_URL}/buscar_operadoras?termo=${encodeURIComponent(termo)}`, {
      method: 'GET',
      mode: 'cors',
      credentials: 'include',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Erro detalhado:', error);
    return {
      success: false,
      error: error.message || 'Falha na comunicação com o servidor',
      count: 0
    };
  }
};