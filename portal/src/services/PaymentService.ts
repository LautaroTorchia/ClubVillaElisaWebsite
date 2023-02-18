import axios from './axios'
import { PaymentResponse } from '../interfaces/responses/PaymentResponse'

export const getPayments = async (id: number): Promise<PaymentResponse> => {
  const response = await axios.get('/me/payments/' + id)
  return response.data
}

export const createPayment = async (
  id: number,
  image: string
): Promise<PaymentResponse> => {
  const response = await axios.post('/me/payments/' + id, { image })
  return response.data
}
