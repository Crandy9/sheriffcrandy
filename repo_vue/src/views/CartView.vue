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
            <td v-if="item.image" class="my-row-image">
              <img src={{ item.image }} alt="">
            </td>
            <td class="my-col-item-details" colspan="3">
              <div class="my-item-description">
                <!-- track/flp title -->
                <h2 class="my-item-name" v-if="item.title"><router-link :to="item.get_absolute_url">{{ item.title }} (track)</router-link></h2>
                <h2 class="my-item-name" v-else><router-link :to="item.get_absolute_url">{{ item.flp_name }} (flp)</router-link></h2>
                <div v-if="item.title" class="my-cart-item-desc">
                  Track download
                </div>
                <div v-else class="my-cart-item-desc">
                  FLP download
                </div>
              </div>
              <div class="my-cart-item-actions">
                <div class="my-item-quantity">1</div>
                <a class="my-remove-button remove">remove<button class="delete"></button></a>
                  <div class="my-cart-price" v-if="item.is_free == true || item.flp_is_free == true">FREE</div>
                    <div class="my-cart-price" v-else-if="item.usd_price && (item.is_free == false || item.flp_is_free == false)">${{ item.usd_price }}</div>
                    <div class="my-cart-price" v-else-if="item.jpy_price && (item.is_free == false || item.flp_is_free == false)">¥{{ item.jpy_price }}</div>                
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <p v-else style="color:white">Your cart is empty :(</p>
    </div>
    <!-- end cart body -->

    <!-- cart footer -->
    <footer class="my-cart-footer">
      <p class="my-subtotal">
        <span>Subtotal</span>
        <span style="padding-left: 0.5rem;" data-cart--cart-target="total">${{ subTotal }}</span>
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
        subTotal: ''
      }
    },
    mounted() {
      // get all cart items
      this.cart = this.$store.state.cart
      document.title = 'Cart' 
    },

    computed: {
        cartTotalLength() {
          let totalLength = this.cart.itemsInCart.length;
          return totalLength;
        },
        // whenever cart changes, cart count will automatically update
        calculateSubtotal() {

          for (let i = 0; i < this.cart.itemsInCart.length; i++) {
            this.subTotal+= i
          }
          return totalLength;
        }
    }
}
</script>