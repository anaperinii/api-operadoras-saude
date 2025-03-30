<template>
    <div class="home-view">
      <SearchBar @search="handleSearch" />
      <div v-if="loading" class="loading">Carregando...</div>
      <div v-if="error" class="error">{{ error }}</div>
      <ResultsList 
        v-if="results.length > 0" 
        :results="results" 
        :count="count" 
      />
      <div v-else-if="searched && !loading" class="no-results">
        Nenhum resultado encontrado
      </div>
    </div>
  </template>
  
  <script>
  import SearchBar from '@/components/SearchBar.vue'
  import ResultsList from '@/components/ResultsList.vue'
  import { buscarOperadoras } from '@/services/api'
  
  export default {
    name: 'HomeView',
    components: {
      SearchBar,
      ResultsList
    },
    data() {
      return {
        results: [],
        count: 0,
        loading: false,
        error: null,
        searched: false
      }
    },
    methods: {
      async handleSearch(termo) {
        if (!termo || termo.length < 2) {
          this.error = 'Digite pelo menos 2 caracteres para buscar'
          return
        }
        
        this.loading = true
        this.error = null
        this.searched = true
        
        try {
          const response = await buscarOperadoras(termo)
          if (response.success) {
            this.results = response.data
            this.count = response.count
          } else {
            this.error = response.error || 'Erro ao buscar operadoras'
            this.results = []
            this.count = 0
          }
        } catch (err) {
          this.error = 'Erro na conexão com o servidor'
          this.results = []
          this.count = 0
        } finally {
          this.loading = false
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .home-view {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .loading, .error, .no-results {
    text-align: center;
    padding: 20px;
    font-size: 1.2em;
  }
  
  .error {
    color: #e74c3c;
  }
  </style>