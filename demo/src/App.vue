<template>
  <div id="app">
    <div class="container">
      <div>
        Trie algorithm
        <AutocompleteInput apiUrl="https://dev-api.paolorechia.de/autocomplete/search?input=" isSorted="test"/>
      </div>
      <div>
        Levenshtein edit distance (limit=20)
        <AutocompleteInput apiUrl="https://dev-api.paolorechia.de/autocomplete/levenshtein?input="/>
      </div>
       </div>
    </div>
</template>

<script>
import AutocompleteInput from './components/AutocompleteInput.vue'
export default {
  name: 'App',
  components: {
    AutocompleteInput
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.container {
  display: flex;
}

</style>
