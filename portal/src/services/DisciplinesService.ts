import axios from './axios'
import { DisciplineClubResponse,DisciplineClubResponseWithCosts } from '../interfaces/responses/DisciplineResponse'

export const getDisciplines = async (): Promise<DisciplineClubResponse> => {
  const response = await axios.get('/club/disciplines')
  return response.data
}

export const getDisciplinesWithCosts = async (): Promise<DisciplineClubResponseWithCosts> => {
  const response = await axios.get('/club/disciplines/disciplines_with_costs',{
    headers: {
      'Secret-Key': 'f0fda58630310a6dd91a7d8f0a4ceda2:4225637426',
    }
  })
  return response.data
}