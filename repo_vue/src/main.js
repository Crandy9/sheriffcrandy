import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// define API path for axios
// process.env is already built in by VUE. Simply create and define .env file in root dir
axios.defaults.baseURL = (process.env.VUE_APP_BACKEND_URL)

createApp(App).use(store).use(router, axios).mount('#app')
