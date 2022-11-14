import { createStore, Store } from 'vuex'
import authModule from './modules/auth'
import { State } from '../interfaces/StateAuth'

const store: Store<State> = createStore({
  modules: {
    auth: authModule,
  },
})

export default store
