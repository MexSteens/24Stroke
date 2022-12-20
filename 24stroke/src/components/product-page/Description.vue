<template>
    <div class="description-box-product row mt-5 py-4">
        <div class="description-product col-9">
            <h1>Beschrijving</h1>
            <p class="description-info">{{product.description}}</p>
            <div class="reviews-component col-3 px-4">
                
            </div>
        </div>
        <div class="technical-details-component col-3 px-4">
            <TechnicalDetails :product="product" />
        </div>
    </div>
</template>

<style>
.description-box-product {
    background-color: white;
    padding-left: 2rem;
}

.description-info {
    text-align: left;
}
</style>

<script>
import TechnicalDetails from './TechnicalDetails.vue';

export default {
    name: "Description",
    props: ['product'],
    components: {
        TechnicalDetails
    }
}

</script>