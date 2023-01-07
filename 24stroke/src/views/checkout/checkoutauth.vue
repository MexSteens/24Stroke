<template>
    <div class="checkout">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="second" />
                <!-- Enter information here -->
                <Account />
                <div class="row">
                    <div class="vorige-button col-2">
                        <div class="shoppingcart-button">
                            <router-link to="/winkelwagen"><button type="button" class="btn btn-dark">
                                <span class="button-cart-text">Vorige</span>
                            </button></router-link>
                        </div>
                    </div>
                    <div class="col-8"></div>
                    <div class="volgende-button col-2">
                        <div class="shoppingcart-button">
                            <router-link to="/checkout-adres"><button type="submit" class="shoppingcart-buttonbutton btn btn-success">
                                <span class="button-cart-text">Volgende</span>
                            </button></router-link>
                        </div>
                    </div>
                </div>
            </div>  
        </div>
    </div>  
</template>

<script>
import Account from '../cart-login-account/account.vue'
import CheckoutBreadcrumbs from '../../components/checkoutBreadcrumbs.vue';

export default ({
    name: "CheckoutAuth",
    components: {
        Account,
        CheckoutBreadcrumbs
    }
})
</script>