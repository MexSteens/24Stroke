<template>
    <div class="template">
        <div class="row justify-content-center">
            <div class="col-10">
                <!-- Enter information here -->
                <div class="register">
                    <div class="row">
                        <div class="login-section col-6">
                            <div class="show-errors" v-if="errors.length">
                                <div class="toasts" v-for="(error, index) in errors" :key="index">
                                    <errorToast :message=errors[index] />
                                </div>
                            </div>
                            <div class="show-succes" v-if="succes">
                                <succesToast message="Uw account is aangemaakt, u kunt nu inloggen!" />
                            </div>
                            <form @submit.prevent="submitForm">
                                <div class="login-title">
                                    <h2>Registreren</h2>
                                </div>
                                <div class="login-subtitle">
                                    <h4>Als nieuwe klant bij 24stroke</h4>
                                </div>
                                <div class="email-title">
                                    <p>E-mail adres</p>
                                </div>
                                <div class="email-form">
                                    <input type="email" class="form-control" placeholder="E-mail adres" v-model="email">
                                </div>
                                <div class="password-title">
                                    <p>Wachtwoord</p>
                                </div>
                                <div class="password-form">
                                    <input type="password" class="form-control" placeholder="Wachtwoord"
                                        v-model="password">
                                </div>
                                <div class="repeat-password-title">
                                    <p>Herhaal wachtwoord</p>
                                </div>
                                <div class="repeat-password-form">
                                    <input type="password" class="form-control" placeholder="Herhaal wachtwoord"
                                        v-model="password2">
                                </div>
                                <div class="login-buttonpart">
                                    <div class="row">
                                        <div class="login-button col-5">
                                            <div class="shoppingcart-button">
                                                <button type="submit" class="shoppingcart-buttonbutton btn btn-success">
                                                    <span class="button-cart-text">Registreren</span>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div class="col-1"></div>
                        <div class="register-section col-5">
                            <div class="login-title">
                                <h2>Heeft u al een account?</h2>
                            </div>
                            <div class="login-subtitle">
                                <h4>Klik hieronder om in te loggen</h4>
                            </div>
                            <div class="register-button">
                                <div class="shopnubutton col-6">
                                    <button type="button" class="btn btn-dark" @click="$router.push('login')">Log
                                        in</button>
                                </div>
                            </div>
                            <hr class="register-hr">
                            <div class="time-register">
                                <span>
                                    <font-awesome-icon icon="tachometer-alt" :style="{ marginRight: '10px' }" />
                                </span>
                                <span class="register-icon-text">inloggen kost 1 minuutje tijd</span>
                            </div>
                            <hr class="register-hr">
                            <div class="time-register">
                                <span>
                                    <font-awesome-icon icon="inbox" :style="{ marginRight: '10px' }" />
                                </span>
                                <span class="register-icon-text">Alle bestellingen inzichtelijk bij elkaar</span>
                            </div>
                            <hr class="register-hr">
                            <div class="time-register">
                                <span>
                                    <font-awesome-icon icon="fast-forward" :style="{ marginRight: '10px' }" />
                                </span>
                                <span class="register-icon-text">Extra snel en moeiteloos bestellen</span>
                            </div>
                            <hr class="register-hr">
                            <div class="time-register">
                                <span>
                                    <font-awesome-icon icon="tag" :style="{ marginRight: '10px' }" />
                                </span>
                                <span class="register-icon-text">Altijd goed geprijste onderdelen</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.register .login-section,
.register-section {
    background-color: white;
    border: 1px solid #ddd;
    text-align: left;
    padding: 20px !important;
    margin-top: 78px !important;
    margin-bottom: 35px !important;
}

.register .login-subtitle h4 {
    font-size: 1vw !important;
    margin-bottom: 15px;
}

.register .email-title p,
.password-title p,
.repeat-password-title p {
    margin-bottom: 5px;
}

.register .email-title,
.password-title,
.repeat-password-title {
    margin-top: 15px;
}

.register .login-buttonpart {
    margin-top: 20px;
}

.register .forgot-password-link {
    text-align: center;
    margin-top: 20px !important;
    margin-bottom: auto;
    font-size: 0.9vw;
}

.register .forgot-password-link a {
    text-decoration: underline !important;
    color: #FF2400;
}

.register .register-hr {
    margin-top: 21px !important;
    margin-bottom: 21px !important;
}
</style>

<script>
import axios from 'axios'
import errorToast from '@/components/toast/error-toast.vue'
import succesToast from '@/components/toast/succes-toast.vue'

export default {
    name: 'Register',
    components: {
        errorToast,
        succesToast
    },
    data() {
        return {
            email: '',
            password: '',
            password2: '',
            errors: [],
            succes: false
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('het e-mail adres is niet ingevuld')
            }

            if (this.password === '') {
                this.errors.push('Het wachtwoord is niet ingevuld')
            }

            if (this.password2 === '') {
                this.errors.push('Vul het herhaal wachtwoord veld in')
            }

            if (this.password !== this.password2) {
                this.errors.push('De wachtwoorden komen niet overeen')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.email,
                    email: this.email,
                    password: this.password
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        // toast({
                        //     message: 'Account created, please log in!',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        console.log("account created!")
                        this.succes = true
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                if (error.response.data[property] == "This password is too common.") {
                                    this.errors.push("Dit wachtwoord komt te vaak voor, bedenk een unieker wachtwoord")
                                }
                                else if (error.response.data[property] == "The password is too similar to the username.") {
                                    this.errors.push("Dit wachtwoord lijkt te veel op uw email, bedenk een unieker wachtwoord")
                                }
                                else if (error.response.data[property] == "A user with that username already exists.") {
                                    this.errors.push("Er bestaat al een gebruiker met dit e-mail adres")
                                }
                                else if (error.response.data[property] == "Enter a valid email address.") {
                                    this.errors.push("Voer een geldig e-mail adres in")
                                }
                                else if (error.response.data[property] == "This password is too short. It must contain at least 8 characters." || [property] == "password") {
                                    this.errors.push("Het wachtwoord is te kort. Het wachtwoord moet minimaal 8 tekens bevatten.")
                                }
                                else {
                                    this.errors.push(`${[property]}: ${error.response.data[property]}`)
                                }
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })

            }

            console.log(this.errors)
        }
    }
}
</script>
