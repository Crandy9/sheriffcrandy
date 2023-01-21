<template>
  <div class="home">
    <div class="banner">
      <h2 class="subtitle">
        “Blessed is the man that trusts in the Lord, and whose hope the Lord is."
       <p><cite>-Jeremiah 17:7 (KJV)</cite></p>
    </h2>
    </div>
    <div class="has-text-centered">
      <figure>
        <img class="sheriff-crandy-img" src="@/assets/images/piano.jpg" alt="">
      </figure>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

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