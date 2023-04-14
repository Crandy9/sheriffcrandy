<template>
    <section class="my-forgotpassword-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-5 is-offset-3">
                    <h1 class="title my-login-title">
                        {{$t('forgotpasswordview.forgotpasswordtitle')}}
                    </h1>
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <!-- general errors-->
                            <div class="my-errors" v-if="errors.generalErrors.length">
                                <p style="color:red" v-for="error in errors.generalErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!-- username/email errors-->
                            <div class="my-errors" v-if="errors.emailErrors.length">
                                <p style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!-- users can enter their email address or username to login -->
                            <label class="my-label" for="">{{$t('forgotpasswordview.email')}}</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" class="input" v-model="email">
                            </div>
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">{{$t('forgotpasswordview.submit')}}</button>
                                </div> 
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ForgotPassword',

    data() {
        return {
            email: null,
            errors: {
                generalErrors: [],
                emailErrors: []
            },     
        }
    },

    // show toast if it exists
    mounted () {

    },

    methods: {
        submitForm() {
            // reset errors
            this.errors.generalErrors = []
            this.errors.emailErrors = []

            console.log(this.email)


            // validate fields
            // USERNAME/EMAIL
            if (this.email === '' || !this.email) {
                this.errors.emailErrors.push(this.$t('forgotpasswordview.errors.emailerror'))
            }

            // if no errors, submit the form and authenticate user
            if (!this.errors.emailErrors.length) {
                // var to hold post data
                // keys must be same strings as model fields in backend api user model
                // values can be named whatever
                const emailAddressToResetPassword = {
                    potential_email_address: this.email,
                }
                console.log('no errors')

                // send post data to backend server
            //     axios
            //         .post(process.env.VUE_APP_AUTHENTICATE_USERS_API_URL, emailAddressToResetPassword)
            //         .then(response => {

            //             // set auth token
            //             const sf_auth_bearer = response.data.auth_token
            //             // set token in store which sets is_authenticated var to true
            //             this.$store.commit('setToken', sf_auth_bearer)
            //             // setting token in axios header
            //             axios.defaults.headers.common['Authorization'] = 'Token ' + sf_auth_bearer
            //             // set token in localstorage
            //             localStorage.setItem("sf_auth_bearer", sf_auth_bearer)

            //             // get user's cart data
            //             axios
            //                 // .get(process.env.VUE_APP_GET_CART_URL, {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
            //                 .get(process.env.VUE_APP_GET_CART_URL, {headers: { 'Authorization': `Token ${sf_auth_bearer}`}})
            //                 .then(response => {

            //                     const cart_data = response.data.cart;
            //                     if (cart_data.length === 0) {
            //                     }
            //                     else {
            //                         // there are cart items, clear the cart if the user added items to cart anonymously
            //                         this.$store.commit('clearCart')

            //                         for (let i = 0; i < cart_data.length; i++) {
            //                             const item = cart_data[i];
            //                             // add item to cart in store
            //                             this.$store.commit('addToCart', item)
            //                         }
            //                     }
            //                     // populate purchasedTracksList
            //                     this.getPurchasedTracks();
            //                 })
            //                 .catch(error => {
            //                     console.log('user cart data get request failed. Printing error')
            //                     console.log(error)

            //                 })

            //             // add toast message
            //             toast({
            //                 message: this.$t('modals.welcomeback') + ' ' + this.email + this.$t('modals.welcomeback2') +'!',
            //                 type: 'is-success',
            //                 dismissible: true,
            //                 pauseOnHover: true,
            //                 duration: 2000,
            //                 position: 'top-center',
            //                 animate: { in: 'fadeIn', out: 'fadeOut' },
            //             })
            //             // check if there is a pending route to be redirected to
            //             // else go to home
            //             const toPath = this.$route.query.to || '/'
            //             // re-route to homepage
            //             this.$router.push(toPath)
            //         })
            //         .catch(error => {
            //             if (error.response) {
            //                 this.errors.generalErrors.push(this.$t('loginsignupview.errors.invalidusernamepassword'))
            //             } 
                        
            //             else if (error.message) {
            //                 this.errors.generalErrors.push(this.$t('loginsignupview.errors.generalerrors'))
            //                 console.log("Didn't work bic boii: " + JSON.stringify(error.response.data))
            //             }
            //         })
            // }
            // else {
            //     console.log('form is invalid')
            }
        },
        toggleShowPassword() {
            this.showPassword = !this.showPassword;
        },
        async getPurchasedTracks() {

            await axios.get(process.env.VUE_APP_GET_TRACK_ORDERS_URL, {headers: { 'Authorization': `Token ${this.$store.state.sf_auth_bearer}`}})
                .then(response => {
                if (response.data.length === 0) {
                }
                else {
                    this.$store.commit('populatePurchasedTrackArray', response.data)
                }
                })
                .catch( error => {
                console.log('ERROR')
                })
        }
    }
}
</script>