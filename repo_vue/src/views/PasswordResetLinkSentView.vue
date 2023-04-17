<template>
    <section class="my-fpasswordresetlinksent-section">
        <div class="forgot-password-form-container">
            <h5 class="my-forgot-password-title">
                {{$t('forgotpasswordview.passwordresetlinksent')}}
            </h5>
            <p class="my-forgot-password-msg">
                {{$t('forgotpasswordview.passwordresetlinksentmsg')}}
            </p>     
        </div>
    </section>
</template>

<script>

export default {
    name: 'PasswordResetLinkSent',

    data() {
        return {

        }
    },

    mounted () {
        document.title = 'Password Reset Link Sent';

    },

    methods: {
    }
}
</script>