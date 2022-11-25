import axios from './axios'
import { InfoResponse } from '../interfaces/responses/InfoResponse'

export const getInfo = async (): Promise<InfoResponse> => {
  const response = await axios.get('/club/info/')
  return response.data
}
