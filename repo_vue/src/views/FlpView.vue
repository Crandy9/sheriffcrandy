<template>

    <section class="flp-section">
      <!-- flps -->
      <section class="flp-title-section">
        <!-- title -->
        <div class="column is-12">
          <h2 class="flp-main-title is-size-3 has-text-centered has-text-white">
            My FLPs
          </h2>
          <p>
            <a style="color:chartreuse !important; text-decoration: none;" target="_blank" href="https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/fformats_save_flp.htm">What's an FLP?</a>
          </p>
        </div>
      </section>
      <section class="flp-items-section">
        <!-- unordered list of flps -->
        <ul class="flp-list">
          <!-- Vue for loop -->
          <div v-for="flp, index in flps" v-bind:key="flp.id" class="flp-list-div">
            <li class="flp-list-item" v-bind:id="flp.id">
                <div class="flp-title">
                    <!-- flp name -->
                    <span class="flp-title-inner">
                        {{ flp.flp_name }}
                    </span>
                </div>
                <div>
                  <!-- check if this item is already in the cart -->
                  <a class="flps-in-cart-button button is-small price-button has-text-weight-medium" 
                    v-if="checkIfFlpIsInCart(flp)" 
                    @click.stop="modalOpened = true; setFlpId(flp.id);" data-target="my-modal-id">
                    Added to Cart!
                  </a>
                  <!-- trigger modal with options to proceed to checkout, or add item to cart -->
                  <a class="button is-small is-black price-button has-text-weight-medium" 
                    v-else-if="flp.flp_is_free"
                    @click.stop="modalOpened = true; setFlpId(flp.id);" data-target="my-modal-id">
                    FREE
                  </a>
                  <a class="button is-small is-black price-button has-text-weight-medium" 
                    v-else 
                    @click.stop="modalOpened = true; setFlpId(flp.id);" data-target="my-modal-id">
                    ${{ flp.usd_price }}
                  </a>
                </div>
            </li>
          </div>
        </ul>
      </section>
    <!-- modal -->
    <Transition>
      <div v-if="modalOpened" id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
        <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <p class="modal-card-title">Buy now?</p>
              <button @click="modalOpened = false" class="delete" aria-label="close"></button>
            </header>
            <section class="modal-card-body">
              Do you want to purchase "{{ FlpName }}" now or add it to your cart and continue shopping?
            </section>
            <footer class="modal-card-foot">
              <!-- trigger stripe payment on this item only -->
              <button @click="modalOpened = false" class="my-modal-button-buy-now button">Buy Now</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click.stop="addFlpToCart(FlpID); modalOpened = false" class="my-modal-button-add-to-cart button">Add to Cart</button>
            </footer>
          </div>
      </div>
    </Transition>
    <!-- end modal -->
      <h2 class="flp-guide is-size-5 has-text-centered has-text-warning">
        Click the links on the right to 
        purchase/download the .zip file containing the 
        FL Studio Project, a text file with a list of required plugins, and any audio files used for the song. 
        After purchasing the project (or downloading if free), 
        a download of the .zip file will begin in your browser.
        Save the .zip file to your computer, extract/unzip the file's contents and that's it!
        Your .flp project is ready to be opened up in your FL Studio DAW to start experimenting!
        Enjoy.
      </h2>
      <p class="flp-guide has-text-danger">
        WARNING: 
        <p class="flp-guide has-text-white">
        An FL Studio "Fruity Edition" license 
        or greater is required in order to open and use 
        these .flp project files. The FL Studio free 
        trial version will not allow you to open or save 
        these .flp files. Purchase an FL Studio Edition 
        license <a target="blank"  class="flp-file-links" href="https://www.image-line.com/fl-studio/compare-editions/">here</a> 
        if you do not already have one.
        </p>
      </p>
      <div class="is-size-6" style="padding: 1rem;">
        <p style="padding:1.2rem;">
          <a class="flp-file-links" target="blank" href="https://www.homemusicmaker.com/open-flp-files-fl-studio-demo">
            - Opening FLP files in FL Studio
          </a>
        </p>
      </div>
    </section>
  </template>

<!-- modal animation fade-in/out -->
<style>
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.3s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }
</style>
  
  <script>
  // @ is an alias to /src
  
  // use axios to get api data from backend to frontend
  // axios was installed during initial vue setup. found in package.json
  // need to import axios in main.js as well
  import axios from 'axios'
  // for pop up notifying user about added item to cart
  import { toast } from 'bulma-toast'

  export default {
    name: 'Flps',
    data() {
      return {
        modalOpened: false,
        flps: [],
        FlpID: '',
        FlpName: '',
      }
    },
  
    components: {
    },
    // Vue lifecycle hook mounted() is called when this component is added to the DOM
    // so I guess on page load, getFlps() is called  
    mounted() {
      this.getFlps();
      document.addEventListener('click', this.closeModalOnWindowClick);
    },
    // functions defined here
    methods: {
      // called in modal popup on FREE or price button click
      setFlpId(flp) {
        // set flp name as well to show in modal popup
        const item = this.flps.find(item => item.id === flp)
        this.FlpName = item.flp_name;
        this.FlpID = flp;
      },

      closeModalOnWindowClick() {
        if (this.modalOpened === false) {

        }
        else if (this.modalOpened === true) {
          this.modalOpened = false;

        }
      },

      // make this method async and axios.get to await to make sure setIsLoading isn't set to false
      // until axios finished fetching api data
      async getFlps() {

        // loading bar while api data is getting fetched
        this.$store.commit('setIsLoading', true);

        // replace the API path with env var
        // .get requests API data from server via HTTP GET
        // .then will take the response data and populate the empty flps list above
        await axios.get(process.env.VUE_APP_FLPS_API__URL)
          .then(response => {
            this.flps = response.data
            document.title = 'Flps'
          })
          .catch(error => {
            console.log("ERROR BOYY: " + error)
            console.log(process.env.VUE_APP_FLPS_API__URL)
          })

        // stop loading bar after api data is fetched
        this.$store.commit('setIsLoading', false);
      },
          // add to cart
    addFlpToCart(flp) {
      // get specific flp added to cart
      const item = this.flps.find(item => item.id === flp)

      // calls store/index.js addToCart function
      this.$store.commit('addToCart', item)
      // show toast msg to user https://www.npmjs.com/package/bulma-toast
      // toast fadein/out animation requires animate.css. See README
      toast({
        message: ' \"' + item.flp_name + '\" FLP added to cart!',
        type: 'is-info',
        dismissible: true,
        pauseOnHover: true,
        duration: 3000,
        position: 'bottom-right',
        animate: { in: 'fadeIn', out: 'fadeOut' },
      })
    },
    // check if an item clicked is already in the cart
    checkIfFlpIsInCart(flp) {
      const pendingFlpCartItem = 
      this.
      $store.
      state.
      cart.
      itemsInCart.
      filter(i => i.flp_name === flp.flp_name)
        if (pendingFlpCartItem.length) {
          return true;
        }
    }
    }
  }
  </script>