import Home from './components/Home.vue'
import Discipline from './components/Discipline.vue'
import Payment from './components/Payment.vue'
import Login from './components/Login.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/disciplinas', component: Discipline },
    { path: '/pagos', component: Payment },
    { path: '/autenticar', component: Login },
]

export default routes
