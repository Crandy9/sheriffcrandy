<template>

</template>

<script>
import axios, { toFormData } from 'axios';
import { toast } from 'bulma-toast'


export default {
    name: 'LogOut',

    beforeCreate() {
        // log user out
        axios.post(process.env.VUE_APP_LOGOUT_USER_API_URL, null, {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
        .then(response => {
          // handle success
          console.log(response.data.success);
          console.log("successfully logged user out and deleted user's auth token")
          // remove token
          axios.defaults.headers.common["Authorization"] = ""
          localStorage.removeItem('sf_auth_bearer')
          this.$store.commit('removeToken')
          // empty cart (or save it for the user's web token)
          this.$store.commit('clearCart')
          // add toast message
          toast({
              message: this.$t('modals.logout'),
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'top-center',
              animate: { in: 'fadeIn', out: 'fadeOut' },
          })
          this.$router.push('/')
        })
        .catch(error => {
        // handle error
        console.log(error);
        console.log("log out didn't work")
        console.log('axios post logout url')
        console.log(process.env.VUE_APP_LOGOUT_USER_API_URL)
        console.log(process.env.VUE_APP_I18N_FALLBACK_LOCALE)

        });
    }
}

</script>