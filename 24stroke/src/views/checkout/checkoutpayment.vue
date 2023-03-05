<template>
    <div class="checkout-payment">
        <div class="row justify-content-center">
            <div class="col-10" id="payment-verify">
                <CheckoutBreadcrumbs activepage="fifth"/>
                <!-- Enter information here -->
                <div class="checkout-title text-center">
                    <h1>Verifiëren</h1>
                </div>
                <!-- <div class="loading-bar">
                    <div class="loading-spinner spinner-border text-danger"></div>
                </div> -->
                <div class="spinner-border loading-spinner text-danger" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
            </div>
            <div class="col-10 " id="payment-elements" >
                <CheckoutBreadcrumbs activepage="fourth"/>
                <!-- Enter information here -->
                <div class="checkout-title text-center">
                    <h1>Betaling</h1>
                </div>
                <div class="checkout-account-section py-3">
                    <div class="payment-title">
                        Kies hieronder uw betaalmethode
                    </div>
                    <form onsubmit="event.preventDefault()" class="form-card">
                        <div v-if=paymenterror>
                            <errorToast :message=paymenterror />
                        </div>
                        <div class="row justify-content-center mb-4 radio-group">
                             <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="ideal" :class="{ selected: activeId == 'payment-1' }" @click.prevent="activePayment('payment-1'); activePaymentMethod()"> <img class="fit-image" src="img/logo/ideal-logo.png" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="apple-pay" :class="{ selected: activeId == 'payment-2' }" @click.prevent="activePayment('payment-2'); activePaymentMethod()"> <img class="fit-image" src="img/logo/apple-pay-logo.png" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="google-pay" :class="{ selected: activeId == 'payment-3' }" @click.prevent="activePayment('payment-3'); activePaymentMethod()"> <img class="fit-image" src="img/logo/google-pay-logo.jpg" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="paypal" :class="{ selected: activeId == 'payment-4' }" @click.prevent="activePayment('payment-4'); activePaymentMethod()"> <img class="fit-image" src="https://i.imgur.com/cMk1MtK.jpg" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="bancontact" :class="{ selected: activeId == 'payment-5' }" @click.prevent="activePayment('payment-5'); activePaymentMethod()"> <img class="fit-image" src="img/logo/bancontact-logo.png" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="sofort" :class="{ selected: activeId == 'payment-6' }" @click.prevent="activePayment('payment-6'); activePaymentMethod()"> <img class="fit-image" src="img/logo/sofort-logo.png" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="klarna" :class="{ selected: activeId == 'payment-7' }" @click.prevent="activePayment('payment-7'); activePaymentMethod()"> <img class="fit-image" src="img/logo/klarna-logo.png" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="visa" :class="{ selected: activeId == 'payment-8' }" @click.prevent="activePayment('payment-8'); activePaymentMethod()"> <img class="fit-image" src="https://i.imgur.com/OdxcctP.jpg" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="american-express" :class="{ selected: activeId == 'payment-9' }" @click.prevent="activePayment('payment-9'); activePaymentMethod()"> <img class="fit-image" src="img/logo/american-express-logo.jpg" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="master" :class="{ selected: activeId == 'payment-10' }" @click.prevent="activePayment('payment-10'); activePaymentMethod()"> <img class="fit-image" src="https://i.imgur.com/WIAP9Ku.jpg" width="110px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="dk" :class="{ selected: activeId == 'payment-11' }" @click.prevent="activePayment('payment-11'); activePaymentMethod()"> <img class="fit-image" src="img/logo/maestro.png" width="110px" height="55px"> </div>
                            </div> <br>
                        </div>
                    </form>
                    <div class="row justify-content-center" v-if="activeId == 'payment-1'">
                        <div class="col-sm-4">
                            <div id="ideal-bank-element" class="ideal-stripe">
                                <!-- A Stripe Element will be inserted here. -->
                            </div>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-2' || activeId == 'payment-3'">
                        <div class="col-sm-4">
                            <div id="payment-request-button">
                                <!-- A Stripe Element will be inserted here. -->
                            </div>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-4'">
                        <div class="col-sm-4">
                            <div id="paypal-button-container"></div>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-5'">
                        <div class="col-sm-4">
                            <button class="shoppingcart-buttonbutton btn btn-success" @click="createStripeToken()">Pay with Bancontact</button>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-6'">
                        <div class="col-sm-4">
                            <button class="shoppingcart-buttonbutton btn btn-success" @click="createStripeToken()">Pay with Sofort</button>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-7'">
                        <div class="col-sm-4">
                            <p>Klarna is helaas nog niet beschikbaar</p>
                        </div>
                    </div>
                    <div class="row justify-content-center" v-if="activeId == 'payment-8' || activeId == 'payment-9' || activeId == 'payment-10' || activeId == 'payment-11'">
                        <div class="col-sm-4">
                            <!-- <div id="card-errors" role="alert" @change="errorHandlingCardStripe()"></div> -->
                            <div id="card-element"></div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="vorige-button col-2" id="payment-button-vorige">
                        <div class="shoppingcart-button">
                            <router-link to="/checkout-adres"><button type="button" class="btn btn-dark">
                                <span class="button-cart-text">Vorige</span>
                            </button></router-link>
                        </div>
                    </div>
                    <div class="col-8"></div>
                    <div class="volgende-button col-2">
                        <div class="shoppingcart-button">
                            <button type="submit" class="shoppingcart-buttonbutton btn btn-success" @click="createStripeToken()">
                                <span class="button-cart-text">Afrekenen</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>                
</template>

<style>
.checkout-payment .checkout-account-section {
    background-color: white;
    border: 1px solid #ddd;
}

.form-card {
    margin-left: 20px;
    margin-right: 20px
}

.form-card input,
.form-card textarea {
    padding: 10px 15px 5px 15px;
    border: none;
    border: 1px solid lightgrey;
    border-radius: 6px;
    margin-bottom: 25px;
    margin-top: 2px;
    width: 100%;
    box-sizing: border-box;
    font-family: arial;
    color: #2C3E50;
    font-size: 14px;
    letter-spacing: 1px
}

.form-card input:focus,
.form-card textarea:focus {
    -moz-box-shadow: 0px 0px 0px 1.5px skyblue !important;
    -webkit-box-shadow: 0px 0px 0px 1.5px skyblue !important;
    box-shadow: 0px 0px 0px 1.5px skyblue !important;
    font-weight: bold;
    border: 1px solid #304FFE;
    outline-width: 0
}

.input-group {
    position: relative;
    width: 100%;
    overflow: hidden
}

.input-group input {
    position: relative;
    height: 80px;
    margin-left: 1px;
    margin-right: 1px;
    border-radius: 6px;
    padding-top: 30px;
    padding-left: 25px
}

.input-group label {
    position: absolute;
    height: 24px;
    background: none;
    border-radius: 6px;
    line-height: 48px;
    font-size: 15px;
    color: gray;
    width: 100%;
    font-weight: 100;
    padding-left: 25px
}

input:focus+label {
    color: #304FFE
}

.btn-pay {
    background-color: #304FFE;
    height: 60px;
    color: #ffffff !important;
    font-weight: bold
}

.btn-pay:hover {
    background-color: #3F51B5
}

.fit-image {
    width: 100%;
    object-fit: cover
}

img {
    border-radius: 5px
}

.radio-group {
    position: relative;
    margin-bottom: 25px
}

.radio {
    display: inline-block;
    border-radius: 6px;
    box-sizing: border-box;
    border: 2px solid lightgrey;
    cursor: pointer;
    margin: 12px 25px 12px 0px
}

.radio:hover {
    box-shadow: 0px 0px 0px 1px rgba(0, 0, 0, 0.2)
}

.radio.selected {
    box-shadow: 0px 0px 0px 1px rgba(0, 0, 155, 0.4);
    border: 2px solid blue
}

.label-radio {
    font-weight: bold;
    color: #000000
}

.ideal-stripe {
    border: lightgray 2px solid;
    padding: 10px;
    border-radius: 6px;
}

#payment-verify {
    display: none;
}

#payment-button-vorige {
    padding-left: 12px !important;
    padding-right: 12px !important;
}

</style>

<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'
import axios from 'axios'
import errorToast from "@/components/toast/error-toast.vue"
import router from '@/router'
import { loadScript } from "@paypal/paypal-js"


export default {
    name: 'CheckoutAddress',
    components: {
        CheckoutBreadcrumbs,
        errorToast
    },
    data () {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            ideal: {},
            prButton: {},
            paymentRequestGoogleAppleLink: null,
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            house_number: '',
            street: '',
            zipcode: '',
            place: '',
            user: null,
            paymenterror: '',
            activeId: "payment-1",
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        this.user = this.$store.state.user
        this.first_name = this.$store.state.user.firstName
        this.last_name = this.$store.state.user.lastName
        this.email = this.$store.state.user.emailAddress
        this.phone = this.$store.state.user.phoneNumber
        this.zipcode = this.$store.state.user.postalCode
        this.place = this.$store.state.user.city
        this.street = this.$store.state.user.street
        this.house_number = this.$store.state.user.houseNumber

        if (this.$store.state.cart.items.length > 0) {
            this.stripe = Stripe('pk_test_51Kk6PTFE6zAlv2VHQhRTMCPyGYwlBGoNAd2QbJl5OHOgU87ErgzMeCWLIJVAo2HLSKVNTgfzD8gjBiPwFBZ1qch400cBR1sLzQ')
            const elements = this.stripe.elements();
            // var idealstyle = {
            //     base: {
            //         cursor: "pointer !important",
            //         color: "#32325d",
            //     },
            //     invalid: {
            //         color: '#FFC7EE',
            //     },
            // }
            this.ideal = elements.create('idealBank')
            this.ideal.mount("#ideal-bank-element")
        }

        if (this.$route.query.failed == "true") {
            this.paymenterror = "Er ging iets verkeerd, probeert u het opnieuw. Er is geen geld afgetrokken van uw bank."
        }

    },
    methods: {
        createOrder: function(data, actions) {
            console.log('Creating order...');
            return actions.order.create({
                purchase_units: [
                {
                    amount: {
                    value: 1,
                    },
                },
                ],
            });
        },
        onApprove: function(data, actions) {
            console.log('Order approved...');
            return actions.order.capture().then(() => {
                // this.paid = true;
                console.log('Order complete!');
                router.push({ path: 'checkout-bevestiging' })
            });
        },
        createStripeToken() {
            this.$store.commit('setIsLoading', true)
            document.getElementById('payment-elements').style.visibility = "hidden";
            document.getElementById('payment-verify').style.display = "block";
            // if (this.card != null) {
            //     this.stripe.createToken(this.card).then(result => {
            //         if (result.error) {
            //             this.$store.commit('setIsLoading', false)
            //             // this.errors.push('Something went wrong with Stripe. Please try again')
            //             console.log(result.error.message)
            //         } else {
            //             this.stripeTokenHandler(result.token, false)
            //         }
            //     })
            // } else {
            if (this.activeId == "payment-1") {
                this.stripeTokenHandler(null, true)
            }
            if (this.activeId == "payment-5") {
                this.stripeTokenHandler(null, true)
            }
            if (this.activeId == "payment-6") {
                this.stripeTokenHandler(null, true)
            }
            if (this.activeId == "payment-8" || this.activeId == "payment-9" || this.activeId == "payment-10" || this.activeId == "payment-11") {
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)
                        document.getElementById('payment-elements').style.visibility = "visible";
                        document.getElementById('payment-verify').style.display = "none";
                        console.log(result.error.message)
                        this.paymenterror = result.error.message
                    } else {
                        this.stripeTokenHandler(result.token, false)
                    }
                })
            }
            // }
        },
        async stripeTokenHandler(token, ideal) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price* item.quantity
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'house_number': this.house_number,
                'street': this.street,
                'zipcode': this.zipcode,
                'phone': this.phone,
                'city': this.place,
                'items': items,
                // 'stripe_token': token.id
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    // this.$store.commit('clearCart')
                    console.log("checkout post complete")
                    // this.$router.push('/cart/success')
                    if (ideal == true) {
                        this.idealPayment(response.data)
                    }
                    if (this.activeId == "payment-2" || this.activeId == "payment-3") {
                        this.appleGoogleLinkPayment(response.data)
                    }
                    if (this.activeId == "payment-5") {
                        this.bancontactPayment(response.data)
                    }
                    if (this.activeId == "payment-6") {
                        this.sofortPayment(response.data)
                    }
                    if (this.activeId == "payment-8" || this.activeId == "payment-9" || this.activeId == "payment-10" || this.activeId == "payment-11") {
                        this.creditcardPayment(response.data)
                    }
                })
                .catch(error => {
                    document.getElementById('payment-elements').style.visibility = "visible";
                    document.getElementById('payment-verify').style.display = "none";
                    // this.errors.push('Something went wrong. Please try again')
                    this.paymenterror = result.error.message
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
        },
        async idealPayment(token) {
            const {error} = await this.stripe.confirmIdealPayment(
                token,
                {
                    payment_method: {
                        ideal: this.ideal,
                        billing_details: {
                            name: this.first_name + " " + this.last_name,
                        },
                    },
                    return_url: 'http://localhost:8080/checkout-verifieren',
                }
            )
        },
        async appleGoogleLinkPayment(token) {
            this.paymentRequestGoogleAppleLink.on('paymentmethod', async (ev) => {
                // Confirm the PaymentIntent without handling potential next actions (yet).
                const {paymentIntent, error: confirmError} = await this.stripe.confirmCardPayment(
                    token,
                    {payment_method: ev.paymentMethod.id},
                    {handleActions: false}
                );

                if (confirmError) {
                    // Report to the browser that the payment failed, prompting it to
                    // re-show the payment interface, or show an error message and close
                    // the payment interface.
                    ev.complete('fail');
                } else {
                    // Report to the browser that the confirmation was successful, prompting
                    // it to close the browser payment method collection interface.
                    ev.complete('success');
                    // Check if the PaymentIntent requires any actions and if so let Stripe.js
                    // handle the flow. If using an API version older than "2019-02-11"
                    // instead check for: `paymentIntent.status === "requires_source_action"`.
                    if (paymentIntent.status === "requires_action") {
                    // Let Stripe.js handle the rest of the payment flow.
                        const {error} = await stripe.confirmCardPayment(token);
                        if (error) {
                            // The payment failed -- ask your customer for a new payment method.
                            this.paymenterror = "Er ging iets verkeerd, probeert u het opnieuw. Er is geen geld afgetrokken van uw bank."
                        } else {
                            // The payment has succeeded.
                            router.push({ path: 'checkout-bevestiging' })
                        }
                    } else {
                        // The payment has succeeded.
                        router.push({ path: 'checkout-bevestiging' })
                    }
                }
            });
        },
        async bancontactPayment(token) {
            const {error} = await this.stripe.confirmBancontactPayment(
                token,
                {
                    payment_method: {
                        billing_details: {
                            name: this.first_name + " " + this.last_name,
                        },
                    },
                    return_url: 'http://localhost:8080/checkout-verifieren',
                }
            )
        },
        async sofortPayment(token) {
            console.log("sofortPayment")
            const {error} = await this.stripe.confirmSofortPayment(
                token,
                {
                    payment_method: {
                        sofort: {
                            country: "NL",
                        },
                    },
                    return_url: 'http://localhost:8080/checkout-verifieren',
                }
            )
        },
        async creditcardPayment(token) {
            const {error} = await this.stripe.confirmCardPayment(
                token,
                {
                    payment_method: {
                        card: this.card,
                        billing_details: {
                            name: this.first_name + " " + this.last_name,
                        },
                    },
                }
            ).then(function(result) {
                if (result.error) {
                    document.getElementById('payment-elements').style.visibility = "visible";
                    document.getElementById('payment-verify').style.display = "none";
                    // Show error to your customer (for example, insufficient funds)
                    console.log(result.error.message);
                    this.paymenterror = result.error.message
                } else {
                    // The payment has been processed!
                    if (result.paymentIntent.status === 'succeeded') {
                        // Show a success message to your customer
                        // There's a risk of the customer closing the window before callback
                        // execution. Set up a webhook or plugin to listen for the
                        // payment_intent.succeeded event that handles any business critical
                        // post-payment actions.
                        router.push({ path: 'checkout-bevestiging' })
                    }
                } 
            })
        },
        activePayment(PaymentIdent) {
            this.activeId = this.activeId === PaymentIdent ? null : PaymentIdent
        },
        async activePaymentMethod() {
            const elements = this.stripe.elements();
            if (this.activeId == "payment-1") {
                this.card.unmount("#card-element")
                // this.ideal = elements.create('idealBank')
                await setTimeout(function(){
                    
                }, 100)
                this.ideal.mount("#ideal-bank-element")
            }
            if (this.activeId == "payment-2" || this.activeId == "payment-3") {
                await setTimeout(function(){
                    
                }, 100)
                this.appleGoogleLinkMounting()
            }
            if (this.activeId == "payment-4") {
                await setTimeout(function(){
                    
                }, 100)
                this.paypalMounting()
            }
            if (this.activeId == "payment-8" || this.activeId == "payment-9" || this.activeId == "payment-10" || this.activeId == "payment-11") {
                this.ideal.unmount("#ideal-bank-element")
                await setTimeout(function(){
                    
                }, 100)
                this.card = elements.create('card', { hidePostalCode: true })
                this.card.mount('#card-element')
            }
        },
        async appleGoogleLinkMounting() {
            const elements = this.stripe.elements();
            var amount = 0;
            await this.cart.items.forEach(item => {
                amount = amount + (item.product.price * 100)
            });
            const prGoogleAppleLink = await this.stripe.paymentRequest({
                country: 'NL',
                currency: 'eur',
                total: {
                    label: 'Demo total',
                    amount: 1,
                },
                requestPayerName: true,
                requestPayerEmail: true,
            });
            this.paymentRequestGoogleAppleLink = prGoogleAppleLink
            console.log(prGoogleAppleLink)
            this.prButton = elements.create('paymentRequestButton',  { paymentRequest: prGoogleAppleLink , } );
            console.log(this.prButton)
            const result = await this.paymentRequestGoogleAppleLink.canMakePayment();
            if (result) {
                this.prButton.mount('#payment-request-button');
            } else {
                document.getElementById('payment-request-button').style.display = 'none';
            }
            this.stripeTokenHandler(null, false)
        },
        paypalMounting() {
            loadScript({ 'client-id': "ARi8e5oF2x7FNtlDq9I4ETPpJ10Su3-wq8lWc2fHaRq_uaz8QZxnTqcsP2sgkIAyxI9ZvDOZCT8XexND", "currency": "EUR", "debug": "true", "components": "buttons,funding-eligibility" }).then((paypal) => {
            paypal
                .Buttons({
                    style: {
                        shape: 'rect',
                        color: 'blue',
                        layout: 'horizontal',
                        label: 'paypal',
                        tagline: 'false'
                    },
                    createOrder: this.createOrder,
                    onApprove: this.onApprove,
                })
                .render('#paypal-button-container');
            });
        }
        // errorHandlingCardStripe() {
        //     this.card.on('change', ({error}) => {
        //         let displayError = document.getElementById('card-errors');
        //         if (error) {
        //             displayError.textContent = error.message;
        //         } else {
        //             displayError.textContent = '';
        //         }
        //     })
        // }
    },
}
</script>