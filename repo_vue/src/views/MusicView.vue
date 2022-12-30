<template>
    <!-- music tracks -->
    <section class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">
            Latest Tracks
            </h2>
        </div>
        <!-- Vue for loop -->
        <div 
            class="colum is-3" 
            v-for="track in tracks"
            v-bind:key="track.id"
            >
            <!-- track image -->
            <div class="box">
            <figure class="image mb-4">
                <img class="cover-art" v-bind:src="track.get_cover_art">
            </figure>
            <!-- track name -->
            <h3 class="is-size-4">{{ track.title}}</h3>
            <!-- price -->
            <p class="is-size-6 has-text-white">${{track.usd_price}}</p>
            <p class="is-size-6 has-text-white">¥{{track.jpy_price}}</p>

            View Details
            </div>
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