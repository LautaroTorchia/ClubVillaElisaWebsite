import { Payment } from '../Payment'

export interface PaymentResponse {
  timestamp: string
  status: number
  status_msg: string
  data: Payment[]
}
