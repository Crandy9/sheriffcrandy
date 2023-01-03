<template>
    <!-- music tracks -->
    <section>
      <!-- title -->
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered has-text-white">
            Singles/Demos
            </h2>
        </div>
        <!-- Vue for loop -->
        <div v-for="track in tracks" v-bind:key="track.id" class="media-player">
            <!-- track image -->
              <figure>
                  <img class="cover-art" v-bind:src="track.get_cover_art">
              </figure>
              <!-- track name -->
              <h1 class="track-title">{{ track.title}}</h1>
              <!-- price -->
              <p class="price">${{track.usd_price}}</p>
              <p class="price">¥{{track.jpy_price}}</p>
        </div>
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
      tracks: []
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