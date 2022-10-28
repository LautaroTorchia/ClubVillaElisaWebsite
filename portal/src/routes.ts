import Home from './components/Home.vue'
import Discipline from './components/Discipline.vue'
import Payment from './components/Payment.vue'
import Login from './components/Login.vue'
import Statistics from './components/Statistics.vue'

const routes = [
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
      component: Statistics 
    },
    { 
      name: "login",
      path: "/autenticar", 
      component: Login 
    },
  ];

export default routes
