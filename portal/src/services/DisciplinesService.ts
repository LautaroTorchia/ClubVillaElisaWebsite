import axios from './axios'
import {
  DisciplineClubResponse,
  DisciplineClubResponseWithCosts,
  DisciplineResponse,
} from '../interfaces/responses/DisciplineResponse'

export const getDisciplines = async (): Promise<DisciplineClubResponse> => {
  const response = await axios.get('/club/disciplines')
  return response.data
}

export const getDisciplinesWithCosts =
  async (): Promise<DisciplineClubResponseWithCosts> => {
    const response = await axios.get('/club/disciplines/disciplines_with_costs')
    return response.data
  }

export const getMyDisciplines = async (): Promise<DisciplineResponse> => {
  const response = await axios.get('/me/disciplines/')
  return response.data
}
