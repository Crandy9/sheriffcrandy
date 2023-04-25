<template>
    <div class="my-account-container">
        <div class="my-account-header">
            <h1 class="my-account-title">
                Account Details
            </h1>
        </div>
        <!-- enable form to edit -->
        <button 
            :disabled="formEnabled" 
            class="button edit-account-button" 
            @click="toggleFormFields"> 
            {{ $t('myaccountview.editaccount') }}
        </button>
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <div class="my-account-info">
                    <!-- sign up form prevent default action -->
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <!-- pfp (not required) -->
                            <div class="my-account-pfp-container">
                                <input
                                    type="file"
                                    ref="fileInput"
                                    @change="handleFileUpload"
                                    style="display: none;">
                                <!-- if the user hasn't uplopaded a pfp yet -->
                                <div v-if="!$store.state.profile_pic_background_img"
                                    @click="openFileInput"
                                    class="my-account-upload-pfp">
                                    <div class="my-account-pfp-placeholder">
                                        {{ $t('myaccountview.uploadpfp') }}
                                        <i class="fas fa-camera"></i>
                                    </div>
                                </div>
                                <div v-else
                                    @click="openFileInput"
                                    class="my-account-upload-pfp" 
                                    :style="{ backgroundImage: `url(${$store.state.profile_pic_background_img})` }">
                                </div>
                            </div>
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
                            <label class="my-label" for="">{{ $t('myaccountview.usernameonly') }}</label>
                            <div class="control">
                                <!-- v-model connects the data var defined below -->
                                <input type="text" v-model="username" :class="{ 'readonly': !formEnabled }" :readonly="!formEnabled" name="username" class="input" :placeholder="$t('myaccountview.usernameonly')">
                            </div>
                            <!-- email errors-->
                            <div v-if="errors.emailErrors.length">
                                <p class="my-errors" style="color:red" v-for="error in errors.emailErrors" v-bind:key="error">
                                <span style="color:red !important">*</span> {{ error }}
                                </p>
                            </div>
                            <!-- email -->
                            <label class="my-label" for="">{{ $t('myaccountview.emailonly') }}</label>
                            <div class="control">
                                <input type="text" v-model="email" :class="{ 'readonly': !formEnabled }" :readonly="!formEnabled" name="email" class="input" :placeholder="$t('myaccountview.emailonly')">
                            </div>
                            <!-- not required fields -->
                            <!-- first_name -->
                            <label class="my-label" for="">{{ $t('myaccountview.firstnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :class="{ 'readonly': !formEnabled }" :readonly="!formEnabled" :placeholder="$t('myaccountview.firstnamelabel')" v-model="first_name">
                            </div>
                            <!-- lastname -->
                            <label class="my-label" for="">{{ $t('myaccountview.lastnamelabel') }}</label>
                            <div class="control">
                                <input type="text" class="input" :class="{ 'readonly': !formEnabled }" :readonly="!formEnabled" :placeholder="$t('myaccountview.lastnameplaceholder')" v-model="last_name">
                            </div>
                            <!-- fav color -->
                            <label class="my-label" for="">{{ $t('myaccountview.favoritecolor') }}</label>
                            <div class="control">
                                <input type="text" class="input" :class="{ 'readonly': !formEnabled }" :readonly="!formEnabled" :placeholder="$t('myaccountview.favoritecolorplaceholder')" v-model="favorite_color">
                            </div>
                            <div class="my-account-button-container">
                                <!-- submit form -->
                                <div class="field">
                                    <div class="control">
                                        <button :disabled="!formEnabled" class="button update-account-button">{{ $t('myaccountview.updateaccount') }}</button>
                                    </div>
                                </div>
                                <!-- delete account button -->
                                <div class="field">
                                    <div class="control">
                                        <button @click.prevent="showDeleteModal = !showDeleteModal" class="button delete-account-button">{{ $t('myaccountview.deleteaccount') }}</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- modal -->
    <Transition>
    <div v-if="showDeleteModal" id="my-modal-id" class="modal" v-bind:class="{'is-active':showDeleteModal}">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title last-chance-msg">{{ $t('myaccountview.areyousureyouwanttodelete') }}</p>
                <!-- close button -->
                <button @click="showDeleteModal = false" class="delete delete-account-modal-close" aria-label="close"></button>
            </header>
            <footer class="modal-card-foot">
            <div>
                <!-- delete account -->
                <button @click='deleteUserAccount(), showDeleteModal = false' class="button delete-account-button">{{ $t('myaccountview.deleteaccount') }}</button>
                <!-- cancel -->
                <button @click="showDeleteModal = false" class="button delete-account-final-cancel">{{ $t('myaccountview.canceldeleteaccount') }}</button>
            </div>
            </footer>
        </div>
    </div>
    </Transition>
    <!-- end modal -->
</template>


<style scoped>
/* CSS styles for the read-only appearance */
.readonly {
    background-color: #f8f8f8; /* Use desired background color for read-only fields */
    color: #777;
}

</style>



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
            profile_pic_file: '',
            errors: {
                generalErrors: [],
                usernameErrors: [],
                emailErrors: []
            },
            formEnabled : false,
            showDeleteModal: false
        }
    },

    mounted() {
        document.title = 'My Account';
        this.getUserData();
    },

    methods: {

        // set profile pic and resize it for backend
        handleFileUpload(event) {

            this.errors.generalErrors = []
            const allowedImageTypes = ['image/jpeg', 'image/png', 'image/gif']; // List of allowed image MIME types

            const file = event.target.files[0];

            if (!allowedImageTypes.includes(file.type)) {
                this.errors.generalErrors.push(this.$t('loginsignupview.invalidimagefile'))
                return
            }
            this.errors.generalErrors = []

            if (file.size <= 2621440) {
                const imgURL = URL.createObjectURL(file);
                this.$store.state.profile_pic_background_img = imgURL;
                this.profile_pic_file = file
                return
            }

            const reader = new FileReader();
            reader.onload = (e) => {
                const imageDataUrl = e.target.result;

                // Create an image element
                const img = new Image();
                img.src = imageDataUrl;

                // Once the image is loaded, resize it using a canvas
                img.onload = () => {
                    const canvas = document.createElement('canvas');
                    const ctx = canvas.getContext('2d');

                    // Calculate the new dimensions based on the desired file size
                    const maxSize = 2621440; // 2.5 MB
                    const scaleFactor = Math.sqrt(maxSize / (img.width * img.height));
                    const newWidth = Math.floor(img.width * scaleFactor);
                    const newHeight = Math.floor(img.height * scaleFactor);

                    // Set the canvas size to the new dimensions
                    canvas.width = newWidth;
                    canvas.height = newHeight;

                    // Draw the image onto the canvas with the new dimensions
                    ctx.drawImage(img, 0, 0, newWidth, newHeight);

                    // Convert the canvas content to a Blob object
                    canvas.toBlob((blob) => {
                        // Access the size property of the Blob object to get the new file size

                        // Log the new file size
                        
                        // Set the resized image data URL as the background image of the div
                        const resizedImageDataUrl = URL.createObjectURL(blob);
                        this.$store.state.profile_pic_background_img = resizedImageDataUrl;

                        const resizedFile = new File([blob], file.name);
                        this.profile_pic_file = resizedFile;

                    }, file.type);

                };
            };
            reader.readAsDataURL(file);
            this.formEnabled = true;
        },


        // trigger filechooser without ugly default HTML filechooser button
        openFileInput() {
            this.$refs.fileInput.click();
            this.formEnabled = true
        },

        // submit account update info 
        submitForm() {
            // reset errors
            this.errors.generalErrors = []
            this.errors.usernameErrors = []
            this.errors.emailErrors = []


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


            // if no errors, submit the form and authenticate user
            if (!this.errors.usernameErrors.length && !this.errors.emailErrors.length) {
                // var to hold post data
                // keys must be same strings as model fields in backend api
                // values can be named whatever
                const updateAccountData = {
                    username: this.username,
                    email: this.email,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    favorite_color: this.favorite_color,
                    profile_pic: this.profile_pic_file
                }

                // send post data to backend server
                axios.post(process.env.VUE_APP_UPDATE_USER_ACCOUNT_API_URL, updateAccountData, 

                    // header needed to send text and file data
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }).then(response => {
                        // add toast message
                        toast({
                            message: this.$t('myaccountview.accountupdated'),
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'center',
                            animate: { in: 'fadeIn', out: 'fadeOut' },
                        })
                        this.formEnabled = false
                        this.$router.push('/myaccount')
                    })
                    // catch the error data, strip it down to category, and push
                    // each error to the appropraite error array
                    .catch(error => {
                        if (error.response && error.response.data) {
                            // Handle username or email 
                            const errors = error.response.data;
                            if (errors.username) {
                                if (errors.username[0] == 'Username already exists.') {
                                    this.errors.usernameErrors.push(this.$t('myaccountview.usernameexistserror'))
                                }
                                // Display the error message to the user or perform other error handling tasks
                            }
                            if (errors.email) {
                                if (errors.email[0] == 'Email already exists.') {
                                    this.errors.emailErrors.push(this.$t('myaccountview.emailexistserror'))
                                }                                
                                // Display the error message to the user or perform other error handling tasks
                            }
                        } else {
                            console.log('error');
                            // Handle other types of errors
                            console.log(error);
                        }
                    });
            }

        },

        // edit account info
        toggleFormFields() {
            this.formEnabled  = !this.formEnabled ;
        },

        // delete user account
        deleteUserAccount() {
            const sf_auth_bearer = this.$store.state.sf_auth_bearer
            axios.post(process.env.VUE_APP_DELETE_USER_ACCOUNT_DATA_URL, {headers: { 'Authorization': `Token ${sf_auth_bearer}`}})
            .then(response => {
                
                axios.defaults.headers.common["Authorization"] = ""
                localStorage.removeItem('sf_auth_bearer')
                this.$store.commit('removeToken')
                this.$store.commit('clearCart')
                this.$store.commit('clearPurchasedTrackList')
                this.$store.state.profile_pic_background_img = ''
                toast({
                    message: this.$t('myaccountview.accountdeleted'),
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'center',
                    animate: { in: 'fadeIn', out: 'fadeOut' },
                })
                this.formEnabled = false
                this.$router.push('/')
                })
                .catch(error => {
                // handle error
                console.log(error);
            });
        },

        // get user account details and populate form
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
                this.$store.state.profile_pic_background_img = this.userdata.get_profile_pic
                })
                .catch(error => {
                // handle error
            });
        }
    },
    computed: {
    }

}
</script>