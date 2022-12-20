<template>
    <div class="cilinder">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="breadcrumbs">
                    <ul class="breadcrumb">
                        <li><a href="/">
                                <font-awesome-icon icon="home" />
                            </a></li>
                        <li><a href="#">{selected moped}</a></li>
                        <li><a href="/motordelen">Motordelen</a></li>
                        <li><a href="/motordelen/cilinders">Cilinders</a></li>
                        <li>{{ product.name }}</li>
                    </ul>
                    <hr class="breadcrumbs-line">
                </div>
                <div class="product-information">
                    <div class="row justify-content-between">
                        <div class="product-big-image col-6">
                            <div class="product-image" v-if="product.images">
                                <img class="img-1 img-fluid" v-bind:src="product.images[currentImage].get_image">
                                <div class="row">
                                    <div class="col-3" @click="showImage(index)"
                                        v-for="(images, index) in product.images" :key='index'>
                                        <img :class="{ active: index === currentImage }" id="img-clickable"
                                            v-bind:src="images.get_image">
                                    </div>
                                </div>
                            </div>
                            <!-- <Lingallery class="tester23" :iid.sync="currentId" :items="[
                            {id: 'someid1', src:product.get_image, thumbnail:product.get_image},
                            {id: 'someid1', src:'https://picsum.photos/600/400/?image=10', thumbnail: 'https://picsum.photos/64/64/?image=10'}
                            ]" /> -->
                        </div>
                        <div class="product-small-information col-5">
                            <InformationRightSide :product="product"/>
                        </div>
                    </div>
                </div>
                <div class="product-description">
                    <Description :product="product" />
                </div>
                <div class="recently-viewed-component">
                    <RecentlyViewed :product="product"/>
                </div>
                <div class="deals-viewed-component">
                    <Deals />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from "/src/components/navigationbar.vue"
import Footer from "/src/components/footerbar.vue"
import axios from 'axios'
import Lingallery from 'lingallery';
import InformationRightSide from "../../components/product-page/InformationRightSide.vue";
import Description from "../../components/product-page/Description.vue";
import RecentlyViewed from "../../components/product-page/RecentlyViewed.vue";
import Deals from "../../components/product-page/Deals.vue";

export default {
    name: 'Home',
    components: {
    Navbar,
    Footer,
    Lingallery,
    InformationRightSide,
    Description,
    RecentlyViewed,
    Deals
    },
    data() {
        return {
            product: null,
            currentImage: 0,
        }
    },
    created() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = '24stroke | ' + this.product.name
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)

        },
        showImage(test) {
            this.currentImage = test
        }
    },
}
</script>

<style>
.product-information img {
    border-radius: 0px !important;
}

.cilinder {
    background-color: #F0F1F2;
}

.product-image {
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.product-image a.image {
    display: block;
}

.product-image img {
    width: 100%;
    height: auto;
}

#img-clickable {
    cursor: pointer;
    margin-top: 10px;
    border: 1px solid gray;
}

.active {
    border: 2px solid #ff2400 !important;
}
</style>

