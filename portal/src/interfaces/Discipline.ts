export interface Discipline {
  available?: boolean
  category: string
  created_at?: string
  days: string
  deleted?: boolean
  id?: number
  teacher: string
  price: number
  name: string
  updated_at?: string
  associated_at?: string
}

export interface DisciplineClub {
  name: string
  teacher: string
  dates: string
}

export interface DisciplineClubWithCosts {
  name: string
  teacher: string
  dates: string
  category: string
  monthly_cost: number
}
