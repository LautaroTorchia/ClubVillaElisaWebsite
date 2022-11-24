import axios from './axios'
import { ConfigurationResponse } from '../interfaces/responses/ConfigurationResponse'

export const getConfiguration = async (): Promise<ConfigurationResponse> => {
  const response = await axios.get('/configuracion/')
  return response.data
}
