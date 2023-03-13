<template>
    <section class="my-login-signup-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-6 is-offset-3">
                    <h1 class="title">
                        {{$t('loginsignupview.logintitle')}}
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
                            <div class="my-errors" v-if="errors.usernameOrEmailErrors.length">
                                <p style="color:red" v-for="error in errors.usernameOrEmailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!-- users can enter their email address or username to login -->
                            <label for="">{{$t('loginsignupview.username')}}</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" class="input" v-model="username_or_email">
                            </div>
                            <!-- password errors-->
                            <div class="my-errors" v-if="errors.passwordErrors.length">
                                <p style="color:red" v-for="error in errors.passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!-- password -->
                            <label for="">{{$t('loginsignupview.password')}}</label>
                            <div class="field has-addons my-password-field">
                                <div class="control is-expanded">
                                    <input v-if="showPassword" type="text" class="input" v-model="password" />
                                    <input v-else type="password" class="input" v-model="password">
                                </div>
                                <div class="control">
                                    <button class="button" @click.prevent="toggleShowPassword"><span class="icon is-small is-right">
                                        <i class="fas" :class="{ 'fa-eye-slash': showPassword, 'fa-eye': !showPassword }"></i>
                                        </span>
                                    </button>
                                </div>
                            </div>
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">{{$t('loginsignupview.logintitle')}}</button>
                                </div>
                                <p class="forgot-password-link">
                                    <a style="color:aqua !important; text-decoration: underline;" href="">{{$t('loginsignupview.forgotpassword')}}</a>
                                </p>  
                            </div>
                            <p v-if="$store.state.region === 'US'" class="signup-login-reroute">
                                {{$t('loginsignupview.signup1')}} <a style="color:aqua !important; text-decoration: underline;" href="/signup">{{$t('loginsignupview.signup2')}}</a>
                            </p>
                            <p v-else-if="$store.state.region === 'JA'" >
                                <a class="signup-login-reroute" style="text-decoration: underline;" href="/signup">{{$t('loginsignupview.signup2')}}</a>
                            </p>
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
    name: 'LogIn',

    data() {
        return {
            username_or_email: '',
            password: '',
            errors: {
                generalErrors: [],
                usernameOrEmailErrors: [],
                passwordErrors: [],
            },            
            showPassword: false,
        }
    },
    methods: {
        submitForm() {
            // reset errors
            this.errors.generalErrors = []
            this.errors.usernameOrEmailErrors = []
            this.errors.passwordErrors = []


            // validate fields
            // USERNAME/EMAIL
            if (this.username_or_email === '') {
                this.errors.usernameOrEmailErrors.push(this.$t('loginsignupview.errors.usernameemailerrors'))
            }
            // PASSWORD
            if (this.password === '') {
                this.errors.passwordErrors.push(this.$t('loginsignupview.errors.passworderrors'))
            }
            // if no errors, submit the form and authenticate user
            if (!this.errors.usernameOrEmailErrors.length && !this.errors.passwordErrors.length ) {
                // var to hold post data
                // keys must be same strings as model fields in backend api user model
                // values can be named whatever
                const loginFormData = {
                    username: this.username_or_email,
                    password: this.password,
                }

                // send post data to backend server
                axios
                    .post(process.env.VUE_APP_AUTHENTICATE_USERS_API_URL, loginFormData)
                    .then(response => {

                        console.log(JSON.stringify(response))
                        // set auth token
                        const sf_auth_bearer = response.data.auth_token
                        // set token in store which sets is_authenticated var to true
                        this.$store.commit('setToken', sf_auth_bearer)
                        // setting token in axios header
                        axios.defaults.headers.common['Authorization'] = 'Token ' + sf_auth_bearer
                        // set token in localstorage
                        localStorage.setItem("sf_auth_bearer", sf_auth_bearer)

                        // get user's username
                        // const currentUsername = response.data.username

                        // add toast message
                        toast({
                            message: this.$t('modals.welcomeback') + ' ' + this.username_or_email + this.$t('modals.welcomeback2') +'!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3000,
                            position: 'top-center',
                            animate: { in: 'fadeIn', out: 'fadeOut' },
                        })
                        // check if there is a pending route to be redirected to
                        // else go to home
                        const toPath = this.$route.query.to || '/'
                        // re-route to homepage
                        this.$router.push(toPath)
                    })
                    .catch(error => {
                        if (error.response) {
                            this.errors.generalErrors.push(this.$t('loginsignupview.errors.invalidusernamepassword'))
                        } 
                        
                        else if (error.message) {
                            this.errors.generalErrors.push(this.$t('loginsignupview.errors.generalerrors'))
                            console.log("Didn't work bic boii: " + JSON.stringify(error.response.data))
                        }
                    })
            }
            else {
                console.log('form is invalid')
            }
        },
        toggleShowPassword() {
            this.showPassword = !this.showPassword;
        },
    }
}
</script>