<template>
  <!-- music tracks -->
  <section>
    <!-- title -->
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered has-text-black">
        Singles
      </h2>
    </div>
    <div v-for="trackDisplay in tracks" v-bind:key="trackDisplay.id">
      <h4 v-if="currentTrackPlaying == trackDisplay.id">
        {{ trackDisplay.title }}
      </h4>
        <!-- show img thumbnail for current track -->
      <figure v-if="currentTrackPlaying == trackDisplay.id" class="track-img">
        <img class="cover-art" v-bind:src="trackDisplay.get_cover_art">
      </figure> 
    </div>
    <div class="skip-icons">
      <a href="#">
        <i class="fa fa-fast-backward"></i>
      </a>
      <a href="#">
        <i class="fa fa-fast-forward"></i>  
      </a>
    </div>
  </section>
  <section class="audio-player-section">
    <!-- currently playing song -->
    <!-- unordered list of track -->
    <ul class="audio-player-ul">
      <!-- Vue for loop -->
      <div v-for="track, index in tracks" v-bind:key="track.id" @click="setPlayOrPause(track.id)" class="media-player">
        <!-- play audio if play is true -->
        <audio class="hidden-player" controls autoplay v-if="play == true && pause == false && currentTrackPlaying == track.id">
          <source :src="track.get_sample" type="audio/mpeg">
          Your browser does not support the audio element.
        </audio>
        <div>
        </div>
        <li class="track-list-item" v-bind:id="track.id">
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
          <a class="play-button-on-pause" href="#" v-if="currentTrackPlaying == track.id && play == false && pause == true">
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
          <!-- audio player -->
          <!-- <audio controls>
                <source v-bind:src="track.get_sample" type="audio/ogg">
                Your browser does not support the audio element.
              </audio> -->
          <!-- price -->
          <div>
            <!-- trigger stripe when this is clicked -->
            <a class="button is-small is-black price-button has-text-weight-medium" v-if="track.is_free" href="/music">FREE</a>
            <a class="button is-small is-black price-button has-text-weight-medium" v-else href="/music">${{ track.usd_price }}</a>
          </div>
        </li>
      </div>
    </ul>
  </section>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
// import { title } from 'process';

// use axios to get api data from backend to frontend
// axios was installed during initial vue setup. found in package.json
// need to import axios in main.js as well
import axios from 'axios'

export default {
  name: 'HomeView',
  // data() is a new obj returning tracks list used in for loop above
  data() {
    return {
      tracks: [],
      // track number
      trackNumber: 0,
      // check whether this track is being played or not
      play: false,
      pause: false,
      stop: true,
      currentTrackPlaying: 0,
      currentTimer: '',
      currentSeconds: 0,
      currentInterval: '',
      timeRemaining: 0
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
    // number the tracks for UI/UX
    increment() {
      this.trackNumber++;
    },
    // for playing/pausing track
    setPlayOrPause(track) {

      // get the specific track chosen as a JSON Object
      const currentTrack = this.tracks.filter(x => x.id == track)
      // get track id
      const id = currentTrack[0].id
      // get track id
      const title = currentTrack[0].title

      // if currentTrackPlaying is 0, it means no song has been played
       if (this.currentTrackPlaying == 0 && this.play == false && this.pause == false && this.stop == true) {
        // set the current track to the track selected by user
        this.currentTrackPlaying = track
        console.log("PLAY: " + title + ' ' + this.currentTrackPlaying)
        this.play = true;
        this.stop = false;
        // start timer
        this.currentTimer = setTimeout(() => {
            console.log("FINISHED")
            this.stop = true; 
            this.play = false;
            this.pause = false;
            this.currentTrackPlaying = 0; 
          }, 51000);        
        // print seconds
        // var i = 0
        // this.currentInterval = setInterval(function(){ 
        //   i = i + 1;
        //   this.currentSeconds = i;
        //   this.timeRemaining = 51 - this.currentSeconds;
        //   if (this.timeRemaining == 0) {
        //     console.log("interval cleared")
        //     clearInterval(this.currentInterval);
        //   }
        //   console.log(this.timeRemaining);
        // }, 1000);
      }
      // either pausing or resuming track in the queue
      else if (this.currentTrackPlaying == track) {
        // if the song is currently playing, pause it
        if (this.play == true && this.pause == false && this.stop == false) {
          // stop interval
          clearInterval(this.currentInterval);
          console.log("PAUSE: " + title + ' ' + this.currentTrackPlaying)
          this.pause = true;
          this.play = false;
          // get how many more seconds the song has to play
          console.log("time remaining: " + this.timeRemaining)
        }
        // if song is currently paused, resume it
        else if (this.play == false && this.pause == true && this.stop == false){
          console.log("RESUME: " + title + ' ' + this.currentTrackPlaying)
          this.pause = false;
          this.play = true;
          // resume timeout
          // start new timer and set stop = true if full song plays
          this.currentTimer = setTimeout(() => {
            console.log("FINISHED")
            this.stop = true; 
            this.play = false;
            this.pause = false;
            this.currentTrackPlaying = 0; 
            console.log("Timer finished");
            console.log("play: " + this.play)
            console.log("pause: " + this.pause)
            console.log("stop: " + this.stop)
          }, 51000); 
          console.log("Timer continued")
        }
      }
      // stop current track and play new track
      else {
        console.log("STOPPED")
        // clear the timer that was playing
        clearTimeout(this.currentTimer)
        clearInterval(this.currentInterval)
        // set the new track
        this.currentTrackPlaying = track;
        console.log("START NEW TRACK: " + title + ' ' + this.currentTrackPlaying);
        this.play = true
        this.stop = false;
        this.pause = false;
        // start new timer
        this.currentTimer = setTimeout(() => {
            console.log("FINISHED")
            this.stop = true; 
            this.play = false;
            this.pause = false;
            this.currentTrackPlaying = 0; 
            console.log("Timer finished");
            console.log("play: " + this.play)
            console.log("pause: " + this.pause)
            console.log("stop: " + this.stop)
          }, 51000);         
        console.log("New Timer Started For new Song")
      }
    },
    getTracks() {
      // replace the API path with env var
      // .get requests API data from server via HTTP GET
      // .then will take the response data and populate the empty tracks list above
      axios.get(process.env.VUE_APP_API_URL)
        .then(response => {
          this.tracks = response.data
        })
        .catch(error => {
          console.log("ERROR BOYY: " + error)
          console.log(process.env.VUE_APP_API_URL)
        })
    }
  }
}
</script>