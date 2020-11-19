<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">Web Scraper</span>
      </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <CompleteScraper/>
    </v-content>
  </v-app>
</template>

<script>
import CompleteScraper from './components/CompleteScraper';

export default {
  name: 'App',

  components: {
    CompleteScraper,
  },

  data: () => ({
    //
  }),
};
</script>
