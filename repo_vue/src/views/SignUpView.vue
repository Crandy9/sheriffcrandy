<template>
    <section class="my-signup-section">
        <h1 class="title">
            Sign up cuz!
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
                    <input type="text" class="input" v-model="username">
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
                <!-- password errors-->
                <div v-if="errors.passwordErrors.length">
                    <p class="my-errors" style="color:red" v-for="error in errors.passwordErrors" v-bind:key="error">
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
                        <button class="button" @click="toggleShowPassword"><span class="icon is-small is-right">
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
                <!--re-enter password -->
                <label for="">Re-enter Password</label>
                <div class="field has-addons">
                    <div class="control is-expanded">
                        <input v-if="showReEnterPassword" type="text" class="input" v-model="re_enter_password" />
                        <input v-else type="password" class="input" v-model="re_enter_password">
                    </div>
                    <div class="control">
                        <button class="button" @click="toggleShowReEnterPassword"><span class="icon is-small is-right">
                            <i class="fas" :class="{ 'fa-eye-slash': showReEnterPassword, 'fa-eye': !showReEnterPassword }"></i>
                            </span>
                        </button>
                    </div>
                </div>  
                <!-- submit form -->
                <div class="field">
                    <div class="control">
                        <button class="button is-dark">Sign Up</button>
                    </div>
                </div>
                Already have an account? <a href="/login">Log in!</a>
            </div>
        </form>
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


            // validate fields
            // USERNAME
            if (this.username === '') {
                this.errors.usernameErrors.push('Username is required')
            }
            // EMAIL
            if (this.email === '') {
                this.errors.emailErrors.push('Email is required. Please enter a valid email address')
            }
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