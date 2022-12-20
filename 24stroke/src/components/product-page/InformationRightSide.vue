<template>
    <div>
        <div class="brand-productno row">
            <div class="brand col">
                <span class="product-brand-label">Motoforce</span>
            </div>
            <div class="productno col">
                <span class="product-article-label">Artikel nr.: MF23.16694</span>
            </div>
        </div>
        <div class="product-big-title">
            <h2>{{ product.name }}</h2>
        </div>
        <hr class="seperation-line-product">
        <div class="price-stock">
            <div class="row">
                <div class="price col">
                    <p>{{ product.price }} €</p>
                </div>
                <div class="stock col g-0">
                    <hr class="stock-line">
                    <p>Op voorraad</p>
                </div>
            </div>
        </div>
        <hr class="seperation-line-product">
        <div class="addto-cart-section">
            <div class="row">
                <div class="quantity-div col-3">
                    <div class="quantity-toggle justify-content-center">
                        <button :disabled="isDisabled" class="increment" @click="decrement()"
                            v-bind:class="{ 'increment-disabled': isDisabled }">-</button>
                        <input class="quantity" type="number" min="1" v-model="quantity"
                            v-bind:class="{ 'quantity-big': this.lessthan }" readonly>
                        <button class="decrement" @click="increment()">+</button>
                    </div>
                </div>
                <div class="cart-button col-7">
                    <div class="shoppingcart-button">
                        <button type="button" class="shoppingcart-buttonbutton btn btn-success"
                            @click="addToCart">
                            <span class="button-cart-icon">
                                <font-awesome-icon icon="shopping-cart"
                                    :style="{ color: 'white', width: '18px', height: '18px' }" />
                            </span>
                            <span class="button-cart-text">In winkelwagen</span>
                        </button>
                    </div>
                    <!-- Modal -->
                    <div class="modal fade" ref="cartAddedModal" tabindex="-1" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered modal-sm">
                            <div class="modal-content">
                                <div class="modal-body">
                                    <!-- <font-awesome-icon icon="check-square" :style="{ marginBottom: '-200px', width: '100px', height:'100px', opacity: 0.3, color: '#00AA00' }" class="mx-auto d-block"/> -->
                                    <img class="modal-image img-fluid mx-auto d-block"
                                        v-bind:src="product.get_image">
                                    <p class="modal-text">Dit product is {{ quantity }} keer
                                        toegevoegd aan uw winkelwagentje</p>
                                    <button type="button"
                                        class="modal-button1 btn btn-success mx-auto d-block"
                                        @click="modal.hide(), item.quantity = 1">Doorgaan met
                                        winkelen</button>
                                    <button type="button"
                                        class="modal-button2 btn btn-dangerr mx-auto d-block"
                                        @click="modal.hide(), $router.push('/winkelwagen')">Naar
                                        winkelwagen</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- einde modal -->
                </div>
                <div class="wishlist-icon col-2" @click="addToWishlist(product)">
                    <div class="fullheart" v-if="wishlist">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                            <path fill="#FF2400"
                                d="M0 190.9V185.1C0 115.2 50.52 55.58 119.4 44.1C164.1 36.51 211.4 51.37 244 84.02L256 96L267.1 84.02C300.6 51.37 347 36.51 392.6 44.1C461.5 55.58 512 115.2 512 185.1V190.9C512 232.4 494.8 272.1 464.4 300.4L283.7 469.1C276.2 476.1 266.3 480 256 480C245.7 480 235.8 476.1 228.3 469.1L47.59 300.4C17.23 272.1 .0003 232.4 .0003 190.9L0 190.9z" />
                        </svg>
                    </div>
                    <div class="heart-outline" v-if="wishlist == false">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                            <path fill="#FF2400"
                                d="M244 84L255.1 96L267.1 84.02C300.6 51.37 347 36.51 392.6 44.1C461.5 55.58 512 115.2 512 185.1V190.9C512 232.4 494.8 272.1 464.4 300.4L283.7 469.1C276.2 476.1 266.3 480 256 480C245.7 480 235.8 476.1 228.3 469.1L47.59 300.4C17.23 272.1 0 232.4 0 190.9V185.1C0 115.2 50.52 55.58 119.4 44.1C164.1 36.51 211.4 51.37 244 84C243.1 84 244 84.01 244 84L244 84zM255.1 163.9L210.1 117.1C188.4 96.28 157.6 86.4 127.3 91.44C81.55 99.07 48 138.7 48 185.1V190.9C48 219.1 59.71 246.1 80.34 265.3L256 429.3L431.7 265.3C452.3 246.1 464 219.1 464 190.9V185.1C464 138.7 430.4 99.07 384.7 91.44C354.4 86.4 323.6 96.28 301.9 117.1L255.1 163.9z" />
                        </svg>
                    </div>
                </div>
            </div>
            <hr class="seperation-line-product">
            <div class="perks">
                <div class="row">
                    <div class="perk-element col-12">
                        <span>
                            <font-awesome-icon icon="check"
                                :style="{ color: '#00AA00', width: '23px', height: '23px', marginRight: '10px' }" />
                        </span>
                        <span class="icon-text-perks">Snelle levering</span>
                    </div>
                    <div class="perk-element col-12">
                        <span>
                            <font-awesome-icon icon="check"
                                :style="{ color: '#00AA00', width: '23px', height: '23px', marginRight: '10px' }" />
                        </span>
                        <span class="icon-text-perks">Gratis verzending</span>
                    </div>
                    <div class="perk-element col-12">
                        <span>
                            <font-awesome-icon icon="check"
                                :style="{ color: '#00AA00', width: '23px', height: '23px', marginRight: '10px' }" />
                        </span>
                        <span class="icon-text-perks">eenvoudig retourneren</span>
                    </div>
                    <div class="perk-element col-12">
                        <span>
                            <font-awesome-icon icon="check"
                                :style="{ color: '#00AA00', width: '23px', height: '23px', marginRight: '10px' }" />
                        </span>
                        <span class="icon-text-perks">Laagste prijsgarantie</span>
                    </div>
                    <div class="perk-element col-12">
                        <span>
                            <font-awesome-icon icon="check"
                                :style="{ color: '#00AA00', width: '23px', height: '23px', marginRight: '10px' }" />
                        </span>
                        <span class="icon-text-perks">retourneren tot 60 dagen</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.product-small-information {
    background-color: white;
    text-align: left;
    padding: 20px;
    padding-left: 20px !important;
    padding-right: 20px !important;
}

.product-brand-label,
.product-article-label {
    color: #6b6b6b;
    background: #fff;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    padding: 3px 10px;
    top: 10px;
    left: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    opacity: 0.8;
}

.product-article-label {
    left: auto;
    right: 10px;
}

.productno {
    text-align: right;
}

.product-big-title {
    margin-top: 15px;
    height: 85px;
    margin-bottom: 10px;
}

.product-big-title h2 {
    font-size: 1.5vw;
}

.seperation-line-product {
    margin-top: 0px;
    margin-bottom: 8px;
}

.product-information .price {
    color: #2c3e50;
    font-size: 2vw;
    font-weight: 500;
}

.product-information .stock {
    text-align: right;
    color: #2c3e50;
    font-weight: 400;
    font-size: 1.3vw;
}

.product-information .stock-line {
    height: 5px;
    border-width: 0;
    color: #00AA00;
    background-color: #00AA00;
    opacity: 1;
    margin: 0px;
    width: 38%;
    margin-left: 62%;
    margin-top: 8px;
}

.price p,
.stock p {
    margin-bottom: 3px;
}

.quantity-div {
    width: 2.5rem;
    text-align: center;
    padding: 0.45rem;
    padding-left: 0.9rem;
    padding-right: 0rem;
}

.quantity-toggle {
    display: flex;
    position: relative;
    top: calc(50% - 24px);
    /* 50% - 3/4 of icon height or 5/8 height*/
}

.quantity,
.quantity-big {
    border: 0;
    border-top: 2px solid #ddd;
    border-bottom: 2px solid #ddd;
    width: 2.5rem;
    text-align: center;
    padding: 0.45rem;
    padding-left: 0.9rem;
    padding-right: 0rem;
    cursor: default;
}

.quantity-big {
    padding-left: 0.45rem !important;
}

.decrement,
.increment,
.increment-disabled {
    border: 2px solid #ddd;
    padding: 0.45rem 0.5rem;
    background: white;
    color: #2c3e50;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 500;
}

.increment {
    padding: 0.45rem 0.6rem !important;
    font-weight: 600 !important;
    border-radius: 6px 0px 0px 6px;
}

.increment-disabled {
    color: #ddd !important;
    cursor: default !important;
}

.decrement {
    border-radius: 0px 6px 6px 0px;
}

.wishlist-icon {
    text-align: center;
}

.fullheart,
.heart-outline {
    position: relative;
    top: calc(50% - 25px);
    /* 50% - 3/4 of icon height or 5/8 height*/
    width: 40px;
    height: 40px;
    cursor: pointer;
}

.perk-element {
    margin-top: 10px !important;
}

.icon-text-perks {
    font-size: 1vw;
    font-weight: 400;
}

.img-modal {
    border-radius: 100%;
}

.modal-text {
    text-align: center !important;
}

.modal-button1 {
    background-color: #00AA00 !important;
    border: 0 !important;
}

.modal-button2 {
    margin-top: 10px;
    color: #00AA00 !important;
}

.modal-image {
    width: 250px;
    height: 250px;
}
</style>

<script>
import { Modal } from 'bootstrap'

export default {
    name: 'InformationRightSide',
    props: ['product'],
    data() {
        return {
            products: this.product,
            quantity: 1,
            lessthan: false,
            disabledIncrement: false,
            modal: null,
            wishlist: false,
            wishlistItems: []
        }
    },
    mounted() {
        this.modal = new Modal(this.$refs.cartAddedModal)
        this.wishlistItems = this.$store.state.wishlist
        this.onWishlist()
    },
    methods: {
        increment() {
            this.quantity++
            if (this.quantity < 9) {
                this.lessthan = false
            } else if (this.quantity > 9) {
                this.lessthan = true
            }
        },
        decrement() {
            this.quantity--
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
            this.modal.show()
        },
        addToWishlist(item) {
            this.wishlist = !this.wishlist
            if (this.wishlist == true) {
                this.$store.commit('addToWishlist', this.product)
            }
            else if (this.wishlist == false) {
                this.wishlistItems.items = this.wishlistItems.items.filter(i => i.id != this.product.id)
                this.$store.commit('removeFromWishlist', this.wishlistItems)
            }
            this.updateWishlist()
        },
        updateWishlist() {
            localStorage.setItem('wishlist', JSON.stringify(this.$store.state.wishlist))
        },
        onWishlist() {
            this.wishlistItems.items.forEach(item => {
                if (item.id === this.products.id) {
                    this.wishlist = true;
                }
            });
        }
    },
    computed: {
        isDisabled: function () {
            if (this.quantity === 1) {
                return this.disabledIncrement = true
            }
        }
    }
}
</script>