import axios from './axios'
import { DisciplineClubResponse,DisciplineClubResponseWithCosts } from '../interfaces/responses/DisciplineResponse'

export const getDisciplines = async (): Promise<DisciplineClubResponse> => {
  const response = await axios.get('/club/disciplines')
  return response.data
}

export const getDisciplinesWithCosts = async (): Promise<DisciplineClubResponseWithCosts> => {
  const response = await axios.get('/club/disciplines_with_costs')
  return response.data
}