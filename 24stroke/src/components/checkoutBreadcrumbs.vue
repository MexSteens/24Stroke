<template>
    <div class="breadcrumb-checkout row">
        <div class="breadcrumb-item-checkout-first col-2" :class="{active: activepage === 'first' || activepage === 'second' || activepage === 'third' || activepage === 'fourth' || activepage === 'fifth' || activepage === 'sixth'}">
            <router-link to="/winkelwagen" class="routerlink"><span class="badge badge-dark">1</span>
            <span>Winkelwagen</span></router-link>
        </div>
        <div class="breadcrumb-item-checkout col-2" :class="{active: activepage === 'second' || activepage === 'third' ||  activepage === 'fourth' || activepage === 'fifth' || activepage === 'sixth'}">
            <div v-if="activepage == 'second' || activepage === 'third' ||  activepage === 'fourth'" @click="linkToAccount()"><span class="badge badge-dark">2</span>
            <span class="routerlink">Account</span></div>
            <div v-else><span class="badge badge-dark">2</span>
            <span>Account</span></div>
        </div>
        <div class="breadcrumb-item-checkout col-2" :class="{active: activepage === 'third' ||  activepage === 'fourth' || activepage === 'fifth' || activepage === 'sixth'}">
            <div v-if="activepage === 'third' ||  activepage === 'fourth'"><router-link to="/checkout-adres" class="routerlink"><span class="badge badge-dark">3</span>
            <span>Adres</span></router-link></div>
            <div v-else><span class="badge badge-dark">3</span>
            <span>Adres</span></div>
        </div>
        <div class="breadcrumb-item-checkout col-2" :class="{active:  activepage === 'fourth' || activepage === 'fifth' || activepage === 'sixth'}">
            <div v-if="activepage === 'fourth'"><router-link to="/checkout-betaling" class="routerlink"><span class="badge badge-dark">4</span>
            <span>Betaling</span></router-link></div>
            <div v-else><span class="badge badge-dark">4</span>
            <span>Betaling</span></div>
        </div>
        <div class="breadcrumb-item-checkout col-2" :class="{active: activepage === 'fifth' || activepage === 'sixth'}">
            <span class="badge badge-dark">5</span>
            <span>Verifiëren</span>
        </div>
        <div class="breadcrumb-item-checkout-last col-2" :class="{active: activepage === 'sixth'}">
            <span class="badge badge-light">6</span>
            <span>Klaar</span>
        </div>
    </div>
</template>

<style>
.breadcrumb-checkout {
    margin-top: 30px !important;
    margin-bottom: 60px !important;
}

.breadcrumb-item-checkout, .breadcrumb-item-checkout-first, .breadcrumb-item-checkout-last {
    background-color: #aaaaaa;
    color: white;
    border-right: 1px solid #F0F1F2;
    border-left: 1px solid #F0F1F2;
    padding: 15px !important;
    cursor: default;
}

.breadcrumb-item-checkout-first {
    border-left: none !important;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
}

.breadcrumb-item-checkout-last {
    border-right: none !important;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}

.breadcrumb-item-checkout-first.active, .breadcrumb-item-checkout-last.active, .breadcrumb-item-checkout.active {
    background-color: #393939 !important;
}

.badge {
    border-radius: 1rem !important;
    background-color: white !important;
    color: #393939 !important;
    margin-right: 10px !important;
    margin-top: 1px !important;
    vertical-align: top !important;
}

.breadcrumb-checkout .routerlink {
    color: white;
    cursor: pointer;
}  

.breadcrumb-checkout .routerlink:hover {
    transition: all 0.3s ease 0s;
    color: #ca1b00;
}  


</style>

<script>

export default {
    props: {
        activepage: String
    },
    data() {
        return{
            first: true,
            second: false,
            third: false,
            fourth: false,
            fifth: false,
            sixth: false,
            authenticated: false
        }
    },
    methods: {
        linkToAccount () {
            console.log(this.authenticated)
            if (this.authenticated == true) {
                this.$router.push('/checkout-auth')
            } else {
                this.$router.push('/checkout')
            }
        }
    },
    created: {
        Active() {
            if (activepage === "second"){
                this.second == true;
            }
        }
    },
    mounted () {
        this.authenticated = this.$store.state.isAuthenticated
    }
}
</script>