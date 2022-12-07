<template>
    <div class="cilinders-product-page">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="breadcrumbs">
                    <ul class="breadcrumb">
                        <li><a href="/"><font-awesome-icon icon="home" /></a></li>
                        <li><a href="#">{selected moped}</a></li>
                        <li><a href="/motordelen">Motordelen</a></li>
                        <li>Cilinders</li>
                    </ul>
                    <hr class="breadcrumbs-line">
                </div>
                <div class="row products-row">
                    <ProductBox  v-for="product in category.products" :key="product.id" v-bind:product="product" />
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Category',
  components: {
    ProductBox
  },
  data() {
    return {
      category: {
          products: []
      }
    }
  },
  mounted() {
      this.getCategory()
  },
  watch: {
      $route(to, from) {
            this.getCategory()
      }
  },
  methods: {
      async getCategory() {
          const categorySlug = this.$route.params.category_slug

          this.$store.commit('setIsLoading', true)


          await axios
            .get(`api/v1/products/${categorySlug}`)
            .then(response => {
                this.category = response.data

                document.title = "24stroke | " + this.category.name
            })
            .catch(error => {
                console.log(error)
            })

            this.$store.commit('setIsLoading', false)
      }
  }
}
</script>