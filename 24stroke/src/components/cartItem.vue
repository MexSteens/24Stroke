<template>
    <div class="cart-item">
        <div class="row">
            <div class="row main align-items-center">
                <div class="image-padding-cart col-2">
                    <div class="row justify-content-center">
                        <div class="col-10"><img class="img-fluid" v-bind:src="item.product.get_thumbnail"></div>
                    </div>
                </div>
                <div class="cart-product-title col-6">
                    <div class="row text-muted"></div>
                    <div class="row"><router-link clas="item-link" :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></div>
                </div>
                <div class="quantity-div col-2">
                    <div class="quantity-toggle justify-content-center">
                        <button class="increment" @click="decrementQuantity(item)" >-</button>
                        <input  class="quantity" type="number" min="1" v-model="item.quantity" readonly>
                        <button class="decrement" @click="incrementQuantity(item)">+</button>
                                <!-- Modal -->
                        <div class="modal fade" ref="exampleModal" tabindex="-1" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Verwijder item</h5>
                                    <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <p>Weet u zeker dat u {{ item.product.name }} wilt verwijderen uit uw winkelwagen?</p>
                                    <div class="row">
                                        <div class="col-6"><button type="button" class="shoppingcart-buttonbutton btn btn-success" @click="modal.hide(), item.quantity = 1">nee, annuleer verwijder</button></div>
                                        <div class="col-6"><button type="button" class="btn btn-danger" @click="removeFromCart(item), modal.hide()">Ja, verwijder</button></div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                                <!-- einde modal -->
                    </div>
                </div>
                <div class="cart-product-price col-2">&euro; {{ getItemTotal(item).toFixed(2) }} <span class="close" @click="modal.show()"> &#10005;</span></div>
            </div>
        </div>
    </div>
</template>

<script>
import { Modal } from 'bootstrap'

export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem,
            confirmRemove: false,
            modal: null,
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1
            if (item.quantity === 0) {
                this.modal.show()
                item.quantity = 1
            }
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
    },
    mounted() {
        this.modal = new Modal(this.$refs.exampleModal, )
    }
}
</script>

<style>
.image-padding-cart {
    padding: 20px;
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
    font-size: 1.3vw !important;
    text-align: right;
}

.cart-item a {
    color: #2c3e50 !important;
}

.cart-item a:hover {
    text-decoration: underline !important;
}

.cart-item .quantity {
    width: 3rem;
}

.close {
    cursor: pointer;
}

.close:hover {
    transition: all 0.3s ease 0s;
    color: #ca1b00;
}
</style>