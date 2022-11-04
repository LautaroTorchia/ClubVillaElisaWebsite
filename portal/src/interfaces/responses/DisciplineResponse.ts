import { DisciplineClub } from '../Discipline'

export interface DisciplineClubResponse {
  timestamp: string
  status: number
  status_msg: string
  data: DisciplineClub[]
}
