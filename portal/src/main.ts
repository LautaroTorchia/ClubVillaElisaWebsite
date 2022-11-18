import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '@coreui/coreui/dist/css/coreui.min.css'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import './icons.ts'
import store from './stores'
import { vfmPlugin } from 'vue-final-modal'
import router from './router'

createApp(App)
  .use(router)
  .use(store)
  .use(vfmPlugin)
  .component('font-awesome-icon', FontAwesomeIcon)
  .mount('#app')
