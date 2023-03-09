import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'animate.css'
import { createI18n } from 'vue-i18n'


// define backend API server path for axios
// process.env is already built in by VUE. Simply create and define .env file in root dir
//  for VUE JS env vars, need to have `VUE_APP` prepended
//  to variable name
axios.defaults.baseURL = (process.env.VUE_APP_BACKEND_URL)

createApp(App).use(store).use(router, axios).use(i18n).mount('#app')
