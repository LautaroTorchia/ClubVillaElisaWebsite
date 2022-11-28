/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import specific icons */
import {
  faHome,
  faPhone,
  faTimesCircle,
  faTimes,
} from '@fortawesome/free-solid-svg-icons'
import {
  faFacebook,
  faTwitter,
  faInstagram,
} from '@fortawesome/free-brands-svg-icons'

/* add icons to the library */
library.add(faHome, faPhone, faFacebook, faTwitter, faInstagram, faTimes)
