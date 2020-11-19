<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex>
        <!-- IMPORTANT PART! -->
        <form>
          <v-text-field v-model="content" label="Type the keyword to be searched" required></v-text-field>
          <v-btn @click="submit">submit</v-btn>
          <v-btn @click="clear">clear</v-btn>
        </form>
        <br />
           
        
        <p> Note 1: The list of URLS at which scraping is happening is at URL.txt file in current working directory where api.py exists</p>
        <p> Note 2: The output table is stored in OutputData.csv file in the current working directory where api.py exists</p>
        <p> Note 3: The output links are stored in OutputLinks.txt file in current working directory </p>
        <br />

    <div>

        <div v-if="loading">
            <vue-simple-spinner size="huge" message="Scraping Now .. Pls Wait"/>
        </div>

        <div v-else>
            <h3>DONE!!!</h3>
        </div>

    </div>
        <br />
        
        
        
        <br />
        <br />
        <div v-for='items in outputClass' v-bind:key="items.id">
          <div v-for="elements in items" v-bind:key="elements.id">
            <p>{{ elements }}</p>
            <hr>
          </div>
          </div>
        
        
        <!-- END: IMPORTANT PART! -->
      </v-flex>
    </v-layout>
  </v-container>
</template><script>
import axios from "axios"
import VueSimpleSpinner from 'vue-simple-spinner'
export default {
  

  name: "CompleteScraper",
  data: () => ({
    loading:false,
    content: '',
    outputClass: []
  }),
  methods: {
    submit() {
      this.loading=true
      axios.post("http://127.0.0.1:5000/scraper", {
         
          content: this.content
        })
        .then((response) => {
          console.log(response.data);
          this.outputClass = response.data;
          
        })
        .catch(error => console.log(error))
        .finally(() => (this.loading = false))
        
    },
    clear() {
      
      this.content = ""
      this.outputClass=[]
    }
  },
components: { 
      VueSimpleSpinner
   }
};



</script>
