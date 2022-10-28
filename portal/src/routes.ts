import Home from './components/Home.vue'
import Discipline from './components/Discipline.vue'
import Payment from './components/Payment.vue'
import Login from './components/Login.vue'
import Statistics from './components/Statistics.vue'

const routes = [
<<<<<<< Updated upstream
  { 
    name: "home",
    path: "/", 
    component: Home 
  },
  { 
    name: "disciplines",
    path: "/disciplinas", 
    component: Discipline 
  },
  { 
    name: "payments",
    path: "/pagos", 
  component: Payment 
  },
  { 
    name: "statistics",
    path: '/estadisticas', 
    component: Estadisticas 
  },
  { 
    name: "login",
    path: "/autenticar", 
    component: Login 
  },
];
=======
    { path: '/', component: Home },
    { path: '/disciplinas', component: Discipline },
    { path: '/pagos', component: Payment },
    { path: '/estadisticas', component: Statistics },
    { path: '/autenticar', component: Login },
]
>>>>>>> Stashed changes

export default routes
