import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHashHistory } from "vue-router";
import routes from "./routes";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  linkActiveClass: "active",
});
createApp(App).use(router).mount("#app");
