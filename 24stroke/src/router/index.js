import store from '../store'

import test from '../views/test.vue'

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Motordelen from '../views/navigation/Motordelen.vue'
import Cilinders from '../views/productpages/cilinders-test.vue'
import Cilinder from '../views/productpages/Cilinder.vue'
import Cart from '../views/cart-login-account/cart.vue'
import Login from '../views/cart-login-account/login.vue'
import Register from '../views/cart-login-account/register.vue'
import ResetPassword from '../views/cart-login-account/resetpassword.vue'
import ResetPasswordConfirm from '../views/cart-login-account/resetpasswordconfirm.vue'
import Search from '../views/cart-login-account/search.vue'
import Account from '../views/cart-login-account/account.vue'
import Checkout from '../views/checkout/checkout.vue'
import CheckoutAdres from '../views/checkout/checkoutaddress.vue'
import CheckoutBetaling from '../views/checkout/checkoutpayment.vue'
import CheckoutVerifieren from '../views/checkout/checkoutverify.vue'
import CheckoutAccountLoggedIn from '../views/checkout/checkoutauth.vue'
import CheckoutConfirm from '../views/checkout/checkoutconfirm.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/test',
    name: 'test',
    component: test
  },
  {
    path: '/motordelen',
    name: 'Motordelen',
    component: Motordelen
  },
  {
    path: '/winkelwagen',
    name: 'cart',
    component: Cart
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: Checkout
  },
  {
    path: '/checkout-auth',
    name: 'checkoutauth',
    component: CheckoutAccountLoggedIn
  },
  {
    path: '/checkout-adres',
    name: 'checkoutadres',
    component: CheckoutAdres
  },
  {
    path: '/checkout-betaling',
    name: 'checkoutbetaling',
    component: CheckoutBetaling
  },
  {
    path: '/checkout-verifieren',
    name: 'checkoutverifieren',
    component: CheckoutVerifieren
  },
  {
    path: '/checkout-bevestiging',
    name: 'checkoutconfirm',
    component: CheckoutConfirm
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/account',
    name: 'account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/registreer',
    name: 'register',
    component: Register
  },
  {
    path: '/reset-wachtwoord',
    name: 'reset-wachtwoord',
    component: ResetPassword
  },
  {
    path: '/reset-wachtwoord-bevestig/:uid/:token',
    name: 'reset-wachtwoord-bevestig',
    component: ResetPasswordConfirm
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/:category_slug',
    name: 'Cilinders',
    component: Cilinders
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Cilinder',
    component: Cilinder
  }, 
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name === "account" && store.getters.isAuthenticated === false) {
    next({ name: 'login', query: { to: to.path } });
  } else {
    next();
  }
})

export default router
