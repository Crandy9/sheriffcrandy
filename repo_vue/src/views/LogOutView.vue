<template>

</template>

<script>
import axios, { toFormData } from 'axios';
import { toast } from 'bulma-toast'


export default {
    name: 'LogOut',

    mounted() {
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
        // redirect to homepage
        this.$router.push('/')
    }
}
</script>