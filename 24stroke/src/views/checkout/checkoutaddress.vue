<template>
    <div class="checkout-address">
        <div class="row justify-content-center">
            <div class="col-10">
                <form>
                <CheckoutBreadcrumbs activepage="third"/>
                <!-- Enter information here -->
                <div class="checkout-title">
                    <h1>Uw adres</h1>
                </div>
                <div class="checkout-account-section">
                    <div class="row">
                        <div class="login-section col-6">
                                <div class="login-title">
                                    <h2>Verzend adres</h2>
                                </div>
                                <div class="email-title">
                                    <p>Voornaam</p>
                                </div>
                                <div class="form">
                                    <input class="form-control" v-model="firstName">
                                </div>
                                <div class="email-title">
                                    <p>Achternaam</p>
                                </div>
                                <div class="email-form">
                                    <input class="form-control" v-model="lastName">
                                </div>
                                <div class="row">
                                    <div class="col-3">
                                        <div class="email-title">
                                            <p>Postcode</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control" v-model="postalCode">
                                        </div>
                                    </div>
                                    <div class="col-9">
                                        <div class="email-title">
                                            <p>Stad</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control" v-model="city">
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-9">
                                        <div class="email-title">
                                            <p>Straat</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control" v-model="street">
                                        </div>
                                    </div>
                                    <div class="col-3">
                                        <div class="email-title">
                                            <p>Huisnummer</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control" v-model="houseNumber">
                                        </div>
                                    </div>
                                </div>
                                <div class="email-title">
                                    <p>Telefoonnummer</p>
                                </div>
                                <div class="email-form">
                                    <input class="form-control" v-model="phoneNumber">
                                </div>
                                <div class="email-title">
                                    <p>E-mail adres</p>
                                </div>
                                <div class="email-form">
                                    <input class="form-control" v-model="emailAddress" />
                                </div>
                                <div class="email-title">
                                    <p>Herhaal E-mail adres</p>
                                </div>
                                <div class="email-form">
                                    <input class="form-control">
                                </div>
                        </div>
                        <div class="col-6">
                            <div class="row justify-content-end">
                                <div class="register-section col-11">
                                    <div class="login-title">
                                        <h2>Factuur adres</h2>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" v-model="differentAddress" value="one" checked>
                                        <label class="form-check-label" for="flexRadioDefault1">
                                            factuur adres is hetzelfde als verzend adres
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" v-model="differentAddress" value="two">
                                        <label class="form-check-label" for="flexRadioDefault2">
                                            Ander factuur adres dan het verzend adres
                                        </label>
                                    </div>
                                    <div class="different-address-div" v-show="differentAddress === 'two'">
                                        <div class="email-title">
                                            <p>Voornaam</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control">
                                        </div>
                                        <div class="email-title">
                                            <p>Achternaam</p>
                                        </div>
                                        <div class="email-form">
                                            <input class="form-control">
                                        </div>
                                        <div class="row">
                                            <div class="col-3">
                                                <div class="email-title">
                                                    <p>Postcode</p>
                                                </div>
                                                <div class="email-form">
                                                    <input class="form-control">
                                                </div>
                                            </div>
                                            <div class="col-9">
                                                <div class="email-title">
                                                    <p>Stad</p>
                                                </div>
                                                <div class="email-form">
                                                    <input class="form-control">
                                                </div>
                                            </div>
                                        </div>
                                        <div class="row">
                                            <div class="col-9">
                                                <div class="email-title">
                                                    <p>Straat</p>
                                                </div>
                                                <div class="email-form">
                                                    <input class="form-control">
                                                </div>
                                            </div>
                                            <div class="col-3">
                                                <div class="email-title">
                                                    <p>Huisnummer</p>
                                                </div>
                                                <div class="email-form">
                                                    <input class="form-control">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="vorige-button col-2">
                        <div class="shoppingcart-button">
                            <button type="button" class="btn btn-dark" @click="linkToAccount()">
                                <span class="button-cart-text">Vorige</span>
                            </button>
                        </div>
                    </div>
                    <div class="col-8"></div>
                    <div class="volgende-button col-2">
                        <div class="shoppingcart-button">
                            <button type="submit" class="shoppingcart-buttonbutton btn btn-success" @click="userInfo()">
                                <span class="button-cart-text">Volgende</span>
                            </button>
                        </div>
                    </div>
                </div>
                </form>
            </div>
        </div>
    </div>                
</template>

<style>
.vorige-button {
    padding-left: 0 !important;
}

.volgende-button {
    padding-right: 0 !important;
}

.vorige-button button {
    width: 100% !important;
}

.checkout-address .login-section, .checkout-address .register-section {
    margin-top: 15px !important;
    margin-bottom: 25px;
}
</style>

<script>
import CheckoutBreadcrumbs from '@/components/checkoutBreadcrumbs.vue'

export default {
    name: 'CheckoutAddress',
    components: {
        CheckoutBreadcrumbs
    },
    data() {
        return {
            differentAddress: "one",
            emailAddress: '',
            firstName: '',
            lastName: '',
            postalCode: '',
            city: '',
            street: '',
            houseNumber: '',
            phoneNumber: '',
            authenticated: false
        }
    },
    methods: {
        userInfo() {
            const user = {
                emailAddress: this.emailAddress,
                firstName: this.firstName,
                lastName: this.lastName,
                postalCode: this.postalCode,
                city: this.city,
                houseNumber: this.houseNumber,
                street: this.street,
                phoneNumber: this.phoneNumber,
            }

            this.$store.commit('userInfo', user)
            this.$router.push({ path: '/checkout-betaling' })
        },
        linkToAccount () {
            console.log(this.authenticated)
            if (this.authenticated == true) {
                this.$router.push('/checkout-auth')
            } else {
                this.$router.push('/checkout')
            }
        },
        prefill(account) {
            if (this.authenticated == true) {
                this.emailAddress = account.emailAddress
                console.log(account)
                console.log(this.emailAddress)
                this.firstName = account.firstName
                this.lastName = account.lastName
                this.postalCode = account.postalCode
                this.city = account.city
                this.houseNumber = account.houseNumber
                this.street = account.street
                this.phoneNumber = account.phoneNumber
            }
        }
    },
    mounted() {
        this.user = this.$store.state.user
        this.authenticated = this.$store.state.isAuthenticated
        this.prefill(this.$store.state.user)
    },
}
</script>