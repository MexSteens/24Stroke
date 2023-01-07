<template>
    <div class="template">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="first"/>
                <!-- Enter information here -->
                <div class="cart">
                    <div class="cart-head row justify-content-start">
                        <div class="cart-title col-5">
                            <span><font-awesome-icon class="shopping-basket-icon" icon="shopping-basket"/></span>
                            <span>Mijn Winkelwagen</span>
                        </div>
                        <div class="cart-item-no col-2 text-muted">
                            <span class="cart-item-no-top">{{ cartTotalLength }} producten</span>
                        </div>
                    </div>
                    <div class="cart-cart row">
                        <div class="cart-items col-7">
                            <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item" v-on:removeFromCart="removeFromCart" /> 
                        </div>
                        <div class="col-1"></div>
                        <div class="cart-summary col-4">
                            <h2>Overzicht</h2>
                            <div class="cartsummary-row row">
                                <div class="cartsummary-information col-10">
                                    <p>Subtotaal (inclusief &euro; {{ cartTotalBTW.toFixed(2) }} BTW)</p>
                                </div>
                                <div class="cartsummary-price col-2">
                                    <p>{{ cartTotalPrice.toFixed(2) }}</p>
                                </div>
                            </div>
                            <div class="cartsummary-row row">
                                <div class="cartsummary-information col-10">
                                    <p>Verzendkosten (PostNL-levering)</p>
                                </div>
                                <div class="cartsummary-price col-2">
                                    <p>{5,95}</p>
                                </div>
                            </div>
                            <hr class="summary-hr">
                            <div class="cartsummary-row row">
                                <div class="cartsummary-information-total col-10">
                                    <p>Totale orderwaarde</p>
                                </div>
                                <div class="cartsummary-price-total col-2">
                                    <p>{5,95}</p>
                                </div>
                            </div>
                            <div class="shoppingcart-button">
                                <button v-if="cart.items.length == 0" type="button" class="shoppingcart-buttonbutton-disabled btn btn-success">
                                    <span class="button-cart-text">Afrekenen</span>
                                </button>
                                <button v-if="cart.items.length > 0" type="button" class="shoppingcart-buttonbutton btn btn-success" @click="$router.push('checkout')">
                                    <span class="button-cart-text">Afrekenen</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.cart-head {
    font-size: 1.7vw;
    margin-top: 25px !important;
    margin-bottom: 15px !important;
}

.cart-title {
    text-align: left;
    font-weight: 600;
}

.shopping-basket-icon {
    margin-right: 25px;
    margin-left: 6px;
}

.cart-item-no {
    font-size: 1.2vw;
    margin-top: 10px !important;
    text-align: right;
    padding-right: 20px !important;
}

.cart-item {
    background-color: white;
    border: 1px solid #ddd;
}

.cart-product-title {
    font-size: 1vw;
    text-align: left;
}

.cart-product-price {
    font-size: 1vw;
    text-align: right;
}



.cart-summary {
    background-color: white;
    border: 1px solid #ddd;
    text-align: left;
    padding: 10px 20px !important;
}

.cart-summary p {
    font-size: 1vw;
}

.cart-summary h2 {
    margin-bottom: 20px;
    font-size: 1.7vw;
}

.cartsummary-price, .cartsummary-price-total {
    text-align: right;
}
</style>

<script>
import axios from 'axios'
import CartItem from '@/components/cartItem.vue'
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'

export default {
    name: 'Cart',
    components: {
        CartItem,
        CheckoutBreadcrumbs
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalBTW() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity * 0.21
            }, 0)
        },
    }
}
</script>