<template>
  <!-- section -->
  <section class="my-cart-section">
    <!-- cart body -->
    <div class="my-cart-body">
      <!-- cart header -->
      <div class="my-cart-content">
        <h2 class="my-cart-title">
          <span>{{$t('cartview.carttitle')}}</span>
        </h2>
      </div>
      <table class="my-cart-items-table" v-if="cartTotalLength">
        <tbody id="testid" class="my-cart-items">
          <!-- loop through all items in cart -->
          <tr class="my-table-row" v-for="item in cart.itemsInCart">
            <!-- get image (for tracks only) -->
            <td v-if="item.get_cover_art" class="my-row-image">
              <img v-bind:src="item.get_cover_art" alt="">
            </td>
            <td class="my-col-item-details" colspan="3">
              <div class="my-item-description">
                <!-- track/flp title -->
                <h2 class="my-item-name" v-if="item.title">{{ item.title }} ( {{$t('cartview.wavfile')}} )</h2>
                <h2 class="my-item-name" v-else>{{ item.flp_name }} ( {{$t('cartview.zipfile')}} )</h2>
                <div v-if="item.title" class="my-cart-item-desc">
                  Track download
                </div>
                <div v-else class="my-cart-item-desc">
                  FLP download
                </div>
              </div>
              <div class="my-cart-item-actions">
                <!-- <div class="my-item-quantity">1</div> -->
                <a @click="removeFromCart(item.id);" class="my-remove-button">{{$t('cartview.remove')}}<button class="delete"></button></a>
                  <div class="my-cart-price" v-if="item.is_free == true || item.flp_is_free == true">{{$t('cartview.free')}}</div>
                  <!-- usd -->
                  <div class="my-cart-price" v-else-if="item.usd_price && (item.is_free == false || item.flp_is_free == false) && $store.state.region === 'US'">${{ item.usd_price }}</div>
                  <!-- jpy -->
                  <div class="my-cart-price" v-else-if="item.jpy_price && (item.is_free == false || item.flp_is_free == false) && $store.state.region === 'JP'">¥{{ item.jpy_price }}</div>                
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <p v-else style="color:white; padding: 2rem;" >{{$t('cartview.emptycart')}} :(</p>
    </div>
    <!-- end cart body -->
    <!-- cart footer US -->
    <footer v-if="cart.itemsInCart.length && $store.state.region === 'US'" class="my-cart-footer">
      <a class="my-clear-cart-button" @click="show = false; purchaseButtonClicked = false; clearCart();">{{$t('cartview.clearcart')}}</a>
      <p class="my-subtotal">
        <span>{{$t('cartview.total')}}:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTotal }}</span>
      </p>
      <p class="my-subtotal">
        <span>{{$t('cartview.tax')}}:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTaxes }}</span>
      </p>
      <p class="my-subtotal">
        <span>{{$t('cartview.subtotal')}}:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdSubtotal }}</span>
      </p>
      <div class="my-checkout-button-div">
        <!-- if the cart has only one free item -->
        <a v-if="calculateUsdSubtotal === '0.00'" @click.prevent="show = false; purchaseButtonClicked = false; freeDownloads();"  rel="noindex" class="my-checkout-button" >{{$t('cartview.download')}}</a>
        <!-- if the cart has at least one item which is not free -->
        <a v-else="cartTotalLength >= 1 && calculateUsdSubtotal !== '0.00'" @click="show = true; purchaseButtonClicked = true; scrollToBottom();"  rel="noindex" class="my-checkout-button" >{{$t('cartview.checkout')}}</a>
      </div>
    </footer>
      <!-- cart footer JP -->
      <footer v-if="cart.itemsInCart.length && $store.state.region === 'JP'" class="my-cart-footer">
        <a class="my-clear-cart-button" @click="show = false; purchaseButtonClicked = false; clearCart();">{{$t('cartview.clearcart')}}</a>
        <p class="my-subtotal">
          <span>{{$t('cartview.total')}}:</span>
          <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTotal }}</span>
        </p>
        <p class="my-subtotal">
          <span>{{$t('cartview.tax')}}:</span>
          <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTaxes }}</span>
        </p>
        <p class="my-subtotal">
          <span>{{$t('cartview.subtotal')}}:</span>
          <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpySubtotal }}</span>
        </p>

        <div class="my-checkout-button-div">
          <!-- if the cart has only one free item -->
          <a v-if="calculateUsdSubtotal == 0.00 && calculateJpySubtotal === 0" @click.prevent="show = false; purchaseButtonClicked = false; freeDownloads();"  rel="noindex" class="my-checkout-button" >{{$t('cartview.download')}}</a>
          <!-- if the cart has at least one item which is not free -->
          <a v-else-if="cartTotalLength >= 1 && (calculateUsdSubtotal != 0.00 || calculateJpySubtotal !== 0)" @click="show = true; purchaseButtonClicked = true; scrollToBottom();"  rel="noindex" class="my-checkout-button" >{{$t('cartview.checkout')}}</a>
        </div>
    </footer>
    <!-- end cart footer -->

    <!-- checkout form initially hidden -->
    <!-- stripe payment form -->
      <div style="z-index: 9999;" class="my-checkout-div"
        :style="showPaymentForm()" v-bind:class="{'is-active': purchaseButtonClicked}" ref="paymentFormTop">
          <!-- <div class="modal-background"></div> -->
            <div class="card">
              <header class="card-head">
                <!-- <p class="card-title">{{$t('paymentmodal.modaltitle')}}</p> -->
                <button class="delete close-button" @click="show = false; clearFields(); purchaseButtonClicked = false;" aria-label="close"></button>
              </header>
              <section class="card-body">
                <div class="page-checkout">
                  <div class="columns is-multiline">
                      <div class="column is-12 box">
                        <h2 style= "text-align: center;" class="subtitle has-text-black has-text-center is-underlined">{{$t('paymentmodal.paymentdetails')}}</h2>
                        <h2 class="subtitle has-text-black">{{$t('paymentmodal.billingaddress')}}</h2>
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
                              <label class="my-label has-text-black">{{$t('paymentmodal.name')}}</label>
                              <div class="control">
                                  <input type="text" class="input" :placeholder="$t('paymentmodal.placeholdername')" v-model="name">
                              </div>
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.email')}}</label>
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
                              <label class="my-label has-text-black">{{$t('paymentmodal.phone')}}</label>
                              <div class="control">
                                  <input type="text" class="input" :placeholder="$t('paymentmodal.placeholderphone')" v-model="phone">
                              </div>
                            </div>
                            <!-- address1 errors-->
                            <div v-if="errors.address1Errors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.address1Errors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.street1')}}</label>
                              <div class="control">
                                  <input type="text" class="input" :placeholder="$t('paymentmodal.street1placeholder')" v-model="address1">
                              </div>
                            </div>
                              <!-- address2 errors-->
                              <div v-if="errors.address2Errors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.address2Errors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <div class="field">
                              <label class="my-label has-text-black">{{$t('paymentmodal.street2')}}</label>
                              <div class="control">
                                  <input type="text" class="input" :placeholder="$t('paymentmodal.street2placeholder')"  v-model="address2">
                              </div>
                            </div>
                          </div>
                          <div class="column is-6">
                              <!-- country errors-->
                              <div v-if="errors.countryErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.countryErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <div class="field">
                                <label class="my-label has-text-black">{{$t('paymentmodal.country')}}</label>
                                <div class="control has-icons-left">
                                    <select class="input" v-model="country" name="country" id="id_country">
                                      <option style="color:rgba(0,0,0,0.4) !important" value="" disabled selected hidden>
                                          {{$t('paymentmodal.countryplaceholder')}}
                                      </option>
                                      <option v-for="cya in $store.state.countries" :value="cya.countryval" style="color: black !important;">{{cya.countryname}}</option>
                                    </select>
                                    <div class="icon is-small is-left">
                                      <i class="fas fa-globe" style="color: rgb(55,195,255)"></i>
                                    </div>
                                </div>
                              </div>
                              <!-- statepref errors-->
                              <div v-if="errors.statePrefErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.statePrefErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <!-- prefectures -->
                              <div v-if="this.country === 'JP'" class="field">
                                <label class="my-label has-text-black">{{$t('paymentmodal.pref')}}</label>
                                <div class="control">
                                  <select v-model="statePref" name="statepref" class="input">
                                    <option value="" disabled selected hidden>
                                            {{$t('paymentmodal.prefplaceholder')}}
                                    </option>
                                    <option v-for="pref in $store.state.prefectures" :key="pref.prefval" :value="pref.prefval" style="color: black !important;">{{pref.prefval}}</option>
                                  </select>
                                </div>
                              </div>
                              <!-- states -->
                              <div v-if="this.country === 'US'" class="field">
                                <label class="my-label has-text-black">{{$t('paymentmodal.state')}}</label>
                                <div class="control">
                                  <select v-model="statePref" name="statepref" class="input">
                                    <option value="" disabled selected hidden>
                                            {{$t('paymentmodal.stateplaceholder')}}
                                    </option>
                                    <option v-for="state in $store.state.usstates" :key="state.stateval" :value="state.stateval" style="color: black !important;">{{state.statename}}</option>
                                  </select>
                                </div>
                              </div>
                              <!-- post code errors-->
                              <div v-if="errors.zipcodeErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.zipcodeErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                              </div>
                              <div class="field">
                                <label class="my-label has-text-black">{{$t('paymentmodal.postcode')}}</label>
                                <div class="control">
                                    <input type="text" class="input" :placeholder="$t('paymentmodal.postcodeplaceholder')" v-model="zipcode">
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
                        <h2 class="my-credit-card-subtitle has-text-black">{{$t('paymentmodal.cardinfo')}}</h2>
                      </div>
                  </div>
                </div>
                <div class="stripe-card-div">
                  <div id="card-element" class="mb-5 control"></div>
                </div>
              </section>
              <!-- for usd -->
              <footer v-if="$store.state.region === 'US'" class="card-foot">
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.total')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTotal }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.tax')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTaxes }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.subtotal')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdSubtotal }}</span>
                </p>
                <button @click.stop="submitForm();" :disabled="paymentProcessing" class="my-button-buy-now button">
                  <span v-if="paymentProcessing">
                    {{$t('paymentmodal.paymentprocessing')}}
                  </span>
                  <span v-else>
                    {{$t('paymentmodal.pay')}} ${{ calculateUsdSubtotal }}
                  </span>
                </button>                
                <!-- if adding to cart, add the item to cart and close modal -->
                <button @click="show = false; clearFields(); purchaseButtonClicked = false;" class="my-button-cancel button">
                  {{$t('paymentmodal.cancel')}}
                </button>
              </footer>
              <!-- for jpy -->
              <footer v-else-if="$store.state.region === 'JP'" class="card-foot">
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.total')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTotal }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.tax')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTaxes }}</span>
                </p>
                <p class="my-subtotal has-text-black">
                  <span>{{$t('cartview.subtotal')}}:</span>
                  <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpySubtotal }}</span>
                </p>
                <button @click.stop="submitForm();" :disabled="paymentProcessing" class="my-button-buy-now button">
                  <span v-if="paymentProcessing">
                    {{$t('paymentmodal.paymentprocessing')}}
                  </span>
                  <span v-else>
                    {{$t('paymentmodal.pay')}} ¥{{ calculateJpySubtotal }}
                  </span>
                </button>                
                <!-- if adding to cart, add the item to cart and close modal -->
                <button @click="show = false; clearFields(); purchaseButtonClicked = false;" class="my-button-cancel button">
                  {{$t('paymentmodal.cancel')}}
                </button>
              </footer>
            </div>
      </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {

    name: 'Cart',
    data() {
      return {
        paymentProcessing: false,
        // country dropdowns
        stateDropdowns: [
          {}
        ],
        prefDropdowns: [{}],
        purchaseButtonClicked: false,
        show: false,
        cart: {
          itemsInCart: [],
        },
        totalUsdPrice: '',
        totalJpyPrice: '',
        usdTaxRate: .0,
        jpyTaxRate: 0.1,
        usdTax: '',
        jpyTax: '',
        usdSubTotal: '',
        jpySubtotal:'',
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

    
    mounted() {
      // get all cart items
      this.cart = this.$store.state.cart
      document.title = 'Cart' 
      if (this.cart.itemsInCart.length > 0) {
        this.$store.state.region === 'US' ? this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'en'}) : this.stripe = Stripe(process.env.VUE_APP_STRIPEPK, {locale: 'ja'})
          const elements = this.stripe.elements();
          this.card = elements.create('card', { hidePostalCode: true })
          this.card.mount('#card-element')
      }
    },

    methods: {

      // free downloads
      async freeDownloads() {
        this.$store.state.downloadableItems = []
        // loop through cart and get all free items
        const flp_items = []
        const track_items = []

        for (let i = 0; i < this.cart.itemsInCart.length; i++) {
          const item = this.cart.itemsInCart[i];
          // for tracks
          // push to store for frontend. May not need this
          if ('title' in item) {
            // for frontend
            const track_obj = {
              track: item.track,
              title: item.title
            }
            this.$store.state.downloadableItems.push(track_obj)

            // for backend
            const track_obj_for_backend = {
              track: item.id
            }
            track_items.push(track_obj_for_backend)

          }
          // for flps
          // push to store for frontend. May not need this
          if ('flp_name' in item) {
            const flp_obj = {
              flp_zip: item.flp_zip,
              flp_name: item.flp_name
            }
            this.$store.state.downloadableItems.push(flp_obj)

            // for backend
            const flp_obj_for_backend = {
              flp: item.id
            }
            flp_items.push(flp_obj_for_backend)
          }
        }

        // check if flp_items array or track_items arrays are empty
        // send this in as a flag to backend
        if (!Array.isArray(flp_items) || !flp_items.length) {
            const flp_obj = {
              no_flps: ''
            }
            flp_items.push(flp_obj)
        }
        if (!Array.isArray(track_items) || !track_items.length) {
            const track_obj = {
              no_tracks: ''
            }
            track_items.push(track_obj)
        }
        // cart items, both flps and tracks
        const data = {
          'flp_items': flp_items,
          'track_items': track_items,
        }

        // if there was only one free track or one free flp 
        if (this.$store.state.downloadableItems.length === 1) {
          // buying one purchased item from cart
          await axios
          .post(process.env.VUE_APP_FREEDOWNLOAD_API_URL, data,  {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
          .then(response => {
            // reset store
            this.$store.state.downloadableItems = []
            this.$store.state.downloadableItems = response.data
            // if response was successful, clear the cart
            this.$store.commit('clearCart')
            // naviaget to thank you page
            this.$router.push('/thankyou')
          })
          .catch(error => {
            console.log(error)
            this.paymentProcessing = false;
            this.errors.generalErrors.push('Something went wrong. Please try again later')
          })

          this.$store.commit('setIsLoading', false)
        }

        // there were multiple free tracks and/or flp files
        else {
          // post data to server; have to set auth token as well as arraybuffer headers for zip file responses
          await axios
          .post(process.env.VUE_APP_FREEDOWNLOAD_API_URL, 
                data, 
                {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}, responseType: 'arraybuffer'})
          .then(response => {
              const url = window.URL.createObjectURL(new Blob([response.data]))
              const link = document.createElement('a')
              link.href = url
              // if it is a single wav file
              link.setAttribute('download', 'SheriffCrandyDownloadables.zip')
              document.body.appendChild(link)
              link.click()
              // redirect to thank you page
              this.$router.push('/thankyou')
          })
          .catch(error => {
            console.log(error)
            this.paymentProcessing = false;
            this.errors.generalErrors.push('Something went wrong. Please try again later')
          })
          this.$store.commit('setIsLoading', false)
        }
      },

      // scroll to top of payment form
      scrollToBottom() {
        // wait until modal closes, then scroll to payment form
        this.$nextTick(() => this.$refs["paymentFormTop"].scrollIntoView({ behavior: "smooth" }))
      },

      // for paid tracks/flps
      submitForm() {
        this.paymentProcessing = true;
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
            this.paymentProcessing = false;
            this.errors.nameErrors.push('The name field is missing!')
        }
        if (this.email === '') {
            this.paymentProcessing = false;
            this.errors.emailErrors.push('The email field is missing!')
        }
        if (this.phone === '') {
            this.paymentProcessing = false;
            this.errors.phoneErrors.push('The phone field is missing!')
        }
        if (this.address1 === '') {
            this.paymentProcessing = false;
            this.errors.address1Errors.push('The address field is missing!')
        }
        if (this.statePref === '') {
            this.paymentProcessing = false;
            this.errors.statePrefErrors.push('The state field is missing!')
        }        
        if (this.country === '') {
            this.paymentProcessing = false;
            this.errors.countryErrors.push('The country field is missing!')
        }
        if (this.zipcode === '') {
            this.paymentProcessing = false;
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
                    this.paymentProcessing = false;
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

      // for paid track/flp items
      async stripeTokenHandler(token) {
        
        const flp_items = []
        const track_items = []

        for (let i = 0; i < this.cart.itemsInCart.length; i++) {
          const item = this.cart.itemsInCart[i];
          // for tracks
          if ('title' in item) {
            const track_obj = {
              track: item.id,
              usd_track_price: item.usd_price,
              jpy_track_price: item.jpy_price
            }
            track_items.push(track_obj)

          }
          // for flps
          if ('flp_name' in item) {
            const flp_obj = {
              // flp_id: item.id,
              flp: item.id,
              usd_flp_price: item.usd_price,        
              jpy_flp_price: item.jpy_price
            }
            flp_items.push(flp_obj)
          }
        }

        // check if flp_items array or track_items arrays are empty
        // send this in as a flag to backend
        if (!Array.isArray(flp_items) || !flp_items.length) {
            const flp_obj = {
              no_flps: ''
            }
            flp_items.push(flp_obj)
        }
        if (!Array.isArray(track_items) || !track_items.length) {
            const track_obj = {
              no_tracks: ''
            }
            track_items.push(track_obj)
        }

        // for a single paid flp or track. 
        if (this.cart.itemsInCart.length === 1) {
          var jpy_paid_amount = 0
          var usd_paid_amount = 0
          // set currency based on language which is being used to set the region as well
          this.$store.state.region === 'US' ? (usd_paid_amount = this.calculateUsdSubtotal, jpy_paid_amount = 0) : (usd_paid_amount = 0, jpy_paid_amount = this.calculateJpySubtotal)

          // buying one purchased item from cart
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
            'stripe_token': token.id,
            'jpy_paid_amount': jpy_paid_amount,
            'usd_paid_amount': usd_paid_amount,
          }

          await axios
          .post(process.env.VUE_APP_CHECKOUT_API_URL, data,  {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
          .then(response => {
            // reset store
            this.$store.state.downloadableItems = []
            this.$store.state.downloadableItems = response.data        
            // redirect to thank you page
            this.paymentProcessing = false;
            this.$router.push('/thankyou')
          })
          .catch(error => {
            console.log(error)
            this.paymentProcessing = false;
            this.errors.generalErrors.push('Something went wrong. Please try again later')
          })
          this.$store.commit('setIsLoading', false)
        }
        // for multiple items
        else {
          var jpy_paid_amount = 0
          var usd_paid_amount = 0
          // set currency based on language which is being used to set the region as well
          this.$store.state.region === 'US' ? (usd_paid_amount = this.calculateUsdSubtotal, jpy_paid_amount = 0) : (usd_paid_amount = 0, jpy_paid_amount = this.calculateJpySubtotal)
          
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
            'stripe_token': token.id,
            'jpy_paid_amount': jpy_paid_amount,
            'usd_paid_amount': usd_paid_amount,
          }

          await axios
          .post(process.env.VUE_APP_CHECKOUT_API_URL, 
                data, 
                {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}, responseType: 'arraybuffer'})
          .then(response => {
            // reset store
            this.$store.state.downloadableItems = []
            this.$store.state.downloadableItems = response.data
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            link.setAttribute('download', 'SheriffCrandyDownloadables.zip')
            document.body.appendChild(link)
            link.click()
            this.paymentProcessing = false;
            this.$router.push('/thankyou')
          })
          .catch(error => {
            console.log(error)
            this.paymentProcessing = false;
            this.errors.generalErrors.push('Something went wrong. Please try again later')
          })
          this.$store.commit('setIsLoading', false)
        }
      },

      showPaymentForm() {
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

      removeFromCart(removeItemID) {
        // get specific track added to cart
        const item = this.cart.itemsInCart.find(item => item.id === removeItemID)
          if (JSON.stringify(item.flp_name) == undefined) {
            console.log('track ' + JSON.stringify(item.title) + ' removed from cart')
          }
          else {
            console.log('flp ' + JSON.stringify(item.flp_name) + ' removed from cart')
          }

        // pass entire json track/flp obj to removeFromCart function
        this.$store.commit('removeFromCart', item)
      },
      clearCart() {
        this.$store.commit('clearCart')
      }
    },

    computed: {

      // display cart only if there are items in the cart, 
      cartTotalLength() {
        let totalLength = this.cart.itemsInCart.length;
        return totalLength;
      },

      // USD TOTAL
      calculateUsdTotal() {
        let sum = 0;
        for(let i = 0; i < this.cart.itemsInCart.length; i++){
          sum += (parseFloat(this.cart.itemsInCart[i].usd_price));
        }

        this.totalUsdPrice = sum.toFixed(2);

        return this.totalUsdPrice;
      },
      calculateUsdTaxes() {
        var taxAmount = (parseFloat(this.usdTaxRate * this.totalUsdPrice))
        this.usdTax = taxAmount.toFixed(2);
        return this.usdTax
      },
      calculateUsdSubtotal() {
        // prepending unary operator to these values to treat them as numbers
        // instead of strings for tax calc
        this.usdSubTotal = parseFloat(((+this.totalUsdPrice) + (+this.usdTax))).toFixed(2);
        return this.usdSubTotal;
      },


      // JPY TOTAL
      calculateJpyTotal () {
        let sum = 0;
        for(let i = 0; i < this.cart.itemsInCart.length; i++){
          sum += (this.cart.itemsInCart[i].jpy_price);
        }
        this.totalJpyPrice = sum;

        return this.totalJpyPrice;
      },
      calculateJpyTaxes() {
        var taxAmount = Math.round(parseFloat(this.jpyTaxRate * this.totalJpyPrice));
        this.jpyTax = taxAmount;
        return this.jpyTax
      },
      calculateJpySubtotal() {

        this.jpySubtotal = Math.round(parseFloat(this.totalJpyPrice + this.jpyTax));

        return this.jpySubtotal
      },
    }
}
</script>