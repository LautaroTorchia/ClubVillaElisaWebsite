import axios, { AxiosInstance } from 'axios'
const axiosInstance: AxiosInstance = axios.create({
  baseURL: import.meta.env.PROD
    ? 'https://admin-grupo12.proyecto2022.linti.unlp.edu.ar/api'
    : 'http://localhost:5000/api',
  withCredentials: true,
  xsrfCookieName: 'csrf_access_token',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default axiosInstance
