<template>
  <div id="app">
    <nav class="app-navigation">
      <Navbar />
    </nav>

    <div class="loading-bar" v-bind:class="{'loading': $store.state.isLoading}">
      <div class="loading-spinner spinner-border text-danger"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

      <Footer />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #F0F1F2;
  min-height: 100vh;
  position: relative;
  padding-bottom: 350px;
}

@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

h1, h2, h3, h4, p {
    font-family: "Roboto", sans-serif;
}

a {
    text-decoration: none !important;
    color: #2c3e50;
}
  
  /*----- begin loader -----*/
.loading-spinner {
  width: 6rem !important;
  height: 6rem !important;
  margin-top: 30px;
  border: 0.75em solid #ff2400 !important;
  border-right-color: transparent !important;
}

.loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.loading-bar.loading {
  height: 200px;
}

  /*----- end loader -----*/

.routerlink{
    color: #2c3e50;
}

.routerlink:hover{
  transition: all 0.3s ease 0s;
  color: #ca1b00;
}
</style>

<script>
import axios from 'axios'

import Footer from "/src/components/footerbar.vue"
import Navbar from "/src/components/navigationbar.vue"

export default {
  name: 'App',
  components: {
    Footer,
    Navbar
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common ['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>
