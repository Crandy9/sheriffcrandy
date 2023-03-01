<template>
  <!-- stripe payment modal -->
  <transition>
    <div style="z-index: 9999;" v-if="modalOpened" id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
        <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <p class="modal-card-title">Checkout</p>
              <button @click="modalOpened = false; clearFields();" class="delete" aria-label="close"></button>
            </header>
            <section class="modal-card-body">
              <div class="page-checkout">
                <div class="columns is-multiline">
                    <div class="column is-12 box">
                      <h2 style= "text-align: center;" class="subtitle has-text-black has-text-center is-underlined">Payment Details</h2>
                      <h2 class="subtitle has-text-black">Billing Address</h2>
                      <!-- <p class="has-text-danger mb-4">* All fields are required</p> -->
                      <div class="columns is-multiline">
                        <!-- general errors -->
                        <div v-if="errors.generalErrors.length">
                            <p class="my-errors" style="color:red" v-for="error in errors.generalErrors" v-bind:key="error">
                            <span style="color:red !important">*</span> {{ error }}
                            </p>                        
                        </div>
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

                    <div class="mb-5 has-text-black">
                      <h2 class="subtitle has-text-black">Card Information</h2>
                    </div>
                </div>
              </div>
              <label for="card-element">Card</label>
              <div id="card-element" class="mb-5 control"></div>
            </section>
            <footer class="modal-card-foot">
              <button @click="submitForm();" class="my-modal-button-buy-now button">Pay</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="modalOpened = false; clearFields();" class="my-modal-button-cancel button">Cancel</button>
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
import axios from 'axios'

export default {
    data() {
      return {
        modalOpened : false,
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
    

    mounted () {
        document.title= 'Checkout'
        this.cart = this.$store.state.cart;
        this.modalOpened = true
        if (this.cart.itemsInCart.length > 0) {
            this.stripe = Stripe(process.env.VUE_APP_CHECKOUT_API_URL)
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
        }
    },

    methods: {

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
      },
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
        // if (this.address2 === '') {
        //     this.errors.address2Errors.push('The address field is missing!')
        // }
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

      async stripeTokenHandler(token) {

        const items = []
        var flp_quantity = 0
        var track_quantity = 0

        for (let i = 0; i < this.cart.itemsInCart.length; i++) {
          const item = this.cart.itemsInCart[i];
          // for tracks
          if ('title' in item) {
            const track_obj = {
              track: item.track.id,
              track_quantity: track_quantity++,
              flp_quantity: flp_quantity,
              price: (isUsd === true ? item.track.usd_price : item.track.jpy_price)
            }
            items.push(track_obj)

          }
          if ('flp_name' in item) {
            const flp_obj = {
              flp: item.flp.id,
              flp_quantity: flp_quantity++,
              track_quantity: track_quantity,
              price: (isUsd === true ? item.flp.usd_price : item.flp.jpy_price)            
            }
            items.push(flp_obj)
            console.log(JSON.stringify(flp_obj))
          }
        }

        console.log(JSON.stringify(items))

        // get user billing data as well as stripe token in an obj
        const data = {
          'name': this.name,
          'email': this.email,
          'phone': this.phone,
          'address1': this.address1,
          'address2': this.address2,
          'statePref': this.statePref,
          'country': this.country,
          'zipcode': this.zipcode,
          'items': items,
          'stripe_token': token.id
        }

        // post data to server
        await axios
        .post(process.env.VUE_APP_CHECKOUT_API_URL, data)
        .then(response => {
          // if response was successful, clear the cart
          this.$store.commit('clearCart')
          // naviaget to thank you page
          this.$router.push('/thankyou')
        })
        .catch(error => {
          console.log('django server error')
          console.log(error)
          this.errors.generalErrors.push('Something went wrong. Please try again later')
        })

        this.$store.commit('setIsLoading', false)
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
        var taxAmount = (parseFloat(this.jpyTaxRate * this.totalJpyPrice))
        this.jpyTax = taxAmount;
        return this.jpyTax
      },
      calculateJpySubtotal() {
        return parseFloat((this.totalJpyPrice + this.jpyTax));
      },
    },
}

</script>