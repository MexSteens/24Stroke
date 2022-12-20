<template>
    <div class="recently-viewed row mt-5 py-4">
        <h1>Recenlty viewed items</h1>
        <Carousel :navigationEnabled="true" :perPage="4">
            <Slide v-for="item  in recentlyViewedItems" :key="item">
                <SliderProductBox :product="item"/>
            </Slide>
        </Carousel>
    </div>
    
</template>

<style>
.recently-viewed {
    background: white;
}
</style>

<script>
import { Carousel, Slide } from 'vue-carousel';
import SliderProductBox from './SliderProductBox.vue';
export default {
  name: "RecentlyViewed",
  components: {
    Carousel,
    Slide,
    SliderProductBox
  },
  props: ['product'],
  data() {
    return {
        recentlyViewedItems: []
    }
  },
  mounted() {
    this.recentlyViewedItems = this.$store.state.recentlyViewed.items
    this.AddToRecentlyViewed()
  },
  methods: {
    AddToRecentlyViewed() {
        var inArray = false;
        this.recentlyViewedItems.forEach(item => {
            if (item.id == this.product.id) {
                inArray = true;
            }
        });
        if (!inArray) {
            this.$store.commit('addToRecentlyViewed', this.product)
            if (this.recentlyViewedItems.length > 9) {
                this.$store.commit('removeFromRecentlyViewed')
            }
        }
    }
  }
};

</script>