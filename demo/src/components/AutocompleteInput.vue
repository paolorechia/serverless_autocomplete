<template>
  <div class="autocomplete">
    Enter your query:
    <input v-on:focus="fetchSuggestions" v-on:keydown="fetchSuggestions" v-model="query" />
    <div class="autocomplete-suggestions" v-if="suggestions.length > 0">
        <ul>
            <li v-on:click="choose" class="autocomplete-suggestions-li" v-for="s in suggestions" :key="s">
                {{s}}
            </li>
        </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  name: "AutocompleteInput",
  data: function() {
    return {
      query: "",
      suggestions: [],
      api_key: window.localStorage.getItem("api-key"),
      api_url: "https://dev-api.paolorechia.de/autocomplete/search?input="
    };
  },
  methods: {
    choose: function(event) {
        console.log("Chose!", event.target.innerHTML);
        this.query = event.target.innerHTML;
        this.query = this.query.trim();
        this.suggestions = this.suggestions.filter(()=>false);
    },
    fetchSuggestions: _.debounce(function() {
      // `this` inside methods points to the Vue instance
      axios
        .get(this.api_url + this.query, { headers: {
            "X-Api-Key": this.api_key,
            "Content-Type": "application/json"
        }})
        .then(response => {
          // JSON responses are automatically parsed.
          const parsed = JSON.parse(
              response.data.suggestions.replace(/'/g, '"')
          ).sort();
          this.suggestions = parsed;
          console.log(this.suggestions);
        //   this.suggestions = parsed.map(
        //       (i, s) => ({
        //           "key": i,
        //           "data": s
        //       })
        //   );
        //   console.log(this.suggestions);
        })
        .catch(e => {
          this.errors.push(e);
        });
      // `event` is the native DOM event
    }, 200)
  }
};
</script>

<style scoped>

.autocomplete {
    width: 200px;
}
.input {
    width: 200px;
}
.autocomplete-suggestions {
    margin-left:8px;
    background-color: whitesmoke;
    border: 1px dotted black;
    width: 183px;
}
.autocomplete-suggestions-li {
    display: flex;
    justify-content: left;
    margin-left: -39px;
    padding: 5px;
    padding-left: 10px;
}
.autocomplete-suggestions-li:hover {
    background-color: white;
}
</style>
