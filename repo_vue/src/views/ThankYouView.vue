<template>
    <section class="thankyou-section">
        <div class="thank-you-div">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title">
                        Thanks for your purchase!
                    </h1>
                    <p class="has-text-white">
                        A download of your purchase(s) should begin in your browser soon!
                    </p>
                    <p class="has-text-white">
                        If you purchased a single track, the .wav file will be available for download.
                        If you purchased mutliple tracks, flps, or a combination of both, a .zip file
                        containing all files will be generated for download.
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    data() {

    },

    methods: {
        
    },
    mounted () {
        document.title = "Thank you!"
    }
}
</script>