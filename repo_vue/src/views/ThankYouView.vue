<template>
    <section class="thankyou-section">
        <div class="thank-you-div">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title">
                        Thanks for your purchase/download!
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
        return {

        }
    },
    methods: {
        getFiles() {
            // check if this is a single buy now/purchase now file
            if (this.$store.state.isSingleDownload === true) {
                console.log('this is a single purchase/download')
                // check if it is a track or flp single download
                if (this.$store.state.downloadType === 'flp') {
                    console.log('this is an flp download')
                    console.log('flp: ' + this.$store.state.freeDownload)
                    console.log('id: ' + this.$store.state.freeDownloadId)
                }
                else {
                    console.log('this is a track download')
                    console.log('track: ' + this.$store.state.freeDownload)
                    console.log('id: ' + this.$store.state.freeDownloadId)
                }
            }
            else {
                console.log('this is a multi-file download/purchase')
            }
        }
    },
    // get the flps/tracks/free flps/free tracks from backend
    created() {
        this.getFiles()
    },

    mounted () {
        document.title = "Thank you!";
    },

}
</script>