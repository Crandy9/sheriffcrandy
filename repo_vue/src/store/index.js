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

      // check if this item is already in the cart
      // will be either '[]' if not in cart.items, or '[proxy]'
      const pendingCartItem = state.cart.itemsInCart.filter(i => i.id === item.id)
      // if pendingCartItem already exists
      // TODO: what to do if attempted duplicate cart item
      if (pendingCartItem.length) {

        if (isTrack) {
          console.log("Track " + item.id + ' already added to cart')
        }
        else if (is_flp) {
          console.log("Flp " + item.id + ' already added to cart')
        }
      }
      // else if it doesn't exist push this track/flp to the cart
       else {
          if (isTrack) {
          console.log("Adding track " + item.id + ' to cart')
          state.cart.itemsInCart.push(item)

          }
          else if (is_flp) {
            console.log("Adding flp " + item.id + ' to cart')
            state.cart.itemsInCart.push(item)

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
