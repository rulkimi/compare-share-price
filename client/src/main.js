/* main.js */
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
 
import CanvasJSStockChart from '@canvasjs/vue-stockcharts';
 
const app = createApp(App);
app.use(CanvasJSStockChart);
app.mount('#app');   