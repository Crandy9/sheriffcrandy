import { createStore } from 'vuex'
// cart implementation
export default createStore({
  state: {
    cart: {
        items: [],
    },
    isAuthenticated: false,
    // used for login
    token: '',
    isLoading: false
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
