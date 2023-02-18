import axios from './axios'
import { AssociateResponse } from '../interfaces/responses/AssociateResponse'
import { CardResponse } from '../interfaces/responses/CardResponse'

export const getAssociates = async (): Promise<AssociateResponse> => {
  const response = await axios.get('/stats/associates')
  return response.data
}

export const getMyCard = async (): Promise<CardResponse> => {
  const response = await axios.get('/me/license/')
  return response.data
}
