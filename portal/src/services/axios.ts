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

const COOKIE_EXPIRED_MSG = 'Token has expired'

axiosInstance.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    switch (error.response.status) {
      case 401:
        const error_message = error.response.data.msg
        if (!error.config.retry && error_message === COOKIE_EXPIRED_MSG) {
          error.config.retry = true
          axiosInstance.defaults.xsrfCookieName = 'csrf_refresh_token'
          await axiosInstance.post('/auth/refresh')
          axiosInstance.defaults.xsrfCookieName = 'csrf_access_token'
          return await axiosInstance.get(error.config.url)
        }
        break
      default:
        break
    }
    return Promise.reject(error.config)
  }
)

export default axiosInstance
