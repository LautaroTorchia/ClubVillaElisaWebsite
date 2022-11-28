import { createStore, Store } from 'vuex'
import authModule from './modules/auth'
import { State } from '../interfaces/StateAuth'
import createPersistedState from 'vuex-persistedstate'

const store: Store<State> = createStore({
  modules: {
    auth: authModule,
  },
  plugins: [createPersistedState()],
})

export default store
