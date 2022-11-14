import { ActionContext } from 'vuex'

export interface StateAuth {
  user: object
  isLoggedIn: boolean
}

export interface State {
  auth: StateAuth
}

export type Context = ActionContext<StateAuth, State>
