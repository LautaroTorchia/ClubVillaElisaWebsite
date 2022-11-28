import axios from './axios'
import { UpToDateResponse } from '../interfaces/responses/UpToDateResponse'

export const getUpToDateAssociates = async (): Promise<UpToDateResponse> => {
  const response = await axios.get('/stats/associates_up_to_date')
  return response.data
}
