<template>
    <div class="results-list">
      <div class="results-count">{{ count }} resultados encontrados</div>
      <div class="results-container">
        <ResultItem 
          v-for="(result, index) in results" 
          :key="index" 
          :result="result" 
        />
      </div>
    </div>
  </template>
  
  <script>
  import ResultItem from './ResultItem.vue'
  
  export default {
    name: 'ResultsList',
    components: {
      ResultItem
    },
    props: {
      results: {
        type: Array,
        required: true
      },
      count: {
        type: Number,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .results-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .results-count {
    font-weight: bold;
    color: #7f8c8d;
  }
  
  .results-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  </style>