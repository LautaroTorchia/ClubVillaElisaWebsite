import Home from './components/Home.vue'
import Discipline from './components/Discipline.vue'
import Payment from './components/Payment.vue'
import Login from './components/Login.vue'
import Statistics from './components/Statistics.vue'
import { createRouter, createWebHistory } from 'vue-router'
import store from './stores' // <-- aliased path

const routes = [
  {
    name: 'home',
    path: '/',
    component: Home,
  },
  {
    name: 'disciplines',
    path: '/disciplinas',
    component: Discipline,
  },
  {
    name: 'payments',
    path: '/pagos',
    component: Payment,
  },
  {
    name: 'statistics',
    path: '/estadisticas',
    component: Statistics,
  },
  {
    name: 'login',
    path: '/autenticar',
    component: Login,
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  linkActiveClass: 'active',
})

router.beforeEach(async (to, from) => {
  if (!store.getters['auth/isLoggedIn'] && to.name == 'disciplines') {
    // redirect the user to the login page
    return { name: 'login' }
  }
  if (store.getters['auth/isLoggedIn'] && to.name == 'login') {
    return { name: 'home' }
  }
})

export default router
