import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()


// Create vue app
const app = createApp(App)

// use plugins
app.use(vuetify)


// Mount vue app
app.mount('#app')