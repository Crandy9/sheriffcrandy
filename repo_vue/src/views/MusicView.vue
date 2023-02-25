<template>

  <section class="main-music-section">

    <!-- music tracks -->
    <section class="title-art-sfsb-section">
      <!-- title -->
      <div class="column is-12" >
        <h2 class="music-title is-size-3 has-text-centered has-text-white">
          Sheriff Crandy Music
        </h2>
      </div>
      <div v-for="trackDisplay in tracks" v-bind:key="trackDisplay.id">
        <!-- show img thumbnail for current track -->
        <!-- or leave title up after song stops playing -->
        <figure v-if="currentTrackPlaying == trackDisplay.id || (lastPlayedTrack == trackDisplay.id && stop == true)" class="track-img">
          <img class="cover-art" v-bind:src="trackDisplay.get_cover_art">
        </figure> 
        <h3 class="track-title-img" v-if="currentTrackPlaying == trackDisplay.id || (lastPlayedTrack == trackDisplay.id && stop == true)">
          Sheriff Crandy - {{ trackDisplay.title }}
        </h3>
      </div>
      <div>
        <h3 style="padding: 1rem;" v-if="currentTrackPlaying == 0" class="is-size-5 has-text-warning">
          Click on a song to hear a sample!
        </h3>
      </div>
      <div class="skip-icons-wrapper">
        <div class="skip-icons">
          <span @click="prevTrack()">
            <i class="fa fa-fast-backward"></i>
          </span>
          <span @click="nextTrack()">
            <i class="fa fa-fast-forward"></i>  
          </span>
        </div>
      </div>
    </section>
    <section class="music-player-section">
      <!-- currently playing song -->
      <!-- unordered list of track -->
      <ul class="audio-player-ul">
        <!-- Vue for loop -->
        <div v-for="track, index in tracks" v-bind:key="track.id" class="media-player">
          <!-- play audio if play is true -->
          <audio class="hidden-player" controls autoplay v-if="play == true && pause == false && currentTrackPlaying == track.id">
            <source :src="track.get_sample" type="audio/mpeg">
            Your browser does not support the audio element.
          </audio>
          <div>
          </div>
          <li @click="setPlayOrPause(track.id)" class="track-list-item" v-bind:id="track.id">
            <!-- show play button on all tracks on hover -->
            <a class="play-button" href="#" v-if="currentTrackPlaying != track.id">
              <span class="play-icon-span">
                <svg 
                  class="play-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 26 26">
                  <polygon points="9.33 6.69 9.33 19.39 19.3 13.04 9.33 6.69" />
                </svg>
              </span>
            </a>
            <!-- show play button on paused track -->
            <a class="play-button-on-pause" href="#"
              v-if="(currentTrackPlaying == track.id && play == false && pause == true) || (lastPlayedTrack == track.id && play == false && pause == false && stop == true)">
              <span class="play-icon-span">
                <svg 
                  class="play-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 26 26">
                  <polygon points="9.33 6.69 9.33 19.39 19.3 13.04 9.33 6.69" />
                </svg>
              </span>
            </a>
            <!-- show pause button while playing -->
            <a class="pause-button" href="#" v-if="currentTrackPlaying == track.id && play == true && pause == false">
              <!-- show pause button only on track that is currently playing -->
              <span class="pause-icon-span" style="display: block !important">
                <svg 
                  class="pause-icon-svg" 
                  xmlns="http://www.w3.org/2000/svg" 
                  preserveAspectRatio="xMinYMin meet"
                  viewBox="0 0 16 16">
                  <path
                    d="M6 3.5 a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5zm4 0a.5.5 0 0 1 .5.5v8a.5.5 0 0 1-1 0V4a.5.5 0 0 1 .5-.5z">
                  </path>
                </svg>
              </span>
            </a>
            <!-- hide track number when track is playing -->
            <span v-if="currentTrackPlaying != track.id" class="track-number">{{++index}}</span>
            <!-- track title -->
            <div class="track-title">
              <span class="track-title-inner">
                {{ track.title }}
                <span class="track-dur">
                  {{ track.get_track_duration }}
                </span>
              </span>
            </div>
            <!-- price -->
            <div class="field has-addons">
              <!-- had to change class name because 'control' was being used by login/signup forms -->
              <div class="sheriff-crandy-music-ctrl-panel">
                <!-- check if this item is already in the cart -->
                <a class="music-in-cart-button button is-small price-button has-text-weight-medium" 
                  v-if="checkIfTrackIsInCart(track)" 
                  @click.stop="modalOpened = false; removeFromCart(track.id)" data-target="my-modal-id">
                  Added to Cart!
                </a>
                <!-- open modal. click.stop prevents the parent click even from firing
                  doesn't play/pause the song, adds this item to cart only
                -->
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.is_free" 
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  FREE
                </a>
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.usd_price"
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  ${{ track.usd_price }}
                </a>
                <!-- <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else-if="track.jpy_price"
                  @click.stop="modalOpened = true; setTrack(track.id);" data-target="my-modal-id">
                  ${{ track.jpy_price }}
                </a> -->
              </div>
            </div>
          </li>
        </div>
      </ul>
    </section>
    <!-- modal -->
    <Transition>
      <div v-if="modalOpened" id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
        <div class="modal-background"></div>

          <div class="modal-card">
            <header class="modal-card-head">
              <p class="modal-card-title">Buy now?</p>
              <button @click="modalOpened = false" class="delete" aria-label="close"></button>
            </header>
            <section v-if="isFree" class="modal-card-body">
              Do you want to download "{{ setTrackTitle }}" for free now or add it to your cart and continue shopping?
            </section>
            <section v-else class="modal-card-body">
              Do you want to purchase "{{ setTrackTitle }}" now or add it to your cart and continue shopping?
            </section>
            <footer class="modal-card-foot">
              <!-- trigger stripe payment on this item only -->
              <button @click="modalOpened = false" class="my-modal-button-buy-now button">Buy Now</button>
              <!-- if adding to cart, add the item to cart and close modal -->
              <button @click.stop="addTrackToCart(setTrackID); modalOpened = false" class="my-modal-button-add-to-cart button">Add to Cart</button>
            </footer>
          </div>
      </div>
    </Transition>
    <!-- end modal -->


    <!-- item already in modal -->
    <!-- <div id="my-modal-id" class="modal" v-bind:class="{'is-active':modalOpened}">
      <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Add to Cart?</p>
            <button @click="modalOpened = false" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body">
            Do you want to add this item to your cart or proceed to checkout?
          </section>
          <footer class="modal-card-foot">
            <button @click.stop="addTrackToCart(setTrack); modalOpened = false" class="button is-success">Add to cart</button>
            <button @click="modalOpened = false" class="button">Proceed to checkout</button>
          </footer>
        </div>
    </div> -->
    <!-- end modal -->
    <h2 class="music-guide is-size-5 has-text-centered has-text-warning">
      Click the links on the right to purchase/download 
      the .wav audio file for the song you want. 
      After purchasing the song (or downloading if free), 
      a download of the .wav file will begin in your browser.
      Save the .wav file to your computer and enjoy the tunes.
      <div class="is-size-6" style="padding: 1rem;">
        <p style="padding:1.2rem;">
          <a class="file-links" target="blank" href="https://www.wideanglesoftware.com/blog/how-to-transfer-music-from-computer-to-android.php#:~:text=on%20your%20Mac.-,Connect%20your%20Android%20to%20your%20Windows%20PC%20using%20a%20USB,device%20in%20Android%20File%20Transfer.">
            - Transfer wav files from computer to Android
          </a>
        </p>
        <p style="padding:1.2rem;">
          <a class="file-links" target="blank" href="https://support.apple.com/guide/itunes/transfer-files-itns32636/windows">
            - Transfer wav files from computer to iPhone
          </a>
        </p>
      </div>
    </h2>
  </section>
</template>


<!-- modal animation fade-in/out -->
<style>
  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.3s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }
</style>


<script>
// @ is an alias to /src

// use axios to get api data from backend to frontend
// axios was installed during initial vue setup. found in package.json
// need to import axios in main.js as well
import axios from 'axios'
// for pop up notifying user about added item to cart
import { toast } from 'bulma-toast'

export default {
  name: 'Music',
  // data() is a new obj returning tracks list used in for loop above
  data() {
    return {
      modalOpened: false,
      tracks: [],
      // track number
      trackNumber: 0,
      // player status
      play: false,
      pause: false,
      stop: true,
      currentTrackPlaying: 0,
      lastPlayedTrack: 0,
      currentTimer: '',
      currentSeconds: 0,
      currentInterval: '',
      // play sample for 51 seconds 
      duration: 51000,
      timeRemaining: 0,
      // pass trackid to modal
      setTrackID: '',
      setTrackTitle: '',
      isFree: ''
    }
  },

  components: {
  },
  // Vue lifecycle hook mounted() is called when this component is added to the DOM
  // so I guess on page load, getTracks() is called  
  mounted() {
    this.getTracks();
    document.addEventListener('click', this.closeModalOnWindowClick);
  },
  // functions defined here
  methods: {

    setTrack(track) {
      // set track name as well to show in modal popup
      const item = this.tracks.find(item => item.id === track)
      this.setTrackTitle = item.title;
      this.isFree = item.is_free;
      this.setTrackID = track;
    },

    closeModalOnWindowClick() {
      if (this.modalOpened === false) {

      }
      else if (this.modalOpened === true) {
        this.modalOpened = false;

      }
    },

    // skip track forward
    nextTrack() {
      var last_track = this.tracks[this.tracks.length - 1].id
      // if no songs have been played, skip to second track in playlist 
      if (this.currentTrackPlaying == 0) {
        this.currentTrackPlaying = this.tracks[0].id
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);
      }
      // else if this is the last track in the playlist, play the first track
      else if (this.currentTrackPlaying == last_track) {
        this.currentTrackPlaying = this.tracks[0].id
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);
      }
      else {
        // local var containing the current track id needed for function below 
        var val = this.currentTrackPlaying
        // get the JSON object index of the current song in the playlist
        var index = this.tracks.findIndex(function(item){
          return item.id === val;
        });
        // get the id of the next track in the playlist
        this.currentTrackPlaying = this.tracks[index + 1].id

        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);
      }
    },
    prevTrack() {
      var first_track = this.tracks[0].id
      var last_track = this.tracks[this.tracks.length - 1].id

      // if no songs have been played or if current track is the first_track, play the last track in the playlist
      if (this.currentTrackPlaying == 0 || this.currentTrackPlaying == first_track) {
        this.currentTrackPlaying = last_track
        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);
      }
      // skip back to the previous track
      else {
        // same setup for nextTrack only reversed
        var val = this.currentTrackPlaying
        var index = this.tracks.findIndex(function(item){
          return item.id === val;
        });
        // get the id of the prev track in the playlist
        this.currentTrackPlaying = this.tracks[index - 1].id

        this.play = true;
        this.stop = false;
        this.pause = false;
        clearTimeout(this.currentTimer)
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);
      }

    },
    // number the tracks for UI/UX media player
    increment() {
      this.trackNumber++;
    },
    // for playing/pausing track
    setPlayOrPause(track) {

      // if currentTrackPlaying is 0, it means no song has been played
       if (this.currentTrackPlaying == 0 && this.play == false && this.pause == false && this.stop == true) {
        // set the current track to the track selected by user
        this.currentTrackPlaying = track
        this.play = true;
        this.stop = false;
        // start timer
        this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);        
      }
      // either pausing or resuming current track
      else if (this.currentTrackPlaying == track) {
        // if the song is currently playing, pause it
        if (this.play == true && this.pause == false && this.stop == false) {
          this.pause = true;
          this.play = false;
          // get how many more seconds the song has to play
        }
        // if song is currently paused, resume it
        else if (this.play == false && this.pause == true && this.stop == false){
          this.pause = false;
          this.play = true;
          // 
          clearTimeout(this.currentTimer)
          // resume timeout
          // start new timer and set stop = true if full song plays
          this.currentTimer = setTimeout(() => {
            this.stop = true; 
            this.lastPlayedTrack = this.currentTrackPlaying;
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration); 
        }
      }
      // stop current track and play new track
      else {
        // clear the timer that was playing
        clearTimeout(this.currentTimer)
        // set the new track
        this.currentTrackPlaying = track;
        this.play = true
        this.stop = false;
        this.pause = false;
        // start new timer
        this.currentTimer = setTimeout(() => {
            this.stop = true;
            this.lastPlayedTrack = this.currentTrackPlaying; 
            this.play = false;
            this.pause = false;
            // this.currentTrackPlaying = 0; 
          }, this.duration);         
      }
    },

    // make this method async and axios.get to await to make sure setIsLoading isn't set to false
    // until axios finished fetching api data
    async getTracks() {
      
      // loading bar while api data is getting fetched
      this.$store.commit('setIsLoading', true);
      // replace the API path with env var
      // .get requests API data from server via HTTP GET
      // .then will take the response data and populate the empty tracks list above
      await axios.get(process.env.VUE_APP_TRACKS_API_URL)
        .then(response => {
          this.tracks = response.data
          // set the tab title
          document.title = 'Music'
        })
        .catch(error => {
          console.log("ERROR BOYY: " + error)
          console.log(process.env.VUE_APP_TRACKS_API_URL)
        })

      // stop loading bar after api data is fetched
      this.$store.commit('setIsLoading', false);
    },

    // add to cart
    addTrackToCart(addTrackIdToCart) {

      // get specific track added to cart
      const item = this.tracks.find(item => item.id === addTrackIdToCart)

      // calls store/index.js addToCart function
      this.$store.commit('addToCart', item)

      // show toast msg to user https://www.npmjs.com/package/bulma-toast
      // toast fadein/out animation requires animate.css. See README
      toast({
        message: ' \"' + item.title + '\" added to cart!',
        type: 'is-info',
        dismissible: true,
        pauseOnHover: true,
        duration: 3000,
        position: 'bottom-right',
        animate: { in: 'fadeIn', out: 'fadeOut' },
      })
    },
    // remove from cart
    removeFromCart(removeItemID) {
      // get specific track added to cart
      const item = this.tracks.find(item => item.id === removeItemID)
      // pass entire json track/flp obj to removeFromCart function
      this.$store.commit('removeFromCart', item)
      toast({
        message: ' \"' + item.title + '\" removed from cart!',
        type: 'is-danger',
        dismissible: true,
        pauseOnHover: true,
        duration: 3000,
        position: 'bottom-right',
        animate: { in: 'fadeIn', out: 'fadeOut' },
      })
    },
    // check if an item clicked is already in the cart
    checkIfTrackIsInCart(track) {
      const pendingTrackCartItem = 
      this.
      $store.
      state.
      cart.
      itemsInCart.
      filter(i => i.title === track.title)
        if (pendingTrackCartItem.length) {
          return true;
        }
    }
  }
}
</script>