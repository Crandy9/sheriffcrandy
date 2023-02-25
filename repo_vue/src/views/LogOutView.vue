<template>

</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast'


export default {
    name: 'LogOut',

    mounted() {
        // remove token
        axios.defaults.headers.common["Authorization"] = ""
        localStorage.removeItem('sf_auth_bearer')
        this.$store.commit('removeToken')
        // add toast message
        toast({
            message: 'Successfully Logged out',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 3000,
            position: 'top-center',
            animate: { in: 'fadeIn', out: 'fadeOut' },
        })
        // redirect to homepage
        this.$router.push('/')
    },
    // methods: {
    //     logout() {
    //         // remove token
    //         axios.defaults.headers.common["Authorization"] = ""
    //         localStorage.removeItem('sf_auth_bearer')
    //         this.$store.commit('removeToken')
    //         // redirect to homepage
    //         this.$router.push('/')
    //     }
    // }
}
</script>