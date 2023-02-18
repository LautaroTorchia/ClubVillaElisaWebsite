import { Payment } from '../Payment'

export interface PaymentResponse {
  timestamp: string
  status: number
  status_msg: string
  data: {
    name: string
    surname: string
    entry_date: Date
    actual_amount: number
    payments: Payment[]
  }
}
