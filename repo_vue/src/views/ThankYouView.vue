<template>
    <section class="thankyou-section">
        <div class="thank-you-div">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title">
                        {{ $t('thankyouview.title') }}
                    </h1>
                    <p class="has-text-white">
                        {{ $t('thankyouview.waitmsg') }}
                    </p>
                    <p class="has-text-white">
                        {{ $t('thankyouview.aboutdownload') }}
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            isSingleTrack: false,
            isSingleFlp: false,
            isMultFile: false,
        }
    },
    methods: {

        getFiles() {
            if (this.$store.state.downloadableItems.length === 0) {
            }
            // single download from either the track view, cart view, or flp view
            else if (this.$store.state.downloadableItems.length === 1) {
                // single track download from track view
                if (this.$store.state.isSingleTrackDownload === true && this.$store.state.downloadType === 'fromMusicView') {
                    this.isSingleTrack = true;
                    this.isSingleFlp = false;
                    this.isMultFile = false;
                    this.downloadWithAxios(this.$store.state.downloadableItems[0].track, this.$store.state.downloadableItems[0].title)
                    this.$store.state.downloadableItems = []
                }
                // single flp download from flp view
                else if (this.$store.state.isSingleFlpDownload === true && this.$store.state.downloadType === 'fromFlpView') {
                    this.isSingleTrack = false;
                    this.isSingleFlp = true;
                    this.isMultFile = false;
                    this.downloadWithAxios(this.$store.state.downloadableItems[0].flp_zip, this.$store.state.downloadableItems[0].flp_name)
                    this.$store.state.downloadableItems = []
                }
                // else it is a single cart download item
                else {
                    // check if this is a single track item being bought from the cart
                    if (this.$store.state.downloadableItems.some(obj => obj.hasOwnProperty('track'))) {
                        this.isSingleTrack = true;
                        this.isSingleFlp = false;
                        this.isMultFile = false;

                        this.downloadWithAxios(this.$store.state.downloadableItems[0].track, this.$store.state.downloadableItems[0].title)
                        this.$store.state.downloadableItems = []
                    }
                    else if (this.$store.state.downloadableItems.some(obj => obj.hasOwnProperty('flp_zip'))) {
                        this.isSingleTrack = false;
                        this.isSingleFlp = true;
                        this.isMultFile = false;
                        for (var i = 0; i < this.$store.state.downloadableItems.length; i++) {

                            this.downloadWithAxios(this.$store.state.downloadableItems[0].flp_zip, this.$store.state.downloadableItems[0].flp_name)
                        }
                        this.$store.state.downloadableItems = []
                    }
                }
            }
            // else this is a multifile download consisting of free and paid tracks and flps from the cart
            // zip file download is handled in the then block of CartView
            else {
                // only thing to do is to empty the cart
                this.$store.commit('clearCart')
            }
        },

        downloadWithAxios(url, title) {
            axios({
                method: 'get',
                url,
                responseType: 'arraybuffer',
            }).then((response) =>{

                // single track download/purchase
                if (this.isSingleTrack === true) {
                    this.forceDownloadSingleTrack(response, title)
                }
                // single flp download/purchase
                else if (this.isSingleFlp === true) {
                    this.forceDownloadSingleFlp(response, title)
                }

            }).catch((error) =>  console.log(error))
            
        },
        forceDownloadSingleTrack(response, title) {
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href= url
            // if it is a single wav file
            link.setAttribute('download', title + '.wav')
            // else for multiple wav files, or single flp or multiple flp files, or combinations of both
            // it should be zipped
            document.body.appendChild(link)
            link.click()
        },
        forceDownloadSingleFlp(response, title) {
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href= url
            // if it is a single wav file
            link.setAttribute('download', title + '.zip')
            // else for multiple wav files, or single flp or multiple flp files, or combinations of both
            // it should be zipped
            document.body.appendChild(link)
            link.click()
        },

    },
    created() {
    },

    mounted () {
        document.title = "Thank you!";
        this.getFiles()
    },
}
</script>