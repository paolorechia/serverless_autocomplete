<template>
  <div id="app">
    <AutocompleteInput />
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
</style>
