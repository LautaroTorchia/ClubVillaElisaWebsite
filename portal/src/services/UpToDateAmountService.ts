import axios from './axios'
import { UpToDateResponse } from '../interfaces/responses/UpToDateResponse'

export const getUpToDateAssociates = async (): Promise<UpToDateResponse> => {
    const response = await axios.get('/stats/associates_up_to_date',{
        headers: {
          'Secret-Key': 'f0fda58630310a6dd91a7d8f0a4ceda2:4225637426',
        }
      })
  return response.data
}