import axios from './axios'
import { AssociateResponse } from '../interfaces/responses/AssociateResponse'

export const getAssociates = async (): Promise<AssociateResponse> => {
    const response = await axios.get('/stats/associates',{
        headers: {
          'Secret-Key': 'f0fda58630310a6dd91a7d8f0a4ceda2:4225637426',
        }
      })
  return response.data
}