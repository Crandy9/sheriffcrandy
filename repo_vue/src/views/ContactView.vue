<template>
    <section class="contact-section">
        <div class="contact-title-div">
            <h3 class="contact-title has-text-white">
                {{$t('contactview.title')}}
            </h3>
        </div>
        <h4 class="is-size-5 has-text-centered">
            <a class="has-text-centered email-link" 
            href="mailto:sheriffcrandy@protonmail.me">
            {{$t('contactview.email')}}<span class="has-text-white">!</span>
            </a>
            
        </h4>
    </section>
</template>

<script>

export default {
    name: 'Contact',
    data() {
        
    },
    mounted() {
      document.title = 'Contact' 
    }
}
</script>