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
    isLoading: false,
    // trackItemsInCart: [],
    // flpItemsInCart: [],
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
        // if track already exists
        // TODO: what to do if attempted duplicate cart item
        if (pendingTrackCartItem.length) {
            console.log("Track " + item.title + ' already added to cart')
        }
        // else if it doesn't exist push this track to the cart
        else {
              // push to cart
              state.cart.itemsInCart.push(item)
              // push to track array
              // state.trackItemsInCart.push(item)
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
              // push flp to cart
              state.cart.itemsInCart.push(item)
              // push flp to flp array
              // state.flpItemsInCart.push(item)
        }
      }

      // save cart storage data
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    // remove items from cart
    removeFromCart(state, item) {

    },

    // remove all data from cart
    clearCart() {
      console.log('clearing cart')
      localStorage.clear();
    },

    // set a loading bar 
    setIsLoading(state, status) {
      state.isLoading = status;
    }
  },
  // asynchronous vars
  actions: {
  },
  modules: {
  }
})
