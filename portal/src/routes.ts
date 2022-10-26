import Home from './components/Home.vue'
import Discipline from './components/Discipline.vue'
import Payment from './components/Payment.vue'
import Login from './components/Login.vue'
import Estadisticas from './components/Estadisticas.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/disciplinas', component: Discipline },
    { path: '/pagos', component: Payment },
    { path: '/estadisticas', component: Estadisticas },
    { path: '/autenticar', component: Login },
]

export default routes
