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
                  <!-- check if this item is already in the cart; remove it if clicked -->
                  <a class="flps-in-cart-button button is-small price-button has-text-weight-medium" 
                    v-if="checkIfFlpIsInCart(flp)" 
                    @click.stop="modalOpened = false; removeFromCart(flp.id)" data-target="my-modal-id">
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
                <p v-if="isFree" class="modal-card-title">Download now?</p>
                <p v-else class="modal-card-title">Buy now?</p>
                <button @click="modalOpened = false" class="delete" aria-label="close"></button>
              </header>
              <section v-if="isFree" class="modal-card-body">
                Do you want to download "{{ FlpName }}" now or add it to your cart and continue shopping?
              </section>
              <section v-else class="modal-card-body">
                Do you want to purchase "{{ FlpName }}" now or add it to your cart and continue shopping?
              </section>
              <footer class="modal-card-foot">
                <!-- pass in the flpname of the free flp to be downloaded -->
                <button v-if="isFree" @click="modalOpened = false; show = false; buyNowClicked = false; downloadFreeNow(FlpName, FlpID);" class="my-modal-button-buy-now button">Download Now</button>
                <!-- trigger stripe payment on this item only -->
                <button v-else @click="modalOpened = false; show = true; buyNowClicked = true; buyNow(FlpName, FlpID); scrollToBottom();" class="my-modal-button-buy-now button">Buy Now</button>
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
    <!-- FOR BUY NOW -->
    <!-- stripe payment form -->
    <transition>
      <div style="z-index: 9999;" class="my-checkout-div"
        :style="styleObject()" v-bind:class="{'is-active': buyNowClicked}" ref="paymentFormTop">
          <!-- <div class="modal-background"></div> -->
            <div class="card">
              <header class="card-head">
                <p class="card-title">Checkout</p>
                <button class="delete close-button" @click="show = false; clearFields(); buyNowClicked = false;" aria-label="close"></button>
              </header>
              <section class="card-body">
                <div class="page-checkout">
                  <div class="columns is-multiline">
                      <div class="column is-12 box">
                        <h2 style= "text-align: center;" class="subtitle has-text-black has-text-center is-underlined">Payment Details</h2>
                        <h2 class="subtitle has-text-black">Billing Address</h2>
                        <!-- <p class="has-text-danger mb-4">* All fields are required</p> -->
                        <div class="columns is-multiline">
                          <div class="column is-6">
                            <!-- name errors-->
                            <div v-if="errors.nameErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.nameErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="has-text-black">Name</label>
                              <div class="control">
                                  <input type="text" class="input" placeholder="ex) John Smith" v-model="name">
                              </div>
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="has-text-black">Email</label>
                              <div class="control">
                                  <input type="email" class="input" placeholder="123@my-email.com" v-model="email">
                              </div>
                            </div>
                            <!-- phone errors-->
                            <div v-if="errors.phoneErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.phoneErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="has-text-black">Phone Number</label>
                              <div class="control">
                                  <input type="text" class="input" placeholder="ex) xxx-xxx-xxxx" v-model="phone">
                              </div>
                            </div>
                            <!-- address1 errors-->
                            <div v-if="errors.address1Errors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.address1Errors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="has-text-black">Street 1</label>
                              <div class="control">
                                  <input type="text" class="input" placeholder="ex) 123 My Street" v-model="address1">
                              </div>
                            </div>
                              <!-- address2 errors-->
                              <div v-if="errors.address2Errors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.address2Errors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="has-text-black">Street 2 (if applicable)</label>
                              <div class="control">
                                  <input type="text" class="input" placeholder="ex) apt. #101"  v-model="address2">
                              </div>
                            </div>
                          </div>
                          <div class="column is-6">
                              <!-- statepref errors-->
                              <div v-if="errors.statePrefErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.statePrefErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <div class="field">
                                <label class="has-text-black">State</label>
                                <div class="control">
                                    <input type="text" class="input" placeholder="Chicago" v-model="statePref">
                                </div>
                              </div>
                              <!-- country errors-->
                              <div v-if="errors.countryErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.countryErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <div class="field">
                                <label class="has-text-black">Country</label>
                                <div class="control">
                                    <input type="text" class="input" placeholder="ex) United States, Japan, etc."  v-model="country">
                                </div>
                              </div>
                              <!-- post code errors-->
                              <div v-if="errors.zipcodeErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.zipcodeErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <div class="field">
                                <label class="has-text-black">Postal Code</label>
                                <div class="control">
                                    <input type="text" class="input" placeholder="ex) 12345 or 12312-1234" v-model="zipcode">
                                </div>
                              </div>
                          </div>
                        </div>
                      </div>
                      <hr>
                      <!-- general errors -->
                      <div v-if="errors.generalErrors.length">
                          <p class="my-errors" style="text-align: center; color:red; padding-bottom: 1rem; padding-inline: 2.2rem;" v-for="error in errors.generalErrors" v-bind:key="error">
                          <span style="color:red !important">*</span> {{ error }}
                          </p>                        
                      </div>
                      <div class="mb-5 has-text-black">
                        <h2 class="subtitle has-text-black">Card Information</h2>
                      </div>
                  </div>
                </div>
                <div class="stripe-card-div">
                  <div id="card-element" class="mb-5 control"></div>
                </div>
              </section>
              <footer class="card-foot">
                <p class="my-subtotal has-text-black">
                  <span>Total:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ usdPrice }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>Tax:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTaxes }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>Subtotal:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdSubtotal }}</span>
                </p>
                <button @click="submitForm();" class="my-button-buy-now button">Pay ${{ usdPrice }}</button>
                <!-- if adding to cart, add the item to cart and close modal -->
                <button @click="show = false; clearFields(); buyNowClicked = false;" class="my-button-cancel button">Cancel</button>
              </footer>
            </div>
      </div>
    </transition>
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
        buyNowClicked: false,
        buyNowItemName: '',
        buyNowItemId: '',
        show: false,
        usdPrice: '',
        jpyPrice: '',
        usdTaxRate: .0,
        jpyTaxRate: 0.1,
        usdTax: '',
        jpyTax: '',
        usdSubTotal: '',
        jpySubtotal:'',
        modalOpened: false,
        flps: [],
        FlpID: '',
        FlpName: '',
        isFree: '',
        // stripe stuff
        stripe: {},
        card: {},
        name: '',
        email: '',
        phone: '',
        address1: '',
        address2:'',
        statePref: '',
        country: '',
        zipcode: '',
        errors: {
                generalErrors: [],
                nameErrors: [],
                emailErrors: [],
                phoneErrors: [],
                address1Errors: [],
                address2Errors: [],
                statePrefErrors: [],
                countryErrors: [],
                zipcodeErrors: [],
            },      
        // check if this a USD or JPY payment
        isUsd: true,
      }
    },
  
    components: {
    },
    // Vue lifecycle hook mounted() is called when this component is added to the DOM
    // so I guess on page load, getFlps() is called  
    mounted() {
      this.getFlps();
      document.addEventListener('click', this.closeModalOnWindowClick);
      this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'en'})
      const elements = this.stripe.elements();
      this.card = elements.create('card', { hidePostalCode: true })
      this.card.mount('#card-element')
    },

    computed: {

      calculateUsdTaxes() {
        var taxAmount = (parseFloat(this.usdTaxRate * this.usdPrice))
        this.usdTax = taxAmount.toFixed(2);
        return this.usdTax
      },
      calculateUsdSubtotal() {
        // prepending unary operator to these values to treat them as numbers
        // instead of strings for tax calc
        this.usdSubTotal = parseFloat(((this.usdPrice) + (+this.usdTax))).toFixed(2);
        return this.usdSubTotal;
      },

      // JPY TOTAL
      calculateJpyTotal () {
        let sum = 0;
        this.totalJpyPrice = sum;

        return this.totalJpyPrice;
      },
      calculateJpyTaxes() {
        var taxAmount = (parseFloat(this.jpyTaxRate * this.totalJpyPrice))
        this.jpyTax = taxAmount;
        return this.jpyTax
      },
      calculateJpySubtotal() {
        this.jpySubtotal = parseFloat((this.totalJpyPrice + this.jpyTax));
        return this.jpySubtotal
      },

    },
    // functions defined here
    methods: {
      // scroll to top of payment form
      scrollToBottom() {
        console.log('scroll to payment form')
        // wait until modal closes, then scroll to payment form
        this.$nextTick(() => this.$refs["paymentFormTop"].scrollIntoView({ behavior: "smooth" }))
      },
      // BUY NOW METHODS
      submitForm() {
        this.errors.generalErrors = []
        this.errors.nameErrors = []
        this.errors.emailErrors = []
        this.errors.phoneErrors = []
        this.errors.address1Errors = []
        this.errors.address2Errors = []
        this.errors.statePrefErrors = []
        this.errors.countryErrors = []
        this.errors.zipcodeErrors = []

        if (this.name === '') {
            this.errors.nameErrors.push('The name field is missing!')
        }
        if (this.email === '') {
            this.errors.emailErrors.push('The email field is missing!')
        }
        if (this.phone === '') {
            this.errors.phoneErrors.push('The phone field is missing!')
        }
        if (this.address1 === '') {
            this.errors.address1Errors.push('The address field is missing!')
        }
        if (this.statePref === '') {
            this.errors.statePrefErrors.push('The state field is missing!')
        }        
        if (this.country === '') {
            this.errors.countryErrors.push('The country field is missing!')
        }
        if (this.zipcode === '') {
            this.errors.zipcodeErrors.push('The zip code field is missing!')
        }

        // if there are no form validation errors, process payment
        if (
            !this.errors.nameErrors.length &&
            !this.errors.emailErrors.length &&
            !this.errors.phoneErrors.length &&
            !this.errors.address1Errors.length &&
            !this.errors.address2Errors.length &&
            !this.errors.statePrefErrors.length &&
            !this.errors.countryErrors.length &&
            !this.errors.zipcodeErrors.length &&
            !this.errors.generalErrors.length
          ) {
            // set loading animation icon
            this.$store.commit('setIsLoading', true)

            // create stripe token based on user card input
            this.stripe.createToken(this.card).then(result => {                    
                if (result.error) {
                    this.$store.commit('setIsLoading', false)
                    this.errors.generalErrors.push('Something went wrong with Stripe. Please try again')
                    console.log(result.error.message)
                } 
                // if there are no stripe processing errors
                else {
                    this.stripeTokenHandler(result.token)
                }
            })
          }
      },
      // single flp purchase
      async stripeTokenHandler(token) {

        // send empty track items for backend
        const track_items = []
        const track_obj = {
              no_tracks: ''
            }
        track_items.push(track_obj)

        const flp_items = []
          // for flps
            const flp_obj = {
              // flp_id: item.id,
              flp: this.FlpID,
              usd_flp_price: this.usdPrice,        
              jpy_flp_price: this.jpyPrice,
            }
            flp_items.push(flp_obj)

        // get user billing data as well as stripe token and all
        // cart items, both flps and tracks
        const data = {
          'name': this.name,
          'email': this.email,
          'phone': this.phone,
          'address1': this.address1,
          'address2': this.address2,
          'statePref': this.statePref,
          'country': this.country,
          'zipcode': this.zipcode,
          'flp_items': flp_items,
          'track_items': track_items,
          'stripe_token': token.id
        }

        // post data to server; have to send token as well
        await axios
        .post(process.env.VUE_APP_CHECKOUT_API_URL, data,  {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
        .then(response => {
          // reset store
          this.$store.state.downloadableItems = []
          this.$store.state.downloadableItems = response.data   
          // naviaget to thank you page
          this.$router.push('/thankyou')
        })
        .catch(error => {
          console.log(error)
          this.errors.generalErrors.push('Something went wrong. Please try again later')
        })

        this.$store.commit('setIsLoading', false)
      },

      styleObject() {
        return this.show === true ? {display: 'block'} : {display: 'none'}
      },
      clearFields() {
        this.name = ''
        this.email = ''
        this.phone = ''
        this.address1 = ''
        this.address2 = ''
        this.zipcode = ''
        this.statePref = '',
        this.country = '',
        this.errors.generalErrors = []
        this.errors.nameErrors = []
        this.errors.emailErrors = []
        this.errors.phoneErrors = []
        this.errors.address1Errors = []
        this.errors.address2Errors = []
        this.errors.statePrefErrors = []
        this.errors.countryErrors = []
        this.errors.zipcodeErrors = []
      },


      // download free flp now
      downloadFreeNow(flp, id) {
        this.$store.state.freeDownload = flp;
        this.$store.state.freeDownloadId = id;
        this.$store.state.isSingleDownload = true;
        this.$store.state.downloadType = 'flp';


      // get current object being downloaded
      var index = this.flps.findIndex(x => x.id === id);
      const flp_obj = {
        flp_zip: this.flps[index].flp_zip,
        flp_name: this.flps[index].flp_name
      }
      this.$store.state.downloadableItems = []
      this.$store.state.downloadableItems.push(flp_obj)

        this.$router.push('/thankyou')
      },
      // set flp name and id
      buyNow(flp, id){
        this.buyNowItemName = flp;
        this.buyNowItemId = id;
        console.log('\nname: ' + flp + '; flp id: '+ id)
      },
      // called in modal popup on FREE or price button click
      setFlpId(flp) {
        // set flp name and whether it is free well to show in modal popup
        const item = this.flps.find(item => item.id === flp)
        this.FlpName = item.flp_name;
        this.isFree = item.flp_is_free;
        this.FlpID = flp;
        this.usdPrice = item.usd_price;
        this.jpyPrice = item.jpy_price;
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
        await axios.get(process.env.VUE_APP_FLPS_API_URL)
          .then(response => {
            this.flps = response.data
            document.title = 'Flps'
          })
          .catch(error => {
            console.log("ERROR BOYY: " + error)
            console.log(process.env.VUE_APP_FLPS_API_URL)
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
    // remove from cart
    removeFromCart(removeItemID) {
      // get specific track added to cart
      const item = this.flps.find(item => item.id === removeItemID)
      // pass entire json track/flp obj to removeFromCart function
      this.$store.commit('removeFromCart', item)
      toast({
        message: ' \"' + item.flp_name + '\" removed from cart!',
        type: 'is-danger',
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