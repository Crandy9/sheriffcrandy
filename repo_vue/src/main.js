import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { createI18n } from 'vue-i18n'
import 'animate.css'

// all translations will be placed here
// const i18n is a plugin that vue can use in the views/components
const i18n = createI18n({
    // default locale
    locale: "en",
    // translations
    messages: {
        // 
        en: {
            logIn: "Log In"
        }
    }
})

// define API server path for axios
// process.env is already built in by VUE. Simply create and define .env file in root dir
axios.defaults.baseURL = (process.env.VUE_APP_BACKEND_URL)

createApp(App).use(store).use(router, axios).use(i18n).mount('#app')
