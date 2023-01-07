<template>
    <div class="deals row mt-5 py-4">
        <h1>Deals</h1>
        <Carousel :navigationEnabled="true" :perPage="4">
            <Slide v-for="item in deals" :key="item">
                <SliderProductBox :product="item"/>
            </Slide>
        </Carousel>
    </div>
    
</template>

<style>
.deals {
    background: white;
}
</style>

<script>
import { Carousel, Slide } from 'vue-carousel';
import SliderProductBox from './SliderProductBox.vue';
import axios from 'axios';
export default {
  name: "Deals",
  components: {
    Carousel,
    Slide,
    SliderProductBox
  },
  data() {
    return {
        deals: [],
    }
  },
  mounted() {
    this.getHighlightedProducts();
  },
  methods: {
    async getHighlightedProducts() {
        this.$store.commit('setIsLoading', true)

        await axios
            .get(`/api/v1/products/highlightedproducts/`)
            .then(response => {
                response.data.forEach(element => {
                    if (element.discounted_deal == true){
                        this.deals.push(element.product)
                    }
                });
            })
            .catch(error => {
                console.log(error)
            })

        this.$store.commit('setIsLoading', false)
    },
  }
};

</script>