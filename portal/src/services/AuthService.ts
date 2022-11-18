import axios from 'axios'

const authService = axios.create({
  baseURL: import.meta.env.PROD
    ? 'https://admin-grupo12.proyecto2022.linti.unlp.edu.ar/api/auth'
    : 'http://localhost:5000/api/auth',
  withCredentials: true,
  xsrfCookieName: 'csrf_access_token',
})
const COOKIE_EXPIRED_MSG = 'Token has expired'

authService.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const error_message = error.response.data.msg
    console.log(error_message)
    switch (error.response.status) {
      case 401:
        if (!error.config.retry && error_message === COOKIE_EXPIRED_MSG) {
          error.config.retry = true
          authService.defaults.xsrfCookieName = 'csrf_refresh_token'
          await authService.post('/refresh')
          authService.defaults.xsrfCookieName = 'csrf_access_token'
          return authService(error.config)
        }
        break
      default:
        break
    }
    return error.response
  }
)

export { authService }
