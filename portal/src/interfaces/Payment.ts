export interface Payment {
  id: string
  date: Date
  paid_late: boolean
  amount: number
  installment_number: number
}
