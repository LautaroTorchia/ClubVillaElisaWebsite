import axios from '../../services/axios'
import { StateAuth, Context } from '../../interfaces/StateAuth'

const namespaced = true

const state: StateAuth = {
  user: {},
  isLoggedIn: false,
}

const getters = {
  isLoggedIn: (state: StateAuth) => state.isLoggedIn,
  user: (state: StateAuth) => state.user,
}

const actions = {
  async loginUser(context: Context, user: object) {
    const res = await axios.post('/auth/login', user)
    if (res.status == 201) await context.dispatch('fetchUser')
  },
  async fetchUser(context: Context) {
    await axios
      .get('/auth/user_jwt')
      .then(({ data }) => context.commit('setUser', data))
  },
  async logoutUser(context: Context) {
    context.commit('logoutUserState')
    await axios.post('/auth/logout')
  },
}

const mutations = {
  setUser(state: StateAuth, user: object) {
    state.isLoggedIn = true
    state.user = user
  },
  logoutUserState(state: StateAuth) {
    state.isLoggedIn = false
    state.user = {}
  },
}

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations,
}
