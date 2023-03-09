<template>
    <section class="bio-section">
        <div class="bio-title-div">
            <h3 class="bio-title has-text-white">
                {{$t('bioview.biotitle')}}
            </h3>
        </div>
        <h4 class="is-size-3 has-text-centered">
        </h4>
    </section>
</template>
  

<script>

export default {
    name: 'Bio',
    data() {
        
    },
    mounted() {
      document.title = 'Bio' 
    }
}
</script>