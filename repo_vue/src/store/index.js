import { createStore } from 'vuex'
// cart implementation, authentication, etc.
// 
export default createStore({
  // state are vars
  state: {
    cart: {
        itemsInCart: [],
    },
    isAuthenticated: false,
    // used for login
    token: '',
    // show loading bar for cart
    isLoading: false
  },
  getters: {
  },
  // synchronous vars; add functionality
  mutations: {

    // called
    initializeStore(state) {
      // check if item exists in local browser storage
      if (localStorage.getItem('cart')) {
          // get obj from storage if it exists
          state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      // create empty cart in local browser storage
      else {
          localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    // add items to cart
    addToCart(state, item) {

      // check if this is an flp or track being added to cart
      var isTrack = false
      var is_flp = false

      if ('title' in item) {
        isTrack = true;
        is_flp = false;      
      }

      else if ('flp_name' in item) {
        isTrack = false;
        is_flp = true;   
      }


      // check if this track is already in the cart
      // will be either '[]' if not in cart.items, or '[proxy]'
      if (isTrack) {
        const pendingTrackCartItem = state.cart.itemsInCart.filter(i => i.title === item.title)
        // if pendingCartItem already exists
        // TODO: what to do if attempted duplicate cart item
        if (pendingTrackCartItem.length) {
            console.log("Track " + item.title + ' already added to cart')
        }
        // else if it doesn't exist push this track/flp to the cart
        else {
              console.log("Adding track " + item.title + ' to cart')
              state.cart.itemsInCart.push(item)
              console.log("Total items in cart: " + state.cart.itemsInCart.length)
        }

      }
      // check if this flp is already in the cart
      else if (is_flp) {
        const pendingFlpCartItem = state.cart.itemsInCart.filter(i => i.flp_name === item.flp_name)
        // TODO: what to do if attempted duplicate cart item
        if (pendingFlpCartItem.length) {
            console.log("Flp " + item.flp_name + ' already added to cart')
          }
        // else if it doesn't exist push this track/flp to the cart
        else {
              console.log("Adding flp " + item.flp_name + ' to cart')
              state.cart.itemsInCart.push(item)
              console.log("Total items in cart: " + state.cart.itemsInCart.length)
        }
      }


      // save items to cart in browser local storage
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  // asynchronous vars
  actions: {
  },
  modules: {
  }
})
