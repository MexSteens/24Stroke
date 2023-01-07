<template>
    <div class="product-box-slider m-2 mx-4">
        <div class="product-grid"><router-link v-bind:to="product.get_absolute_url" class="routerlink">
            <div class="product-image">
                    <img class="img-1" v-bind:src="product.get_thumbnail">
                <span class="product-brand-label">Motoforce</span>
            </div></router-link>
            <div class="product-content">
                <ul class="rating">
                    <li class=""><font-awesome-icon icon="star"/></li>
                    <li class=""><font-awesome-icon icon="star"/></li>
                    <li class=""><font-awesome-icon icon="star"/></li>
                    <li class=""><font-awesome-icon icon="star"/></li>
                    <li class="disable"><font-awesome-icon icon="star"/></li>
                    <li class="disable">(1 reviews)</li>
                </ul>
                <div class="product-title"><router-link v-bind:to="product.get_absolute_url" class="routerlink">
                    <div class="product-title">
                    <h3 class="title">{{ product.name }}</h3>
                </div></router-link>
                </div>
                <div class="price-stock">
                    <div class="row">
                        <div class="price col"><p>{{ product.price}} €</p></div>
                        <div class="stock col g-0">
                            <hr class="stock-line">
                            <p>Op voorraad</p>
                        </div>
                    </div>
                </div>
                <div class="shoppingcart-button">
                    <button type="button" class="shoppingcart-buttonbutton btn btn-success" @click="addToCart">
                            <span class="button-cart-icon"><font-awesome-icon icon="shopping-cart" :style="{ color: 'white', width: '18px', height: '18px'}" /></span>
                            <span class="button-cart-text">In winkelwagen</span>
                    </button>
                    <!-- Modal -->
                    <div class="modal fade" ref="cartAddedModal" tabindex="-1" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-sm">
                            <div class="modal-content">
                            <div class="modal-body">
                                <img class="img-fluid mx-auto d-block" v-bind:src="product.get_image">
                                <p class="modal-text">Dit product is toegevoegd aan uw winkelwagentje</p>
                                <button type="button" class="modal-button1 btn btn-success mx-auto d-block" @click="modal.hide(), item.quantity = 1">Doorgaan met winkelen</button>
                                <button type="button" class="modal-button2 btn btn-dangerr mx-auto d-block" @click="modal.hide(), $router.push('/winkelwagen')">Naar winkelwagen</button>
                            </div>
                            </div>
                        </div>
                    </div>
                    <!-- einde modal -->
                </div>
            </div> 
        </div>
    </div>
</template>

<script>
import { Modal } from 'bootstrap'

export default {
    name: 'ProductBox',
    props: {
        product: Object
    },
    methods: {
        addToCart() {
        if (isNaN(this.quantity) || this.quantity < 1) {
            this.quantity = 1
        }

        const item = {
            product: this.product,
            quantity: 1
        }

        this.$store.commit('addToCart', item)
        this.modal.show()
        },
    },
    mounted() {
        this.modal = new Modal(this.$refs.cartAddedModal)
    }
}
</script>

<style>
.product-box-slider {
    border: 2px solid #cacaca;
}

.product-grid .product-image {
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.product-grid .product-image a.image {
    display: block; 
}

.product-grid .product-image img{
    width: 100%;
    height: auto;
}

.product-grid .product-brand-label,
.product-grid .product-discount-label {
    color: #6b6b6b;
    background: #fff;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    padding: 3px 10px;
    position: absolute;
    top: 10px;
    left: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    opacity: 0.8;
}

.product-grid .product-discount-label {
    background: #ff3939;
    left: auto;
    right: 10px;
}

.product-grid .product-view {
    color: #fff;
    background:#000;
    font-size: 0.9rem;
    text-align: right;
    line-height: 50px;
    width: 60px;
    height: 60px;
    padding: 0 16px 0 0;
    border-radius: 50px;
    opacity: 0;
    transform: scale(0);
    position: absolute;
    bottom: -40px;
    left: -40px;
    transition: all .3s ease;
}

.product-grid .product-links {
    padding: 0;
    margin: 0;
    list-style: none;
    transform: translateY(50%);
    position: absolute;
    bottom: 50%;
    right: 10px;
    z-index: 1;
}

.product-grid .product-content {
    background: #fff;
    text-align: left;
    padding-left: 15px;
    padding-right: 15px;
}

.product-grid .rating {
    color: #f7bc3d;
    font-size: 11px;
    padding: 0;
    margin: 0 0 8px;
    list-style: none;
}

.product-grid .rating li { 
    display: inline-block; 
}
.product-grid .rating .disable { 
    color: #a3a3a3; 
}

.product-grid .title {
    font-size: 15px;
    font-weight: 500;
    text-transform: capitalize;
    margin: 0 0 8px;
}
.product-grid .title a {
    color: #333;
    transition: all 0.3s ease 0s;
}
.product-grid .title a:hover { 
    color: #ca1b00; 
}

.product-grid .price {
    color: #2c3e50;
    font-size: 20px;
    font-weight: 500;
}

.product-grid .stock {
    text-align: right;
    color: #2c3e50;
    font-weight: 400;
}

.product-grid .stock-line {
    height: 3px;
    border-width: 0;
    color: #00AA00;
    background-color: #00AA00;
    opacity: 1;
    margin: 0px;
    width: 50%;
    margin-left: 51%;
    margin-top: 4px;
}

.shoppingcart-button {
    padding-bottom: 20px;
    padding-top: 15px;
}

.shoppingcart-buttonbutton, .shoppingcart-buttonbutton-disabled {
    width: 100%;
    background-color: #1cad00 !important;
    border-color: #1cad00 !important;
}

.shoppingcart-buttonbutton-disabled {
    cursor: not-allowed !important;
    background-color: #1dad0091 !important;
    border-color: #1dad0091 !important;
}

.product-title {
    height: 60px;
}

.button-cart-text {
    font-size: 1rem;
    font-weight: 500;
    margin-left: 10px;
}

.product-grid .price span {
    color: #999;
    font-size: 14px;
    font-weight: 400;
    text-decoration: line-through;
    margin-right: 5px;
}

.products-row {
    margin-bottom: 25px;
}

@media screen and (max-width: 990px) {
    .product-grid{ margin-bottom: 30px; }
}

/*----- test -----*/


.cilinders-product-page {
    background-color: #F0F1F2;
}

.total-product-1, .total-product-2, .total-product-3, .total-product-4 {
    padding: 0px;
    height: 250px;
    background-color: white;
}

.total-product-1 {
    border-right: 8px solid #F0F1F2;
}

.total-product-2 {
    border-right: 6px solid #F0F1F2;
    border-left: 4px solid #F0F1F2;
}

.total-product-3 {
    border-right: 4px solid #F0F1F2;
    border-left: 6px solid #F0F1F2;
}

.total-product-4 {
    border-left: 8px solid #F0F1F2;
}

.product-image-row {
    height: 100px;
}
</style>

