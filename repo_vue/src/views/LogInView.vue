<template>
    <section class="my-login-signup-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-6 is-offset-3">
                    <h1 class="title">
                        Login
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
                            <label for="">Username/Email Address</label>
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
                            <label for="">Password</label>
                            <div class="field has-addons">
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
                            <!-- errors need to make them specific for each field-->
                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">Log in</button>
                                </div>
                            </div>
                            <p class="signup-login-reroute">
                                Don't have an account? <a style="color:aqua !important; text-decoration: underline;" href="/signup">Sign up!</a>
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
                this.errors.usernameOrEmailErrors.push('Please enter your username or email address to login')
            }
            // PASSWORD
            if (this.password === '') {
                this.errors.passwordErrors.push('Please enter your password')
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
                        const token = response.data.auth_token
                        // set token in store which sets is_authenticated var to true
                        this.$store.commit('setToken', token)
                        // setting token in axios header
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        // set token in localstorage
                        localStorage.setItem("sf_auth_bearer", token)

                        // get user's username
                        // const currentUsername = response.data.username

                        // add toast message
                        toast({
                            message: 'Welcome back ' + this.username_or_email + '!',
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
                            this.errors.generalErrors.push("username and/or password is invalid")
                        } 
                        
                        else if (error.message) {
                            this.errors.generalErrors.push('Oops! Something went wrong, please try again later.')
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