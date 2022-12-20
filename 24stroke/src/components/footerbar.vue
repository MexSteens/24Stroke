<template>
    <footer class="app-footer">
        <div class="footer mt-auto">
            <div class="blackrowfooter">
                <div class="row justify-content-center">
                    <div class="col-10">
                        <div class="row justify-content-between">
                            <div class="klantenservice col-2">
                                <h1>Klantenservice</h1>
                                <p>
                                    <router-link :to="'faq'" class="routerlink">FAQ</router-link>
                                </p>
                                <p>
                                    <router-link :to="'contact'" class="routerlink">Contact</router-link>
                                </p>
                                <p>
                                    <router-link :to="'levering'" class="routerlink">Levering</router-link>
                                </p>
                                <p>
                                    <router-link :to="'retourneren'" class="routerlink">Retourneren</router-link>
                                </p>
                                <p>
                                    <router-link :to="'account'" class="routerlink">Mijn account</router-link>
                                </p>
                            </div>
                            <div class="navigatie col-2">
                                <h1>Navigatie</h1>
                                <p>
                                    <router-link :to="'motordelen'" class="routerlink">Motordelen</router-link>
                                </p>
                                <p>
                                    <router-link :to="'framedelen'" class="routerlink">Framedelen</router-link>
                                </p>
                                <p>
                                    <router-link :to="'mechanisch'" class="routerlink">Mechanisch</router-link>
                                </p>
                                <p>
                                    <router-link :to="'universeel'" class="routerlink">Universeel</router-link>
                                </p>
                                <p>
                                    <router-link :to="'outlet'" class="routerlink">Outlet</router-link>
                                </p>
                                <p>
                                    <router-link :to="'kits'" class="routerlink">Kits</router-link>
                                </p>
                                <p>
                                    <router-link :to="'non-scooter'" class="routerlink">Non-scooter</router-link>
                                </p>
                            </div>
                            <div class="volgons-taal col-2">
                                <div class="row">
                                    <div class="volgons">
                                        <h1>Volg ons</h1>
                                        <font-awesome-icon :icon="['fab', 'instagram']"
                                            :style="{ color: 'white', width: '35px', height: '35px', marginRight: '10px' }" />
                                        <font-awesome-icon :icon="['fab', 'facebook']"
                                            :style="{ color: 'white', width: '35px', height: '35px', marginRight: '10px' }" />
                                        <font-awesome-icon :icon="['fab', 'youtube']"
                                            :style="{ color: 'white', width: '35px', height: '35px' }" />
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="taal">
                                        <h1>Taal</h1>
                                        <img src="http://localhost:8080/img/icon/dutch-flag.png" alt="dutch-flag" width="35px" height="35px"
                                            style="margin-left: 2px; margin-right: 10px;">
                                        <img src="http://localhost:8080/img/icon/united-kingdom.png" alt="united-kingdom" width="35px"
                                            height="35px">
                                    </div>
                                </div>
                            </div>
                            <div class="nieuwsbrief col-4">
                                <h1>Nieuwsbief</h1>
                                <p>Meld je aan voor de nieuwsbrief en mis geen enkele deal!</p>
                                <form class="input-group newsletter-form" @submit.prevent="submitForm">
                                    <input type="email" class="news-letter-input form-control" name="newsletter"
                                        placeholder="vul hier je e-mail adres in" v-model="email">
                                    <span class="input-group-btn">
                                        <button class="news-letter-button btn" type="submit">Meld aan</button>
                                    </span>
                                </form>
                                <div v-if="succesNewsletter">
                                    <SuccesToast message="email is aangemeld!" />
                                </div>
                                <div class="show-errors" v-if="errors.length">
                                <div class="toasts" v-for="(error, index) in errors" :key="index">
                                    <ErrorToast :message=errors[index] />
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div class="redrowfooter">
                        <p>© 2021 24stroke | Algemene voorwaarden | Cookies | Privacy</p>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
import axios from 'axios'
import SuccesToast from '@/components/toast/succes-toast.vue'
import ErrorToast from '@/components/toast/error-toast.vue'

export default {
    name: 'Footer',
    components:{SuccesToast, ErrorToast},
    data() {
        return {
            email: '',
            succesNewsletter: false,
            errors: [],
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === '') {
                this.errors.push('het e-mail adres is niet ingevuld')
            }
            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                }

                axios
                    .post("/api/v1/subscribe/", formData)
                    .then(response => {
                        // toast({
                        //     message: 'Account created, please log in!',
                        //     type: 'is-success',
                        //     dismissible: true,
                        //     pauseOnHover: true,
                        //     duration: 2000,
                        //     position: 'bottom-right',
                        // })
                        console.log("email is aangemeld!")
                        this.succesNewsletter = true
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${[property]}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }

}
</script>

<style>
.news-letter-input:focus {
    outline: 0px !important;
    box-shadow: none !important;
    border: 1px solid #ced4da !important;
}

.news-letter-button:focus {
    box-shadow: none !important;
}

.app-footer {
    bottom: 0;
    position: absolute;
    width: 100%;
    height: auto;
}

.footer {
    text-align: left;
}

.footer h1 {
    color: #FF2400;
    font-size: 25px;
    font-weight: 900;
}

.footer p {
    font-size: 15px;
    color: white;
    margin: 0;
}

.footer a {
    font-size: 15px;
    color: white;
    margin: 0;
    text-decoration: none;
}

.blackrowfooter {
    background-color: #1D1D1D;
    padding-top: 30px;
    margin-top: 60px;
}

.redrowfooter {
    background-color: #FF2400;
    padding: 3px;
    text-align: center !important;
    margin-top: 20px !important;
}

.redrowfooter p {
    font-size: 13px;
}

.volgons {
    margin-bottom: 15px;
}

.newsletter-form {
    margin-bottom: 15px;
}

.news-letter-input {
    height: 40px !important;
    padding: 0 !important;
    padding-left: 5px !important;
    border-radius: 5px 0px 0px 5px !important;
}

.news-letter-button {
    background-color: #FF2400 !important;
    height: 40px !important;
    border-radius: 0px 5px 5px 0px !important;
}
</style>