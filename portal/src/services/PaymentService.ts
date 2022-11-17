import axios from './axios'
import { PaymentResponse } from '../interfaces/responses/PaymentResponse'

export const getPayments = async (): Promise<PaymentResponse> => {
  const response = await axios.get('/me/payments/')
  return response.data
}


export const createPayment = async (): Promise<PaymentResponse> => {
  const response = await axios.post('/me/payments/')
  return response.data
}
