import { createStore } from 'vuex'

// cart implementation, authentication, etc.
// 
export default createStore({
  // state are vars that persist
  state: {
    downloadableItems: [],
    // web token used for authentication
    sf_auth_bearer: '',
    isAuthenticated: false,
    // set up cart state
    cart: {
        itemsInCart: [],
    },
    // show loading bar for cart
    isLoading: false,
    username: '',
    // free track/flp downloads
    isSingleDownload: false,
    freeDownload: '',
    freeDownloadId: '',
    downloadType: '',
  },
  getters: {
  },
  // synchronous functions; change states
  mutations: {

    // called on app load/page refresh in App.vue entry point
    initializeStore(state) {

      // check if user has a web token (logged in)
      if (localStorage.getItem('sf_auth_bearer')) {
        state.sf_auth_bearer = localStorage.getItem('sf_auth_bearer')
        state.isAuthenticated = true
      }
      else {
        state.sf_auth_bearer = ''
        state.isAuthenticated = false
      }

      // check if cart exists in local browser storage
      if (localStorage.getItem('cart')) {
          // get obj from storage if it exists
          state.cart = JSON.parse(localStorage.getItem('cart'))
      }
      // create empty cart in local browser storage
      else {
          localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },

    // set web token
    setToken(state, sf_auth_bearer) {
      state.sf_auth_bearer = sf_auth_bearer
      state.isAuthenticated = true
    },

    // remove token for logout
    removeToken(state) {
      state.sf_auth_bearer = ''
      state.isAuthenticated = false
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


      // make sure track is in cart
      if (isTrack) {
        // try to extract the object from the cart array
        const pendingTrackCartItemRemoval = state.cart.itemsInCart.filter(i => i.title === item.title)
        // if track exists
        if (pendingTrackCartItemRemoval.length) {

          // get track title used to find its location in the cart
          var track_title = pendingTrackCartItemRemoval[0].title
          // now using the track title, find the index of this track in the cart array
          var index = state.cart.itemsInCart.findIndex(x => x.title === track_title);

          // don't pop, but remove this specific track wherever it is located in the array
          state.cart.itemsInCart.splice(index, 1);
          // save cart storage data
          localStorage.setItem('cart', JSON.stringify(state.cart))
        }
        // else if it doesn't exist just return
        else {
          return
        }

      }
      // same with flps
      else if (is_flp) {
        // try to extract the object from the cart array
        const pendingFlpCartItemRemoval = state.cart.itemsInCart.filter(i => i.flp_name === item.flp_name)
        // if track exists
        if (pendingFlpCartItemRemoval.length) {

          // get track title used to find its location in the cart
          var flpName = pendingFlpCartItemRemoval[0].flp_name
          // now using the track title, find the index of this track in the cart array
          var index = state.cart.itemsInCart.findIndex(x => x.flp_name === flpName);

          // don't pop, but remove this specific track wherever it is located in the array
          state.cart.itemsInCart.splice(index, 1);
          // save cart storage data
          localStorage.setItem('cart', JSON.stringify(state.cart))
        }
        // else if it doesn't exist just return
        else {
          return
        }
      }
    },

    // remove all data from cart
    clearCart(state) {

      state.cart.itemsInCart = [];
      // update local storage
      localStorage.setItem('cart', JSON.stringify(state.cart))
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
