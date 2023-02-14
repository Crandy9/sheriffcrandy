<template>
    <section class="my-login-section">
        <h1 class="title">
            Login cuz!
        </h1>
        <!-- sign up form prevent default action -->
        <form @submit.prevent="submitForm">
            <div class="field">
                <!-- username/email errors-->
                <div class="my-errors" v-if="errors.usernameErrors.length">
                    <p style="color:red" v-for="error in errors.usernameErrors" v-bind:key="error">
                    <span style="color:red !important">*</span> {{ error }}
                    </p>                           
                </div>
                <!-- username/email errors-->
                <div class="my-errors" v-else-if="errors.emailErrors.length">
                    <p style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
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
                <!-- errors need to make them specific for each field-->
                <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <!-- submit form -->
                <div class="field">
                    <div class="control">
                        <button class="button is-dark">Log in</button>
                    </div>
                </div>
                Don't have an account? <a href="/signup">Sign up!</a>
            </div>
        </form>
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
            re_enter_password: '',
            errors: {
                usernameErrors: [],
                emailErrors: [],
                passwordErrors: [],
                re_enter_passwordErrors: [],
            },            
            showPassword: false,
            showReEnterPassword: false,
        }
    },
    methods: {
        submitForm() {
            // reset errors
            this.errors.usernameErrors = []
            this.errors.emailErrors = []
            this.errors.passwordErrors = []
            this.errors.re_enter_passwordErrors = []


            // validate fields
            // USERNAME/EMAIL
            if (this.username_or_email === '') {
                this.errors.usernameErrors.push('Please enter your username or email address to login')
            }
            // PASSWORD
            if (this.password === '') {
                this.errors.passwordErrors.push('Please enter your password')
            }
            // RE-ENTER PASSWORD
            if (this.re_enter_password === '') {
                this.errors.re_enter_passwordErrors.push('Please re-enter your password')
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