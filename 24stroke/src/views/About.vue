<template>
  <div class="about">
    <Navbar />
    <h1>This is an about page</h1>
  </div>
</template>

<script>
import Navbar from "../components/navigationbar.vue"
import Footer from "../components/footerbar.vue"

export default {
  name: 'Home',
  components: {
    Navbar,
    Footer
  }
}
</script>