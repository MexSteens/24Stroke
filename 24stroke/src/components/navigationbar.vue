<template>
    <div class="navigationbar">
        <div class="row colorrows">
            <div class="grayrow col-12">
                <div class="row grayrowheight">
                    <div class="logo col-3">
                        <img class="logo-twentyfourstroke" src="http://localhost:8080/img/logo/24stroke-logo.png" alt="logo">
                    </div>
                    <div class="searchbar form-group col-3">
                        <form method="get" action="/search"><input type="text" class="form-control"
                                placeholder="Waar ben je naar opzoek?" name="query"></form>
                    </div>
                    <div class="accountnav col-2">
                        <router-link to="/account">
                            <div class="row">
                                <div class="helmetimage col-3">
                                    <img src="http://localhost:8080/img/icon/full-motorcycle-helmet.svg" alt="motorcyclehelmet" width="40px"
                                        height="40px">
                                </div>
                                <div class="accounttext col-9">
                                    <h4>Mijn account</h4>
                                    <h1>Welkom {name}</h1>
                                </div>
                            </div>
                        </router-link>
                    </div>
                    <div class="garagenav col-2">
                        <router-link to="/garage">
                            <div class="row">
                                <div class="motorcycleimage col-3">
                                    <font-awesome-icon icon="motorcycle"
                                        :style="{ color: 'white', width: '45px', height: '45px', marginTop: '-3px' }" />
                                </div>
                                <div class="accounttext col-9">
                                    <h4>geselecteerde scooter</h4>
                                    <h1>{geselecteerde scooter}</h1>
                                </div>
                            </div>
                        </router-link>
                    </div>
                    <div class="cartnav col-1">
                        <router-link to="/winkelwagen">
                            <div class="row">
                                <div class="shoppingcartimage col-3">
                                    <font-awesome-icon icon="shopping-cart"
                                        :style="{ color: 'white', width: '35px', height: '35px', marginTop: '-3px'}" />
                                </div>
                                <div class="accounttext col-9">
                                    <h4>winkelwagentje</h4>
                                    <h1>{{ numberOfItems }} {{ itemMessage }}</h1>
                                </div>
                            </div>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="blackrow col-12" id="hidenav">
                <div class="row">
                    <div class="motordelen col">
                        <router-link to="/motordelen">
                            <h1>Motordelen</h1>
                        </router-link>
                    </div>
                    <div class="framedelen col">
                        <router-link to="/framedelen">
                            <h1>Framedelen</h1>
                        </router-link>
                    </div>
                    <div class="mechanisch col">
                        <router-link to="/mechanisch">
                            <h1>Mechanisch</h1>
                        </router-link>
                    </div>
                    <div class="universeel col">
                        <router-link to="/universeel">
                            <h1>Universeel</h1>
                        </router-link>
                    </div>
                    <div class="outlet col">
                        <router-link to="/outlet">
                            <h1>Outlet</h1>
                        </router-link>
                    </div>
                    <div class="kits col">
                        <router-link to="/kits">
                            <h1>Kits</h1>
                        </router-link>
                    </div>
                    <div class="non-scooter col">
                        <router-link to="/non-scooter">
                            <h1>Non-scooter</h1>
                        </router-link>
                    </div>
                </div>
            </div>
            <div class="redrow col-12"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'navbar',
    data() {
        return {
            cart: {
                items: []
            },
            itemMessage: '',
            below: false,
            margintop: 0,
            goingup: false 
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        window.addEventListener("scroll", this.scrollFunction)
    },
    methods: {
        scrollFunction(e) {
            if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
                if (this.below == false) {
                    this.below = true;
                    this.goingup = true;
                    var interval = setInterval(() => {
                        if (this.margintop == -50 || this.marginTop < -50) {
                            clearInterval(interval)
                            this.margintop = -50;
                        }
                        this.margintop -= 1
                        document.getElementById("hidenav").style.marginTop = this.margintop + "px"
                    }, 20);
                    setTimeout(() => {
                        this.goingup = false;
                    }, 1000)
                }
            } else {
                if (this.below == true) {
                    if (this.goingup == true) {
                        setTimeout(this.scrollFunction, 200)
                    } else {
                        this.below = false;
                        var interval = setInterval(() => {
                            if (this.margintop == -1 || this.margintop > 0) {
                                clearInterval(interval)
                                this.margintop = -1
                            }
                            this.margintop += 1
                            document.getElementById("hidenav").style.marginTop = this.margintop + "px"
                        }, 20);
                    }
                }
            }
        }
    },
    computed: {
        numberOfItems() {
            let numberOfItems = 0

            for (let i = 0; i < this.cart.items.length; i++) {
                numberOfItems += this.cart.items[i].quantity
            }
            if (numberOfItems == 1){
                this.itemMessage = "product"
            }
            else {
                this.itemMessage = "producten"
            }

            return numberOfItems
        }
    }
}
</script>

<style>
.logo-twentyfourstroke {
    display: block;
    max-width: 140px;
    max-height: 45px;
    width: auto;
    height: auto;
    margin-left: auto;
    margin-right: auto;
}

.app-navigation {
    padding-bottom: 110px;
    background-color: #F0F1F2;
    /* z-index: -4; */
}

.navigationbar {
    overflow: hidden;
    transition: 0.4s;
    position: fixed;
    top: 0;
    z-index: 99;
    width: 100%;
}

.grayrow {
    background-color: #393939;
    height: 60px;
    z-index: 1;
}

.grayrowheight {
    height: 60px;
}

.logo {
    margin-top: 8px !important;
}

.searchbar {
    border-radius: 3px;
    margin-top: 12px !important;
    margin-bottom: 18px;
    justify-content: center;
    margin-right: 4%;
}

.accountnav {
    /* background-color: #676767; */
    padding-top: 8px !important;
    padding-bottom: 8px;
    /* border-left: 12px solid #393939;
    border-right: 12px solid #393939; */
}

.accounttext {
    text-align: left;
}

.accounttext h4 {
    font-size: 0.8vw;
    margin-bottom: 0px;
    color: #98A1A8;
}

.accounttext h1 {
    font-size: 0.9vw;
    margin-bottom: 0px;
    color: #fff;
}

.garagenav {
    /* background-color: #676767; */
    padding-top: 8px !important;
}

.cartnav {
    /* background-color: #676767; */
    padding-top: 8px !important;
    /* border-left: 12px solid #393939;
    border-right: 12px solid #393939; */
    width: 12.333333% !important;
}

.shoppingcartimage {
    padding-top: 5px;
}

.blackrow {
    position: relative;
    background-color: #1D1D1D;
    padding-right: 2% !important;
    padding-left: 2% !important;
}

.blackrow h1 {
    color: white;
    font-size: 1vw;
    margin-top: 10px;
    margin-bottom: 10px;
}

.motordelen,
.framedelen,
.mechanisch,
.universeel,
.outlet,
.kits {
    border-right: 5px solid #393939;
}

.redrow {
    background-color: #FF2400;
    height: 10px;
}
</style>
