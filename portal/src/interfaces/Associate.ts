import { Discipline } from './Discipline'
export interface Associate {
  id?: number
  DNI_number: number
  DNI_type: string
  address: string
  email: string
  gender: string
  name: string
  phone_number: number
  surname: string
  disciplines?: Discipline[]
}
