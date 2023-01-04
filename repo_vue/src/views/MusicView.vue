<template>
    <!-- music tracks -->
    <section>
        <!-- title -->
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered has-text-black">
          Singles
          </h2>
      </div>
    </section>
    <section class="audio-player-section">
      <!-- unordered list of track -->
      <ul>
        <!-- Vue for loop -->
        <div v-for="track, index in tracks" v-bind:key="track.id" class="media-player">
            <li class="track-list-item">
              <span class="track-number">{{++index}}</span>
              <!-- track image -->
              <!-- <figure class="track-img">
                  <img class="cover-art" v-bind:src="track.get_cover_art">
              </figure> -->
              <!-- track title -->
              <div class="track-title">
                <span class="track-title-inner">
                  {{ track.title}}
                </span>
                <span class="track-dur">{{track.get_track_duration}}</span>
              </div>
              <!-- audio player -->
              <!-- <audio controls>
                <source v-bind:src="track.get_sample" type="audio/ogg">
                Your browser does not support the audio element.
              </audio> -->
              <!-- price -->
              <div>
                <!-- trigger stripe when this is clicked -->
                <a class="button is-small is-black" v-if="track.is_free" href="/music">FREE</a>
                <a class="button is-small is-black" v-else href="/music">${{track.usd_price}}</a>
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
    increment() {
      this.trackNumber++;
    },
    getTracks() {
      // replace the API path with env var
      // .get requests API data from server via HTTP GET
      // .then will take the response data and populate the empty tracks list above
      axios.get(process.env.VUE_APP_API_URL)
      .then(response=> {
        this.tracks = response.data
      })
      .catch(error=>{
        console.log("ERROR BOYY: " + error)
        console.log(process.env.VUE_APP_API_URL)
      })
    }
  }
}
</script>