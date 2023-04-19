<template>
    <section class="my-reset-password-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-6 is-offset-3">
                    <h5 class="title my-reset-pass-title">
                        {{ $t('forgotpasswordview.changepasswordtitle') }}                    
                    </h5>
                    <p class="my-reset-pass-msg">
                        {{ $t('forgotpasswordview.changepasswordmsg') }}
                    </p>
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <!-- general errors -->
                            <div v-if="errors.generalErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.generalErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <!-- password errors-->
                            <div v-if="errors.passwordErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <!-- password use click.prevent to prevent form submission action -->
                            <label class="my-label" for="">{{ $t('loginsignupview.password') }}</label>
                            <div class="field has-addons my-password-field">
                                <div class="control is-expanded input-container">
                                    <!-- show password, type has to be text -->
                                    <input v-if="showPassword" type="text" class="input" v-model="password" />
                                    <!-- hide password, type is password -->
                                    <input v-else type="password" class="input" v-model="password">
                                    <span @click.prevent="toggleShowPassword" class="icon is-small is-right my-eye-icon">
                                        <i class="fas" :class="{ 'fa-eye-slash': showPassword, 'fa-eye': !showPassword }"></i>
                                    </span>
                                </div>
                            </div>
                            <!-- re-enter password errors-->
                            <div class="my-errors" v-if="errors.re_enter_passwordErrors.length">
                                <p style="color:red" v-for="error in errors.re_enter_passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!--re-enter password use click.prevent to prevent form submission action -->
                            <label class="my-label" for="">{{ $t('loginsignupview.reenterpassword') }}</label>
                            <div class="field has-addons my-password-field">
                                <div class="control is-expanded input-container">
                                    <!-- show password, type has to be text -->
                                    <input v-if="showReEnterPassword" type="text" class="input" v-model="re_enter_password" />
                                    <!-- hide password, type is password -->
                                    <input v-else type="password" class="input" v-model="re_enter_password">
                                    <span @click.prevent="toggleShowReEnterPassword" class="icon is-small is-right my-eye-icon">
                                        <i class="fas" :class="{ 'fa-eye-slash': showReEnterPassword, 'fa-eye': !showReEnterPassword }"></i>
                                    </span>
                                </div>
                            </div> 
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">{{ $t('forgotpasswordview.changepasswordtitle') }}</button>
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
    name: 'ResetPassword',

    data() {
        return {
            password: '',
            re_enter_password: '',
            errors: {
                generalErrors: [],
                passwordErrors: [],
                re_enter_passwordErrors: [],
            },
            showPassword: false,
            showReEnterPassword: false, 
        }
    },

    mounted () {
        document.title = 'Set New Password';

    },

    methods: {

        submitForm() {
            // reset errors
            this.errors.generalErrors = []
            this.errors.passwordErrors = []
            this.errors.re_enter_passwordErrors = []


            // client side validation
            // PASSWORD
            if (this.password === '') {
                this.errors.passwordErrors.push(this.$t('loginsignupview.noemptypass'))
            }

            // RE-ENTER PASSWORD
            if (this.re_enter_password === '') {
                this.errors.re_enter_passwordErrors.push(this.$t('loginsignupview.blankreenterpassword'))
            }

            // if passwords don't match
            if (this.password !== this.re_enter_password) {
                this.errors.passwordErrors.push(this.$t('loginsignupview.passwordsdontmatch'))
            }


            // if no errors, submit the form and authenticate user
            if (!this.errors.passwordErrors.length && !this.errors.re_enter_passwordErrors.length) {

                // Get the current URL
                const url = window.location.href;
                // extract token and uidb64 from URL which is used to identify the current user
                // define a regex that matches the string "/resetpassword/" 
                // followed by one or more non-slash characters (captured as the first group), 
                // followed by another slash and one or more non-slash characters (captured as the second group).
                const regex = /\/resetpassword\/([^\/]+)\/([^\/]+)/;

                // search for a match in the URL against the regex which should always return resetpassword/uid/token
                const match = url.match(regex);
                const uidb64 = match[1];
                const token = match[2];

                // var to hold post data
                // keys must be same strings as model fields in backend api
                // values can be named whatever
                const new_reset_pass_data = {
                    password: this.password,
                    uidb64: uidb64,
                    token: token
                }

                // send post data to backend server
                axios
                    .post(process.env.VUE_APP_RESET_USER_PASSWORD_URL, new_reset_pass_data)
                    .then(response => {

                        // add toast message
                        toast({
                            message: this.$t('modals.passwordreset'),
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'center',
                            animate: { in: 'fadeIn', out: 'fadeOut' },
                        })

                        // if account was created, re-route to login 
                        this.$router.push('/login')
                    })
                    // catch the error data, strip it down to category, and push
                    // each error to the appropraite error array
                    
                    .catch(error => {
                            this.errors.generalErrors.push(this.$t('loginsignupview.generror'))
                    })
            }
            else {
            }

        },












        toggleShowPassword() {
            this.showPassword = !this.showPassword;
        },
        toggleShowReEnterPassword() {
            this.showReEnterPassword = !this.showReEnterPassword;
        },
    }
}
</script>