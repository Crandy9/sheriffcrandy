<template>
    <section class="tools-section">
        <div class="tools-title-div">
            <h3 class="tools-title has-text-white">
                {{$t('toolsview.toolsiuse')}}
            </h3>
        </div>
        <h4 class="is-size-3 has-text-centered">
        </h4>
    </section>
</template>

<script>

export default {
    name: 'Tools',
    data() {
        
    },
    mounted() {
      document.title = 'Tools' 
    }
}
</script>