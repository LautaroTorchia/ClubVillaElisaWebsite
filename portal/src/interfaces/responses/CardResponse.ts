import { Card } from '../Card'

export interface CardResponse {
  timestamp: string
  status: number
  status_msg: string
  data: Card
}
