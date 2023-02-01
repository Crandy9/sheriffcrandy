<template>

    <section class="flp-section">
      <!-- flps -->
      <section class="flp-title-section">
        <!-- title -->
        <div class="column is-12">
          <h2 class="flp-main-title is-size-3 has-text-centered has-text-white">
            My FLPs
          </h2>
          <p>
            <a style="color:chartreuse !important; text-decoration: none;" target="_blank" href="https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/fformats_save_flp.htm">What's an FLP?</a>
          </p>
        </div>
      </section>
      <section class="flp-items-section">
        <!-- unordered list of flps -->
        <ul class="flp-list">
          <!-- Vue for loop -->
          <div v-for="flp, index in flps" v-bind:key="flp.id" class="flp-list-div">
            <li class="flp-list-item" v-bind:id="flp.id">
                <div class="flp-title">
                    <!-- flp name -->
                    <span class="flp-title-inner">
                        {{ flp.flp_name }}
                    </span>
                </div>
                <div>
                    <!-- trigger stripe when this is clicked -->
                    <a class="button is-small is-black price-button has-text-weight-medium" v-if="flp.is_free" href="/flps">FREE</a>
                    <a class="button is-small is-black price-button has-text-weight-medium" v-else href="/flps">${{ flp.usd_price }}</a>
                </div>
            </li>
          </div>
        </ul>
      </section>
      <h2 class="flp-guide is-size-5 has-text-centered has-text-warning">
        Click the links on the right to 
        purchase/download the .zip file containing the 
        FL Studio Project and any audio files used for the song. 
        After purchasing the project (or downloading if free), 
        a download of the .zip file will begin in your browser.
        Save the .zip file to your computer, extract/unzip the file's contents and that's it!
        Your .flp file is ready to be opened in your FL Studio DAW to start experimenting!
        Enjoy.
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
    data() {
      return {
        flps: [],
      }
    },
  
    components: {
    },
    // Vue lifecycle hook mounted() is called when this component is added to the DOM
    // so I guess on page load, getFlps() is called  
    mounted() {
      this.getFlps()
    },
    // functions defined here
    methods: {
      getFlps() {
        // replace the API path with env var
        // .get requests API data from server via HTTP GET
        // .then will take the response data and populate the empty tracks list above
        axios.get(process.env.VUE_APP_API_FLPS_URL)
          .then(response => {
            this.flps = response.data
          })
          .catch(error => {
            console.log("ERROR BOYY: " + error)
            console.log(process.env.VUE_APP_API_FLPS_URL)
          })
      }
    }
  }
  </script>