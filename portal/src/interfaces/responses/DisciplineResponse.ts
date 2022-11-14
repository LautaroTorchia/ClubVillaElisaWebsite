import { DisciplineClub,DisciplineClubWithCosts } from '../Discipline'

export interface DisciplineClubResponse {
  timestamp: string
  status: number
  status_msg: string
  data: DisciplineClub[]
}

export interface DisciplineClubResponseWithCosts {
  timestamp: string
  status: number
  status_msg: string
  data: DisciplineClubWithCosts[]
}