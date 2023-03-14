<template>
    <section class="my-login-signup-section">
        <div class="page-sign-up">
            <div class="columns">
                <div class="column is-6 is-offset-3">
                    <h1 class="title">
                        {{$t('loginsignupview.signuptitle')}}
                    </h1>
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <!-- general errors -->
                            <div v-if="errors.generalErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.generalErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <!-- username errors-->
                            <div v-if="errors.usernameErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.usernameErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- username -->
                            <label for="">{{ $t('loginsignupview.usernameonly') }}</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" name="username" class="input" :placeholder="$t('loginsignupview.usernameonly')" v-model="username">
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- email -->
                            <label for="">{{ $t('loginsignupview.emailonly') }}</label>
                            <div class="control">
                                <input type="text" name="email" class="input" :placeholder="$t('loginsignupview.emailonly')" v-model="email">
                            </div>
                            <!-- not required fields -->
                            <!-- first_name -->
                            <label for="">{{ $t('loginsignupview.firstnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.firstnamelabel')" v-model="first_name">
                            </div>
                            <!-- lastname -->
                            <label for="">{{ $t('loginsignupview.lastnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.lastnameplaceholder')" v-model="last_name">
                            </div>
                            <!-- fav color -->
                            <label for="">{{ $t('loginsignupview.favoritecolor') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.favoritecolorplaceholder')" v-model="favorite_color">
                            </div>
                            <!-- password errors-->
                            <div v-if="errors.passwordErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.passwordErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>                        
                            </div>
                            <!-- password use click.prevent to prevent form submission action -->
                            <label for="">{{ $t('loginsignupview.password') }}</label>
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
                            <label for="">{{ $t('loginsignupview.reenterpassword') }}</label>
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
                                    <button class="button login-signup-button">{{ $t('loginsignupview.createaccountbutton') }}</button>
                                </div>
                            </div>
                            <p v-if="$i18n.locale === 'en'" class="signup-login-reroute">
                                {{ $t('loginsignupview.login1') }} <a style="color:aqua !important; text-decoration:underline;" href="/login">{{ $t('loginsignupview.login2') }}</a>
                            </p>
                            <p v-else-if="$i18n.locale === 'ja'" >
                                <a class="signup-login-reroute" style=" text-decoration:underline;" href="/login">{{ $t('loginsignupview.login2') }}</a>
                            </p>
                            <h1>
                                {{ $i18n.locale }}
                            </h1>
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
            first_name: '',
            last_name: '',
            password: '',
            re_enter_password: '',
            favorite_color: '',
            errors: {
                generalErrors: [],
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
            this.errors.generalErrors = []
            this.errors.usernameErrors = []
            this.errors.emailErrors = []
            this.errors.passwordErrors = []
            this.errors.re_enter_passwordErrors = []


            // client side validation
            // USERNAME
            // if username is empty
            if (this.username === '') {
                this.errors.usernameErrors.push(this.$t('loginsignupview.usernamereq'))
            }

            // EMAIL
            if (this.email === '') {
                this.errors.emailErrors.push(this.$t('loginsignupview.emailreq'))
            }
            // check if email has @ symbol
            if (!this.email.includes('@')) {
                this.errors.emailErrors.push(this.$t('loginsignupview.email@symbolerror'))

            }

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
            // if password is similiar to username
            if (this.username.includes(this.password) && this.re_enter_password !== '') {
                this.errors.passwordErrors.push(this.$t('loginsignupview.passwordtoosimilartousername'))
            }
            // if password is similiar to username
            if (this.email.includes(this.password) && this.re_enter_password !== '') {
                this.errors.passwordErrors.push(this.$t('loginsignupview.passwordtoosimilartoemail'))
            }



            // if no errors, submit the form and authenticate user
            if (!this.errors.usernameErrors.length && !this.errors.emailErrors.length && !this.errors.passwordErrors.length && !this.errors.re_enter_passwordErrors.length) {
                // var to hold post data
                // keys must be same strings as model fields in backend api
                // values can be named whatever
                const signUpFormData = {
                    username: this.username,
                    email: this.email,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    favorite_color: this.favorite_color,
                    password: this.password,
                }

                // send post data to backend server
                axios
                    .post(process.env.VUE_APP_CREATE_USERS_API_URL, signUpFormData)
                    .then(response => {

                        // add toast message
                        toast({
                            message: this.$t('modals.accountcreated'),
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 3000,
                            position: 'top-center',
                            animate: { in: 'fadeIn', out: 'fadeOut' },
                        })

                        // if account was created, re-route to login 
                        this.$router.push('/login')
                    })
                    // catch the error data, strip it down to category, and push
                    // each error to the appropraite error array
                    
                    .catch(error => {

                        if (error.response) {
                            for (const property in error.response.data) {
                                // disabled server side password validation
                                // if (property === 'password') {
                                //     this.errors.passwordErrors.push(`${error.response.data[property]}`)
                                // }
                                
                                // check if username is already taken
                                if (property === 'username') {
                                    this.errors.usernameErrors.push(this.$t('loginsignupview.usernameexistserror'))
                                }
                                console.log(property)
                                // check if username is already taken
                                if (property === 'email') {
                                    this.errors.emailErrors.push(this.$t('loginsignupview.emailexistserror'))
                                }
                                console.log(property)
                            }

                        } else if (error.message) {
                            this.errors.generalErrors.push(this.$t('loginsignupview.generror'))
                        }
                    })
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