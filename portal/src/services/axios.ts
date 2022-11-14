import axios, { AxiosInstance } from 'axios'
const axiosInstance: AxiosInstance = axios.create({
  baseURL: 'http://localhost:5000/api', // TODO: make it change depending on environment
  withCredentials: true,
  xsrfCookieName: 'csrf_access_token',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default axiosInstance
