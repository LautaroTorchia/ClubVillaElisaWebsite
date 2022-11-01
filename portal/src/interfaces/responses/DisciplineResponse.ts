import { Discipline } from '../Discipline'

export interface DisciplineResponse {
  timestamp: string
  status: number
  status_msg: string
  data: Discipline[] | string
}
