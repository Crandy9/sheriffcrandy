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
      <!-- <p class="my-subtotal">
        <span>Total:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTotal }}</span>
      </p>
      <p class="my-subtotal">
        <span>Tax:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpyTaxes }}</span>
      </p>
      <p class="my-subtotal">
        <span>Subtotal:</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">¥{{ calculateJpySubtotal }}</span>
      </p> -->
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
        <a rel="noindex" class="my-checkout-button" href="#">Checkout</a>
      </div>
    </footer>
    <!-- end cart footer -->
  </section>
</template>


<script>
import axios from 'axios'

export default {

    name: 'Cart',
    data() {
      return {
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
        jpySubtotal:''
      }
    },
    mounted() {
      // get all cart items
      this.cart = this.$store.state.cart
      document.title = 'Cart' 
    },

    methods: {

      removeFromCart(removeItemID) {
        // get specific track added to cart
        const item = this.cart.itemsInCart.find(item => item.id === removeItemID)
        // pass entire json track/flp obj to removeFromCart function
        this.$store.commit('removeFromCart', item)
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
        return parseFloat((this.totalJpyPrice + this.jpyTax));
      },
    }
}
</script>