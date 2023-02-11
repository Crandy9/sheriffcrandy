<template>
  <section>
    <div class="page-cart">
      <div class="columns is-multiline">
        <div>
          <h1 class="title cart-title">My Cart</h1>
        </div>
        <!-- show cart items -->
        <div class="table-div">
          <table class="table is-fullwidth" v-if="cartTotalLength">
            <thead>
              <tr>
                <th>Tracks/FLPs</th>
                <th>Price</th>
                <th></th>
              </tr>
            </thead>

              <tbody>
                <tr class="rows" v-for="item in cart.itemsInCart">
                    <!-- for tracks -->
                    <td class="table-title" v-if="item.title"><router-link :to="item.get_absolute_url">{{ item.title }} (track)</router-link></td>
                    <td class="table-title" v-else><router-link :to="item.get_absolute_url">{{ item.flp_name }} (flp)</router-link></td>
                    <!-- for flps -->
                    <!-- gotta check for free tracks.flps -->
                    <td v-if="item.is_free == true || item.flp_is_free == true" class="table-price" >FREE</td>
                    <td v-else-if="item.usd_price && (item.is_free == false || item.flp_is_free == false)" class="table-price" >${{ item.usd_price }}</td>
                    <td v-else-if="item.jpy_price && (item.is_free == false || item.flp_is_free == false)" class="table-price" >¥{{ item.jpy_price }}</td>
                    <td class="remove">remove<button class="delete"></button></td>
                </tr>
                <tr>
                  <th>
                    Subtotal <span>{{ subTotal }}</span>
                  </th>
                </tr>
              </tbody>
          </table>
          <p v-else style="color:white">Your cart is empty :(</p>
        </div>
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