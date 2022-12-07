<template>
    <div class="template">
        <div class="row justify-content-center">
            <div class="col-10">
                <!-- Enter information here -->
                <div class="login">
                    <div class="row">
                        <div class="login-section col-6">
                            <div class="show-errors" v-if="errors.length">
                                <div class="toasts" v-for="(error, index) in errors" :key="index">
                                    <errorToast :message=errors[index] />
                                </div>
                            </div>
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
                                            <router-link to="/reset-wachtwoord" class="routerlink">Inloggegevens
                                                vergeten</router-link>
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
                                            <button type="button" class="btn btn-dark"
                                                @click="$router.push('register')">Registreer eenvoudig</button>
                                        </div>
                                    </div>
                                    <hr class="register-hr">
                                    <div class="time-register">
                                        <span>
                                            <font-awesome-icon icon="tachometer-alt" :style="{ marginRight: '10px' }" />
                                        </span>
                                        <span class="register-icon-text">registreren kost 2 minuten tijd</span>
                                    </div>
                                    <hr class="register-hr">
                                    <div class="time-register">
                                        <span>
                                            <font-awesome-icon icon="inbox" :style="{ marginRight: '10px' }" />
                                        </span>
                                        <span class="register-icon-text">Alle bestellingen inzichtelijk bij
                                            elkaar</span>
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
        </div>
    </div>
</template>

<style>
.login-section,
.register-section,
.guest-section {
    background-color: white;
    border: 1px solid #ddd;
    text-align: left;
    padding: 20px !important;
    margin-top: 78px !important;
    margin-bottom: 35px;
}

.login-subtitle h4 {
    font-size: 1vw !important;
    margin-bottom: 25px;
}

.email-title p,
.password-title p {
    margin-bottom: 5px;
}

.email-title,
.password-title {
    margin-top: 20px;
}

.login-buttonpart {
    margin-top: 20px;
}

.forgot-password-link {
    text-align: center;
    margin-top: 18px !important;
    margin-bottom: auto;
    font-size: 0.9vw;
}

.forgot-password-link a {
    text-decoration: underline !important;
    color: #FF2400;
}
</style>

<script>
import axios from 'axios'
import errorToast from "@/components/toast/error-toast.vue"

export default {
    name: 'login',
    components: {
        errorToast,
    },
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = "24stroke | Log in"
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('De gebruikersnaam is niet ingevuld')
            }

            if (this.password === '') {
                this.errors.push('Het wachtwoord is niet ingevuld')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
            

            axios.defaults.headers.common["authorization"] = ""

            localStorage.removeItem("token")

            axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/account'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            if (error.response.data[property] == "Unable to log in with provided credentials.") {
                                this.errors.push('Het e-mail adres en wachtwoord komen niet overeen')
                            }
                            else {
                                this.errors.push(`${error.response.data[property]}`)
                                console.log(this.errors)
                            }
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    }

}
</script>