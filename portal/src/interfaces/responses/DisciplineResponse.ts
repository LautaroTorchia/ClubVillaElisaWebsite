import {
  Discipline,
  DisciplineClub,
  DisciplineClubWithCosts,
} from '../Discipline'

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

export interface DisciplineResponse {
  timestamp: string
  status: number
  status_msg: string
  data: Discipline[]
}
