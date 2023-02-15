<template>
    <section class="my-login-signup-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-6 is-offset-3">
                    <h1 class="title">
                        Sign up
                    </h1>
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <!-- username errors-->
                            <div v-if="errors.usernameErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.usernameErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- username -->
                            <label for="">Username</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" name="username" class="input" v-model="username">
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- email -->
                            <label for="">Email Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="email">
                            </div>
                            <!-- firstname -->
                            <label for="">First Name (not required)</label>
                            <div class="control">
                                <input type="text" class="input" v-model="firstname">
                            </div>
                            <!-- lastname -->
                            <label for="">Last Name (not required)</label>
                            <div class="control">
                                <input type="text" class="input" v-model="lastname">
                            </div>
                            <!-- password errors-->
                            <div v-if="errors.passwordErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <!-- password use click.prevent to prevent form submission action -->
                            <label for="">Password</label>
                            <div class="field has-addons">
                                <div class="control is-expanded">
                                    <input v-if="showPassword" type="text" class="input" v-model="password" />
                                    <input v-else type="password" name="password" class="input" v-model="password">
                                </div>
                                <div class="control">
                                    <button class="button" @click.prevent="toggleShowPassword"><span class="icon is-small is-right">
                                        <i class="fas" :class="{ 'fa-eye-slash': showPassword, 'fa-eye': !showPassword }"></i>
                                        </span>
                                    </button>
                                </div>
                            </div>  
                            <!-- re-enter password errors-->
                            <div class="my-errors" v-if="errors.re_enter_passwordErrors.length">
                                <p style="color:red" v-for="error in errors.re_enter_passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                           
                            </div>
                            <!--re-enter password use click.prevent to prevent form submission action -->
                            <label for="">Re-enter Password</label>
                            <div class="field has-addons">
                                <div class="control is-expanded">
                                    <input v-if="showReEnterPassword" type="text" class="input" v-model="re_enter_password" />
                                    <input v-else type="password" class="input" v-model="re_enter_password">
                                </div>
                                <div class="control">
                                    <button class="button" @click.prevent="toggleShowReEnterPassword"><span class="icon is-small is-right">
                                        <i class="fas" :class="{ 'fa-eye-slash': showReEnterPassword, 'fa-eye': !showReEnterPassword }"></i>
                                        </span>
                                    </button>
                                </div>
                            </div>  
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">Create Account</button>
                                </div>
                            </div>
                            <p class="signup-login-reroute">
                                Already have an account? <a style="color:aqua !important; text-decoration:underline;" href="/login">Log in!</a>
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
    name: 'SignUp',

    data() {
        return {
            username: '',
            email: '',
            firstname: null,
            lastname: null,
            password: '',
            re_enter_password: '',
            errors: {
                usernameErrors: [],
                emailErrors: [],
                passwordErrors: [],
                re_enter_passwordErrors: [],
            },
            showPassword: false,
            showReEnterPassword: false,
        };
    },
    computed: {
    },
    methods: {
        submitForm() {
            // reset errors
            this.errors.usernameErrors = []
            this.errors.emailErrors = []
            this.errors.passwordErrors = []
            this.errors.re_enter_passwordErrors = []
            // var to hold post data
            const signUpFormData = {}


            // client side validation
            // USERNAME
            // if username is empty
            if (this.username === '') {
                this.errors.usernameErrors.push('Username is required')
            }
            // EMAIL
            if (this.email === '') {
                this.errors.emailErrors.push('Email is required. Please enter a valid email address')
            }
            // if email is already used

            // PASSWORD
            if (this.password === '') {
                this.errors.passwordErrors.push('Password field cannot be empty. Please enter a strong password')
            }
            // RE-ENTER PASSWORD
            if (this.re_enter_password === '') {
                this.errors.re_enter_passwordErrors.push('Please re-enter your password')
            }

            if (this.password !== this.re_enter_password) {
                this.errors.passwordErrors.push('Passwords do not match')

            }



            // if no errors, submit the form and authenticate user
            if (!this.errors.usernameErrors.length && !this.errors.emailErrors.length && !this.errors.passwordErrors.length && !this.errors.re_enter_passwordErrors.length) {
                console.log('form is valid')

                // if firstname and last name were not entered
                if (this.firstname === null && this.lastname === null) {
                    // send data to server
                    signUpFormData = {
                        username: this.username,
                        email: this.email,
                        password: this.password
                    }

                    // post data to backend server
                }
                // if only firstname was entered
                else if (this.firstname !== null && this.lastname === null) {
                    signUpFormData = {
                        username: this.username,
                        firstname: this.firstname,
                        email: this.email,
                        password: this.password
                    }
                }
                // if only lastname was entered
                else if (this.firstname === null && this.lastname !== null) {
                    signUpFormData = {
                        username: this.username,
                        lastname: this.lastname,
                        email: this.email,
                        password: this.password
                    }
                }
                // if lastname and lastname were entered
                else if (this.firstname !== null && this.lastname !== null) {
                    signUpFormData = {
                        username: this.username,
                        firstname: this.firstname,
                        lastname: this.lastname,
                        email: this.email,
                        password: this.password
                    }
                }
                // send post data to backend server
                // axios.post("")
            }
            else {
                console.log('form is invalid, errors')
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