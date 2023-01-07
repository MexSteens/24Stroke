<template>
    <div class="checkout">
        <div class="row justify-content-center">
            <div class="col-10">
                <CheckoutBreadcrumbs activepage="second" />
                <!-- Enter information here -->
                <div class="checkout-title">
                    <h1>Uw Account</h1>
                </div>
                <div class="checkout-account-section">
                    <div class="row">
                        <div class="login-section col-6">
                            <form @submit.prevent="submitForm">
                                <div class="login-title">
                                    <h2>Inloggen</h2>
                                </div>
                                <div class="login-subtitle">
                                    <h4>Voor bestaande klanten</h4>
                                </div>
                                <div class="email-title">
                                    <p>E-mail adres</p>
                                </div>
                                <div class="email-form">
                                    <input type="email" class="form-control" placeholder="E-mail adres"
                                        v-model="username">
                                </div>
                                <div class="password-title">
                                    <p>Wachtwoord</p>
                                </div>
                                <div class="password-form">
                                    <input type="password" class="form-control" placeholder="Wachtwoord"
                                        v-model="password">
                                </div>
                                <div class="login-buttonpart">
                                    <div class="row">
                                        <div class="login-button col-5">
                                            <div class="shoppingcart-button">
                                                <button type="submit" class="shoppingcart-buttonbutton btn btn-success">
                                                    <span class="button-cart-text">Inloggen</span>
                                                </button>
                                            </div>
                                        </div>
                                        <div class="forgot-password-link col-7">
                                            <router-link class="routerlink" to="/resetpassword">Inloggegevens vergeten
                                            </router-link>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div class="col-6">
                            <div class="row justify-content-end">
                                <div class="register-section col-11">
                                    <div class="login-title">
                                        <h2>Registreren</h2>
                                    </div>
                                    <div class="login-subtitle">
                                        <h4>Als nieuwe klant bij 24stroke</h4>
                                    </div>
                                    <div class="register-button">
                                        <div class="shopnubutton col-6">
                                            <button type="button" class="btn btn-dark" @click="$router.push('/registreer')">Registreer eenvoudig</button>
                                        </div>
                                    </div>
                                </div>
                                <div class="guest-section col-11">
                                    <div class="login-title">
                                        <h2>Doorgaan als gast</h2>
                                    </div>
                                    <div class="login-subtitle">
                                        <h4>doorgaan zonder te registreren</h4>
                                    </div>
                                    <div class="register-button">
                                        <div class="shopnubutton col-6">
                                            <button type="button" class="btn btn-dark"
                                                @click="$router.push('/checkout-adres')">Ga door als gast</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.checkout-title {
    text-align: left;
    margin-top: 60px;
}

.checkout .guest-section {
    margin-top: 0px !important;
}

.checkout .register-section {
    margin-bottom: 35px !important;
}

.checkout .register-section,
.checkout .login-section {
    margin-top: 15px !important;
}
</style>

<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'
import store from '../../store'

export default {
    name: 'Checkout',
    components: {
        CheckoutBreadcrumbs
    },
    created() {
        if (store.state.isAuthenticated == true){
            this.$router.push('/checkout-adres')
        }
    }
}
</script>