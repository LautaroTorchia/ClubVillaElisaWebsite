import axios from './axios'
import { PaymentResponse } from '../interfaces/responses/PaymentResponse'

export const getPayments = async (id: string): Promise<PaymentResponse> => {
  const response = await axios.get('/me/payments/' + id)
  return response.data
}


export const createPayment = async (id:string): Promise<PaymentResponse> => {
  const response = await axios.post('/me/payments/' + id)
  return response.data
}
