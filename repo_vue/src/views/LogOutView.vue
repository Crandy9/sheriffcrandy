<template>

</template>

<script>
import axios, { toFormData } from 'axios';
import { toast } from 'bulma-toast'


export default {
    name: 'LogOut',

    beforeCreate() {
        const cartData = {
            cart: this.$store.state.cart.itemsInCart
        }
        
        // log user out, pass in the cart to save it to user
        axios.post(process.env.VUE_APP_LOGOUT_USER_API_URL, cartData , {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
        .then(response => {
            // handle success
            // remove token
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem('sf_auth_bearer')
            this.$store.commit('removeToken')
            // empty cart (or save it for the user's web token)
            this.$store.commit('clearCart')
            this.$store.commit('clearPurchasedTrackList')
            // remove  pfp
            this.$store.state.profile_pic_background_img = null

            this.$router.push('/')
        })
        .catch(error => {

        });
    }
}

</script>