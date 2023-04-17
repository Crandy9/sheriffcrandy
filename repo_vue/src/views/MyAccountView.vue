<template>
    <div class="my-account-container">
        <div class="my-account-header">
            <h1 class="my-account-title">
                Account Details
            </h1>
        </div>
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <div class="my-account-info">
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm" v-bind:readonly="isReadOnly">
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
                            <!-- real-time username validation -->
                            <p class="my-errors" style="color:red" v-if="!usernameAvailable && !isUsernameEmpty ">{{ $t('loginsignupview.usernamenotavail') }}</p>
                            <p class="my-errors" style="color:green" v-else-if="usernameAvailable && !isUsernameEmpty ">{{ $t('loginsignupview.usernameavail') }}</p>
                            <!-- username -->
                            <label class="my-label" for="">{{ $t('loginsignupview.usernameonly') }}</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" v-model="username" name="username" @input="checkUsername" class="input" :placeholder="$t('loginsignupview.usernameonly')">
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- real-time email validation -->
                            <p class="my-errors" style="color:red" v-if="!emailAvailable && !isEmailEmpty">{{ $t('loginsignupview.emailnotavail') }}</p>
                            <p class="my-errors" style="color:green" v-else-if="emailAvailable && !isEmailEmpty">{{ $t('loginsignupview.emailavail') }}</p>
                            <!-- email -->
                            <label class="my-label" for="">{{ $t('loginsignupview.emailonly') }}</label>
                            <div class="control">
                                <input type="text" v-model="email" name="email" @input="checkEmail" class="input" :placeholder="$t('loginsignupview.emailonly')">
                            </div>
                            <!-- not required fields -->
                            <!-- first_name -->
                            <label class="my-label" for="">{{ $t('loginsignupview.firstnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.firstnamelabel')" v-model="first_name">
                            </div>
                            <!-- lastname -->
                            <label class="my-label" for="">{{ $t('loginsignupview.lastnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.lastnameplaceholder')" v-model="last_name">
                            </div>
                            <!-- fav color -->
                            <label class="my-label" for="">{{ $t('loginsignupview.favoritecolor') }}</label>
                            <div class="control">
                                <input type="text" class="input" :placeholder="$t('loginsignupview.favoritecolorplaceholder')" v-model="favorite_color">
                            </div>
                            <!-- submit form -->
                            <div class="field">
                                <div class="control">
                                    <button class="button login-signup-button">{{ $t('loginsignupview.createaccountbutton') }}</button>
                                </div>
                            </div>
                            <p v-if="$store.state.language === 'en'" class="signup-login-reroute">
                                {{ $t('loginsignupview.login1') }} <a style="color:aqua !important; text-decoration:underline;" href="/login">{{ $t('loginsignupview.login2') }}</a>
                            </p>
                            <p v-else-if="$store.state.language === 'ja'" >
                                <a class="signup-login-reroute" style="text-decoration:underline;" href="/login">{{ $t('loginsignupview.login1') }}</a>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
// for pop up notifying user about added item to cart
import { toast } from 'bulma-toast'

export default {

    data() {
        return {
            userdata: [],
            timer: '',
            timerRunning: '',
            // 1 second
            api_post_wait_duration: 400,
            username: '',
            usernameAvailable: true,
            email: '',
            emailAvailable: true,
            first_name: '',
            last_name: '',
            favorite_color: '',
            errors: {
                generalErrors: [],
                usernameErrors: [],
                emailErrors: []
            },
            isReadOnly: true
        }
    },

    mounted() {
        document.title = 'My Account';
        this.getUserData();
    },

    methods: {

        // edit account info
        toggleReadOnly() {
            this.isReadOnly = !this.isReadOnly;
        },
        // dynamically check username validity
        checkUsername() {
            // clear the timeout if it is still running
            if (this.timer) {
                clearTimeout(this.timer);
                this.timerRunning = false;
            }
            if (this.username.trim().length > 0) {
                this.timer = setTimeout(() => {
                    this.timerRunning = true;
                    try {
                        axios.get(process.env.VUE_APP_CHECK_USERNAME_API_URL + `${this.username}`)
                        .then(response => {
                            const data = response.data;
                            this.usernameAvailable = data.available;
                            this.timerRunning = false;
                        })
                        .catch(error => {
                            console.log(error);
                        })
                    }
                    catch(error) {
                        console.log(error)
                        }   
                }, this.api_post_wait_duration)
            }
        } ,

        checkEmail() {
            // clear the timeout if it is still running
            if (this.timer) {
                clearTimeout(this.timer);
            }
            if (this.email.trim().length > 0) {
                this.timer = setTimeout(() => {
                    try {
                        axios.get(process.env.VUE_APP_CHECK_EMAIL_API_URL + `${this.email}`)
                        .then(response => {
                            const data = response.data;
                            this.emailAvailable = data.available;
                        })
                        .catch(error => {
                            console.log(error);
                        })
                    }
                    catch(error) {
                        console.log(error)
                        }   
                }, this.api_post_wait_duration)
            }
        },
        getUserData() {
            const sf_auth_bearer = this.$store.state.sf_auth_bearer
            axios.get(process.env.VUE_APP_GET_USER_ACCOUNT_DATA_URL, {headers: { 'Authorization': `Token ${sf_auth_bearer}`}})
            .then(response => {
                this.userdata = response.data
                // populate the fields
                this.username = this.userdata.username
                this.email = this.userdata.email
                this.first_name = this.userdata.first_name
                this.last_name = this.userdata.last_name
                this.favorite_color = this.userdata.favorite_color

                })
                .catch(error => {
                // handle error
                console.log(error);
            });
        }
    },
    computed: {
        isUsernameEmpty() {
            return this.username.trim().length === 0;
        },

        isEmailEmpty() {
            return this.email.trim().length === 0;
        },
    }

}
</script>