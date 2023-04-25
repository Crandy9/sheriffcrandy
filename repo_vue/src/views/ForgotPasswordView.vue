<template>
    <section class="my-forgotpassword-section">
        <div class="forgot-password-form-container">
            <h5 class="my-forgot-password-title">
                {{$t('forgotpasswordview.forgotpasswordtitle')}}
            </h5>
            <!-- sign up form prevent default action -->
            <form class="password-reset-form" @submit.prevent="submitForm">
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
                    <!-- <label class="my-forgot-password-email-label" for="">{{$t('forgotpasswordview.email')}}</label> -->
                    <div class="control forgot-password-control">
                        <!-- v-model connects the data var defined below -->
                        <input type="text" class="input forgot-password-input" placeholder="123@my-email.com" v-model="email">
                    </div>
                    <!-- submit form -->
                    <div class="field">
                        <div class="control">
                            <button class="button reset-password-button">{{$t('forgotpasswordview.submit')}}</button>
                        </div> 
                    </div>
                </div>
            </form>
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
        document.title = 'Reset Password';
    },

    methods: {
        submitForm() {
            
            // loading bar while api data is getting fetched
            this.$store.commit('setIsLoading', true);
            // reset errors
            this.errors.generalErrors = []
            this.errors.emailErrors = []

            console.log(this.email)


            // validate fields
            // USERNAME/EMAIL
            if (this.email === '' || !this.email || !/\S+@\S+\.\S+/.test(this.email)) {
                this.errors.emailErrors.push(this.$t('forgotpasswordview.errors.emailerror'))
            }

            // if no errors, submit the form and authenticate user
            if (!this.errors.emailErrors.length) {
                // var to hold post data
                // keys must be same strings as model fields in backend api user model
                // values can be named whatever
                const passwordresetdata = {
                    potential_email_address: this.email,
                    password_reset_url: '/resetpassword'
                }

                // send post data to backend server
                axios
                    .post(process.env.VUE_APP_CREATE_RESET_PASSWORD_LINK_URL, passwordresetdata)
                    .then(response => {
                        this.$router.push('/passwordresetlinksent')
                        
                    })
                    .catch(error => {
                        if (error.response) {

                        } 
                        
                        else if (error.message) {
                            this.errors.generalErrors.push(this.$t('forgotpasswordview.errors.generalerrors'))
                        }
                    })
            }
            else {
            }
            this.$store.commit('setIsLoading', false);
        }
    }
}
</script>