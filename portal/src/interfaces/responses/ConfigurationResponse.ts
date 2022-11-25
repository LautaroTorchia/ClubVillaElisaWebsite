import { Configuration } from '../Configuration'

export interface ConfigurationResponse {
  timestamp: string
  status: number
  status_msg: string
  data: Configuration
}
