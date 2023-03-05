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
    },
    isAuthenticated: false,
    token: '',
    isLoading: false,
    wishlist: {
      items: []
    },
    recentlyViewed: {
      items: []
    },
    filters: [],
    technicalDetails: [],
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
        state.user = JSON.parse(localStorage.getItem('users'))
      }

      if (localStorage.getItem('filters')) {
        state.filters = JSON.parse(localStorage.getItem('filters'))
      }

      if (localStorage.getItem('technicalDetails')) {
        state.technicalDetails = JSON.parse(localStorage.getItem('technicalDetails'))
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
    addFilter(state, filter) {
      state.filters.push(filter)
      localStorage.setItem('filters', JSON.stringify(state.filters))
    },
    addFilterValue(state, oldfilter) {
      const index = state.filters.indexOf(oldfilter[0])
      state.filters[index].filtering.push(oldfilter[1])
      localStorage.setItem('filters', JSON.stringify(state.filters))
    },
    removeFilter(state, filter) {
      const index = state.filters.indexOf(filter)
      state.filters.splice(index, 1)
      localStorage.setItem('filters', JSON.stringify(state.filters))
    },
    removeFilterValue(state, oldfilter) {
      const index = state.filters.indexOf(oldfilter[0])
      const indexnumber = state.filters[index].filtering.indexOf(oldfilter[1].filtering[0])
      state.filters[index].filtering.splice(indexnumber, 1)
      localStorage.setItem('filters', JSON.stringify(state.filters))
    },
    addTechnicalDetails(state, td) {
      state.technicalDetails = td
      localStorage.setItem('technicalDetails', JSON.stringify(state.technicalDetails))
    },
    // removeFilter(state, filter) {
    //   const index = state.filters.indexOf(filter)
    //   state.filters.splice(index, 1)
    //   localStorage.setItem('filters', JSON.stringify(state.filters))
    // },
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
