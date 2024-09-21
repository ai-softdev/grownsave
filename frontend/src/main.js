import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";
import store from "./store/index.js";
import i18n from "./locales/index.js";
import 'swiper/css';
import 'vue3-toastify/dist/index.css';
import '@vuepic/vue-datepicker/dist/main.css'

const app = createApp(App);
app.use(router);
app.use(i18n);
app.use(store);
app.mount('#app')
