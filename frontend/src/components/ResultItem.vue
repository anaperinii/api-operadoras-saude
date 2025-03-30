<template>
  <div class="result-item">
    <div class="result-header">
      <h3>{{ result.razao_social || 'Nome não disponível' }}</h3>
    </div>
    <div class="result-details">
      <div v-if="result.cnpj" class="detail">
        <strong>CNPJ:</strong> {{ result.cnpj }}
      </div>
      <div v-if="result.municipio" class="detail">
        <strong>Município:</strong> {{ result.municipio }}
      </div>
      <div v-if="result.uf" class="detail">
        <strong>UF:</strong> {{ result.uf }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultItem',
  props: {
    result: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.result-item {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 15px;
  background-color: #f9f9f9;
}

.result-header {
  margin-bottom: 10px;
}

.result-header h3 {
  margin: 0;
  color: #2c3e50;
}

.result-details {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.detail {
  font-size: 0.9em;
  color: #555;
}
</style>