<template>
  <!-- section -->
  <section class="my-cart-section">
    <!-- cart body -->
    <div class="my-cart-body">
      <!-- cart header -->
      <div class="my-cart-content">
        <h2 class="my-cart-title">
          <span>Your cart</span>
        </h2>
      </div>
      <table class="my-cart-items-table" v-if="cartTotalLength">
        <a class="my-clear-cart-button" @click="clearCart()">Clear Cart</a>
        <tbody class="my-cart-items">
          <!-- loop through all items in cart -->
          <tr class="my-table-row" v-for="item in cart.itemsInCart">
            <!-- get image (for tracks only) -->
            <td v-if="item.get_cover_art" class="my-row-image">
              <img v-bind:src="item.get_cover_art" alt="">
            </td>
            <td class="my-col-item-details" colspan="3">
              <div class="my-item-description">
                <!-- track/flp title -->
                <h2 class="my-item-name" v-if="item.title">{{ item.title }} (wav audio file)</h2>
                <h2 class="my-item-name" v-else>{{ item.flp_name }} (FLP zip file)</h2>
                <div v-if="item.title" class="my-cart-item-desc">
                  Track download
                </div>
                <div v-else class="my-cart-item-desc">
                  FLP download
                </div>
              </div>
              <div class="my-cart-item-actions">
                <!-- <div class="my-item-quantity">1</div> -->
                <a @click="removeFromCart(item.id)" class="my-remove-button">remove<button class="delete"></button></a>
                  <div class="my-cart-price" v-if="item.is_free == true || item.flp_is_free == true">FREE</div>
                    <div class="my-cart-price" v-else-if="item.usd_price && (item.is_free == false || item.flp_is_free == false)">${{ item.usd_price }}</div>
                    <div class="my-cart-price" v-else-if="item.jpy_price && (item.is_free == false || item.flp_is_free == false)">¥{{ item.jpy_price }}</div>                
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <p v-else style="color:white; padding: 2rem;" >Your cart is empty :(</p>
    </div>
    <!-- end cart body -->

    <!-- cart footer -->
    <footer v-if="cart.itemsInCart.length" class="my-cart-footer">
      <p class="my-subtotal">
        <span>Total:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTotal }}</span>
      </p>
      <p class="my-subtotal">
        <span>Tax:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdTaxes }}</span>
      </p>
      <p class="my-subtotal">
        <span>Subtotal:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ calculateUsdSubtotal }}</span>
      </p>
      <div class="my-checkout-button-div">
        <a @click="modalOpened = true;" rel="noindex" class="my-checkout-button" v-if="cartTotalLength >= 1" >Checkout</a>
      </div>
    </footer>
    <!-- end cart footer -->
  </section>

  <!-- stripe payment modal -->
  <Transition>
      <div style="z-index: 9999;" v-if="modalOpened" id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
        <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <p class="modal-card-title">Checkout</p>
              <button @click="modalOpened = false" class="delete" aria-label="close"></button>
            </header>
            <section class="modal-card-body">
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
                            <!-- place errors-->
                            <div v-if="errors.placeErrors.length">
                              <p class="my-errors" style="color:red" v-for="error in errors.placeErrors" v-bind:key="error">
                              <span style="color:red !important">*</span> {{ error }}
                              </p>                        
                            </div>
                            <div class="field">
                                <label class="has-text-black">Place</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="place">
                                </div>
                            </div>
                        </div>
                      </div>
                    </div>
                    <hr>

                    <div id="card-element" class="mb-5 has-text-black">
                      <h2 class="subtitle has-text-black">Card Information</h2>
                    </div>
                </div>
              </div>
            </section>
            <footer class="modal-card-foot">
              <button @click="submitForm()" class="my-modal-button-buy-now button">Pay</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click="modalOpened = false; clearFields();" class="my-modal-button-cancel button">Cancel</button>
            </footer>
          </div>
      </div>
    </Transition>

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

    name: 'Cart',
    data() {
      return {
        modalOpened: false,
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
        place: '',
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
                placeErrors: []
            },      
      }
    },
    mounted() {
      // get all cart items
      this.cart = this.$store.state.cart
      document.title = 'Cart' 
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
        this.place = ''
        this.errors.generalErrors = []
        this.errors.nameErrors = []
        this.errors.emailErrors = []
        this.errors.phoneErrors = []
        this.errors.address1Errors = []
        this.errors.address2Errors = []
        this.errors.statePrefErrors = []
        this.errors.countryErrors = []
        this.errors.zipcodeErrors = []
        this.errors.placeErrors = []
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
        this.errors.placeErrors = []

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
        if (this.place === '') {
            this.errors.placeErrors.push('The place field is missing!')
        }

        if (
            !this.errors.nameErrors.length &&
            !this.errors.emailErrors.length &&
            !this.errors.phoneErrors.length &&
            !this.errors.address1Errors.length &&
            !this.errors.address2Errors.length &&
            !this.errors.statePrefErrors.length &&
            !this.errors.countryErrors.length &&
            !this.errors.zipcodeErrors.length &&
            !this.errors.placeErrors.length
          ) 
          {
          console.log('no errors')
                // this.$store.commit('setIsLoading', true)
                // this.stripe.createToken(this.card).then(result => {                    
                //     if (result.error) {
                //         this.$store.commit('setIsLoading', false)
                //         this.errors.push('Something went wrong with Stripe. Please try again')
                //         console.log(result.error.message)
                //     } else {
                //         this.stripeTokenHandler(result.token)
                //     }
                // })
            }
      },

      stripePaymentModal() {

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
        var taxAmount = (parseFloat(this.jpyTaxRate * this.totalJpyPrice))
        this.jpyTax = taxAmount;
        return this.jpyTax
      },
      calculateJpySubtotal() {
        this.jpySubtotal = parseFloat((this.totalJpyPrice + this.jpyTax));
        return this.jpySubtotal
      },
    }
}
</script>