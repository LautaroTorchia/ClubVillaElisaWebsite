import axios from './axios'
import { DisciplineResponse } from '../interfaces/responses/DisciplineResponse'

export const getDisciplines = async (): Promise<DisciplineResponse> => {
  const response = await axios.get('/club/disciplines')
  return response.data
}
