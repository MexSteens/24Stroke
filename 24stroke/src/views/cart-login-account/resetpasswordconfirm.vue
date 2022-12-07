<template>
    <div class="template">
        <div class="row justify-content-center">
            <div class="col-10">
                <!-- Enter information here -->
                <div class="register">
                    <div class="row">
                        <div class="col-3"></div>
                        <div class="login-section col-6">
                            <form @submit.prevent="submitForm">
                                <div class="login-title">
                                    <h2>Wachtwoord resetten</h2>
                                </div>
                                <div class="login-subtitle">
                                    <h4>Van bestaand account</h4>
                                </div>
                                <div class="password-title">
                                    <p>Niew wachtwoord</p>
                                </div>
                                <div class="password-form">
                                    <input type="password" class="form-control"
                                        v-model="password">
                                </div>
                                <div class="repeat-password-title">
                                    <p>Herhaal nieuw wachtwoord</p>
                                </div>
                                <div class="repeat-password-form">
                                    <input type="password" class="form-control"
                                        v-model="password2">
                                </div>
                                <div class="login-buttonpart">
                                    <div class="row">
                                        <div class="login-button col-5">
                                            <div class="shoppingcart-button">
                                                <button type="submit" class="shoppingcart-buttonbutton btn btn-success">
                                                    <span class="button-cart-text">reset wachtwoord</span>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div class="col-3"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Resetpasswordconfirm',
    data() {
        return {
            password: String,
            password2: String,
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.password === '') {
                this.errors.push('Het wachtwoord is niet ingevuld')
            }

            if (this.password !== this.password2) {
                this.errors.push('De wachtwoorden komen niet overeen')
            }

            if (!this.errors.length) {
                const formData = {
                    uid: this.$route.params.uid,
                    token: this.$route.params.token,
                    new_password: this.password
                }

                axios
                    .post("/api/v1/users/reset_password_confirm/", formData)
                    .then(response => {
                        // toast({
                        //     message: 'Account created, please log in!',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        console.log("password reset!")
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
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
