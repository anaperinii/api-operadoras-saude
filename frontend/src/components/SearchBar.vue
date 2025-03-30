<template>
    <div class="search-bar">
      <form @submit.prevent="handleSubmit">
        <input
          type="text"
          v-model="searchTerm"
          placeholder="Digite o nome da operadora..."
          @input="clearError"
        />
        <button type="submit">Buscar</button>
      </form>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        searchTerm: '',
        error: null
      }
    },
    methods: {
      handleSubmit() {
        if (this.searchTerm.length < 2) {
          this.error = 'Digite pelo menos 2 caracteres'
          return
        }
        this.$emit('search', this.searchTerm)
      },
      clearError() {
        this.error = null
      }
    }
  }
  </script>
  
  <style scoped>
  .search-bar {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  form {
    display: flex;
    gap: 10px;
  }
  
  input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1em;
  }
  
  button {
    padding: 10px 20px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }
  
  button:hover {
    background-color: #2980b9;
  }
  
  .error {
    color: #e74c3c;
    font-size: 0.9em;
  }
  </style>