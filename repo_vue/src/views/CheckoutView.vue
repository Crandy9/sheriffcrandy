<template>

    <div>
        <h1>
            CHECKOUT CUZZ!
        </h1>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
        cart: {
          itemsInCart: [],
        },
        // stripe stuff
        stripe: {},
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        address: '',
        zipcode: '',
        place: '',
        errors: [],
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

    mounted () {
        document.title= 'Checkout'
        this.cart = this.$store.state.cart;
    },

    methods: {
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
    },
}

</script>