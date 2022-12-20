import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  getters: {
    isAuthenticated() {
      return !!localStorage.getItem('token')
    }
  },
  state: {
    cart: {
      items: [],
    },
    user: {
      emailAddress: '',
      firstName: '',
      lastName: '',
      postalCode: '',
      city: '',
      street: '',
      houseNumber: '',
      phoneNumber: '',
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    wishlist: {
      items: []
    },
    recentlyViewed: {
      items: []
    }
  },

  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('wishlist')) {
        state.wishlist = JSON.parse(localStorage.getItem('wishlist'))
      } else {
        localStorage.setItem('wishlist', JSON.stringify(state.wishlist))
      }

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }

      if (localStorage.getItem('users')) {
        state.user = localStorage.getItem('users')
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }

      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    addToRecentlyViewed(state, item) {
      state.recentlyViewed.items.push(item)
      localStorage.setItem('recentlyViewed', JSON.stringify(state.recentlyViewed))
    },
    removeFromRecentlyViewed(state) {
      state.recentlyViewed.shift()
      localStorage.setItem('recentlyViewed', JSON.stringify(state.recentlyViewed))
    },
    addToWishlist(state, item) {
      state.wishlist.items.push(item)
      localStorage.setItem('wishlist', JSON.stringify(state.wishlist))
    },
    removeFromWishlist(state, item) {
      state.wishlist = item
      localStorage.setItem('wishlist', JSON.stringify(state.wishlist))
    },
    userInfo(state, user) {
      state.user = user
      localStorage.setItem('users', JSON.stringify(state.user))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
