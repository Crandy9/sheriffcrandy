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
        <h3 style="padding: 1rem; color: aqua;" v-if="currentTrackPlaying == 0" class="is-size-4">
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
              <div class="control">
                <!-- add track to cart. click.stop prevents the parent click even from firing
                  doesn't play/pause the song, adds this item to cart only
                -->
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-if="track.is_free" 
                  @click.stop="addTrackToCart(track.id)">
                  FREE
                </a>
                <!-- set var for jpy/usd -->
                <a class="button is-small is-black price-button has-text-weight-medium" 
                  v-else 
                  @click.stop="addTrackToCart(track.id)">
                  ${{ track.usd_price }}
                </a>
              </div>
            </div>
          </li>
        </div>
      </ul>
    </section>
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

<script>
// @ is an alias to /src

// use axios to get api data from backend to frontend
// axios was installed during initial vue setup. found in package.json
// need to import axios in main.js as well
import axios from 'axios'

export default {
  name: 'Music',
  // data() is a new obj returning tracks list used in for loop above
  data() {
    return {
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
      // play track for 51 seconds 
      duration: 51000,
      timeRemaining: 0,
    }
  },

  components: {
  },
  // Vue lifecycle hook mounted() is called when this component is added to the DOM
  // so I guess on page load, getTracks() is called  
  mounted() {
    this.getTracks()
  },
  // functions defined here
  methods: {

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
    getTracks() {
      // replace the API path with env var
      // .get requests API data from server via HTTP GET
      // .then will take the response data and populate the empty tracks list above
      axios.get(process.env.VUE_APP_TRACKS_API_URL)
        .then(response => {
          this.tracks = response.data
        })
        .catch(error => {
          console.log("ERROR BOYY: " + error)
          console.log(process.env.VUE_APP_TRACKS_API_URL)
        })
    },

    // add to cart
    addTrackToCart(track) {

      // get specific track added to cart
      const item = this.tracks.find(item => item.id === track)

      // calls store/index.js addToCart function
      this.$store.commit('addToCart', item)
    },
  }
}
</script>