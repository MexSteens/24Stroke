<template>
    <div class="my-account">
        <div class="row justify-content-center">
            <div class="col-10">
                <div class="my-account-padding row">
                    <div class="col-4">
                        <SideBar />
                    </div>
                    <div class="my-account-overview-information col-8">
                        <div class="my-account-overview-title">
                            <h1>Account overzicht</h1>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <div class="row justify-content-start">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Mijn gegevens</h3>
                                        <button type="button" class="btn btn-dark">Log in</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="row justify-content-end">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Mijn bestellingen</h3>
                                        <button type="button" class="btn btn-dark">Log in</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="row justify-content-start">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Mijn garage</h3>
                                        <button type="button" class="btn btn-dark">Log in</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="row justify-content-end">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Mijn verlanglijst</h3>
                                        <button type="button" class="btn btn-dark">Log in</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="row justify-content-start">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Wachtwoord wijzigen</h3>
                                        <button type="button" class="btn btn-dark">Log in</button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="row justify-content-end">
                                    <div class="my-account-overview-box col-11">
                                        <h3>Uitloggen</h3>
                                        <button @click="logout()" type="button" class="btn btn-dark">Log uit</button>
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

.my-account-padding {
    margin-top: 50px !important;
}

.my-account-overview-box {
    border: 1px solid #ddd;
    padding: 20px !important;
    margin-top: 20px !important;
}

.my-account-overview-information {
    background-color: white;
    border: 1px solid #ddd;
    padding: 20px !important;
    text-align: left;
    padding-right: 50px !important;
    padding-left: 70px !important;
}


.my-account-overview-box h3 {
    font-size: 1.2vw;
}
</style>

<script>
import axios from 'axios'
import SideBar from '@/components/sidebarAccount.vue'

export default {
    name: 'Account',
    components: {
        SideBar
    },
    data() {
        return {
            orders: [],
        }
    },
    mounted() {
        document.title = '24stroke | account'
        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
        // async getMyOrders() {
        //     this.$store.commit('setIsLoading', true)
        //     await axios
        //         .get('/api/v1/orders/')
        //         .then(response => {
        //             this.orders = response.data
        //         })
        //         .catch(error => {
        //             console.log(error)
        //         })
        //     this.$store.commit('setIsLoading', false)
        // }
    }
}
</script>