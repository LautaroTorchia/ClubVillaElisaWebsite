import axios from './axios'
import { DisciplineClubResponse } from '../interfaces/responses/DisciplineResponse'

export const getDisciplines = async (): Promise<DisciplineClubResponse> => {
  const response = await axios.get('/club/disciplines')
  return response.data
}
