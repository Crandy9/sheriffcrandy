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
import axios from 'axios'

export default {
    data() {
        return {
            isSingleTrack: false,
            isSingleFlp: false,
            isMultFile: false,
            multipleFileUrls: [],

        }
    },
    methods: {
        downloadWithAxios(url, title) {
            axios({
                method: 'get',
                url,
                responseType: 'arraybuffer',
            }).then((response) =>{

                // single track download/purchase
                if (this.isSingleTrack === true) {
                    console.log('In downloadWithAxios method. This is a single track. Going to forceDownloadSingleTrack method')
                    this.forceDownloadSingleTrack(response, title)
                }
                // single flp download/purchase
                else if (this.isSingleFlp === true) {
                    this.forceDownloadSingleFlp(response, title)
                }

            }).catch((error) =>  console.log(error))
            
        },
        forceDownloadSingleTrack(response, title) {
            console.log('In forceDownloadSingleTrack method. This is a single track')
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
        getFiles() {
            if (this.$store.state.downloadableItems.length === 0) {
                console.log('no items to download')
            }
            // check if this is a single buy now/purchase now not from cart view
            else if (this.$store.state.isSingleDownload === true) {
                // check if it is a track or flp single download
                if (this.$store.state.downloadType === 'flp') {
                    this.isSingleTrack = false;
                    this.isSingleFlp = true;
                    this.isMultFile = false;
                    console.log('this is an flp download/purchase from the FLP view')
                    // automatically download on page render
                    this.downloadWithAxios(this.$store.state.downloadableItems[0].flp_zip, this.$store.state.downloadableItems[0].flp_name)
                    // clear array
                    this.$store.state.downloadableItems = []
                }
                else {
                    console.log('this is a track download/purchase from the TRACK view')
                    this.isSingleTrack = true;
                    this.isSingleFlp = false;
                    this.isMultFile = false;
                    // automatically download on page render
                    this.downloadWithAxios(this.$store.state.downloadableItems[0].track, this.$store.state.downloadableItems[0].title)
                    // clear array
                    this.$store.state.downloadableItems = []
                }
            }
            else {

                if (this.$store.state.downloadableItems.length === 1) {
                    console.log('this is a cart download/purchase')
                    // check if this is a single track item being bought from the cart
                    if (this.$store.state.downloadableItems.some(obj => obj.hasOwnProperty('track'))) {
                        this.isSingleTrack = true;
                        this.isSingleFlp = false;
                        this.isMultFile = false;

                        console.log('single TRACK download/purchase from cart')
                        this.downloadWithAxios(this.$store.state.downloadableItems[0].track, this.$store.state.downloadableItems[0].title)
                        this.$store.state.downloadableItems = []
                    }
                    else if (this.$store.state.downloadableItems.some(obj => obj.hasOwnProperty('flp_zip'))) {
                        console.log('single FLP download/purchase from cart')
                        this.isSingleTrack = false;
                        this.isSingleFlp = true;
                        this.isMultFile = false;
                        for (var i = 0; i < this.$store.state.downloadableItems.length; i++) {
                            console.log(this.$store.state.downloadableItems[0].flp_zip)
                            console.log(this.$store.state.downloadableItems[0].flp_name)
                            this.downloadWithAxios(this.$store.state.downloadableItems[0].flp_zip, this.$store.state.downloadableItems[0].flp_name)
                        }
                        this.$store.state.downloadableItems = []

                    }
                }
                // this is a multi-file zip download
                else {
                    this.isSingleTrack = false;
                    this.isSingleFlp = false;
                    this.isMultFile = true;
                    console.log('MULTI FILE DOWNLOAD')

                    for (var i = 0; i < this.$store.state.downloadableItems.length; i++) {

                        // if this item in the list is a track
                        // if (this.$store.state.downloadableItems[i].some(obj => obj.hasOwnProperty('track'))) {
                        if ('track' in this.$store.state.downloadableItems[i]) {
                            console.log('this is a track item')
                            this.downloadMultiFilesWithAxios(this.$store.state.downloadableItems[i].track, this.$store.state.downloadableItems[i].title)

                        }
                        // it is an flp
                        else {
                            console.log('this is an flp item')
                            this.downloadMultiFilesWithAxios(this.$store.state.downloadableItems[i].flp_zip, this.$store.state.downloadableItems[i].flp_name)
                        }
                    }
                    this.$store.state.downloadableItems = []
                }

            }
        },
        downloadMultiFilesWithAxios(url, title) {
            axios({
                method: 'get',
                url,
                responseType: 'arraybuffer',
            }).then((response) =>{
                console.log(JSON.stringify(response))
                // forceDownloadMultiFile(response, title)

            }).catch((error) =>  console.log(error))
        },
        forceDownloadMultiFile(response) {
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a')
            link.href = url
            // if it is a single wav file
            link.setAttribute('download', 'sheriffCrandyMusicFiles.zip')
            // else for multiple wav files, or single flp or multiple flp files, or combinations of both
            // it should be zipped
            document.body.appendChild(link)
            link.click()
        },
    },
    // get the flps/tracks/free flps/free tracks from backend
    created() {
    },

    mounted () {
        document.title = "Thank you!";
        this.getFiles()

    },

}
</script>