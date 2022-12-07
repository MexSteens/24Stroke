<template>
    <div class="checkout-payment">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="fourth"/>
                <!-- Enter information here -->
                <div class="checkout-title">
                    <h1>Betaling</h1>
                </div>
                <div class="checkout-account-section">
                    <div class="payment-title">
                        Kies hieronder uw betaalmethode
                    </div>
                    <form onsubmit="event.preventDefault()" class="form-card">
                        <div class="row justify-content-center mb-4 radio-group">
                             <div class="col-sm-1 col-5">
                                <div class='radio selected mx-auto' data-value="ideal"> <img class="fit-image" src="img/logo/ideal-logo.png" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="apple-pay"> <img class="fit-image" src="img/logo/apple-pay-logo.png" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="google-pay"> <img class="fit-image" src="img/logo/google-pay-logo.jpg" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="paypal"> <img class="fit-image" src="https://i.imgur.com/cMk1MtK.jpg" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="bancontact"> <img class="fit-image" src="img/logo/bancontact-logo.png" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="sofort"> <img class="fit-image" src="img/logo/sofort-logo.png" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="klarna"> <img class="fit-image" src="img/logo/klarna-logo.png" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="visa"> <img class="fit-image" src="https://i.imgur.com/OdxcctP.jpg" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="american-express"> <img class="fit-image" src="img/logo/american-express-logo.jpg" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="master"> <img class="fit-image" src="https://i.imgur.com/WIAP9Ku.jpg" width="105px" height="55px"> </div>
                            </div>
                            <div class="col-sm-1 col-5">
                                <div class='radio mx-auto' data-value="dk"> <img class="fit-image" src="https://i.imgur.com/5TqiRQV.jpg" width="105px" height="55px"> </div>
                            </div> <br>
                        </div>
                    </form>
                </div>
                <div class="row">
                    <div class="vorige-button col-2">
                        <div class="shoppingcart-button">
                            <button type="button" class="btn btn-dark">
                                <span class="button-cart-text">Vorige</span>
                            </button>
                        </div>
                    </div>
                    <div class="col-8"></div>
                    <div class="volgende-button col-2">
                        <div class="shoppingcart-button">
                            <button type="submit" class="shoppingcart-buttonbutton btn btn-success">
                                <span class="button-cart-text">Volgende</span>
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
</style>


<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'

export default {
    name: 'CheckoutAddress',
    components: {
        CheckoutBreadcrumbs
    },
}
</script>