export interface Discipline {
  available: boolean
  category: string
  created_at: string
  dates: string
  deleted: boolean
  id: number
  instructors: string
  monthly_cost: number
  name: string
  updated_at: string
  associated_at?: string
}
export interface DisciplineClub {
    name: string,
    teacher: string,
    dates: string,
  }

  export interface DisciplineClubWithCosts {
    name: string,
    teacher: string,
    dates: string,
    monthly_cost: number,
  }