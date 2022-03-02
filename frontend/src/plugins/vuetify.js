// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import * as components from 'vuetify/lib/components'
import * as directives from 'vuetify/lib/directives'
// Vuetify
import { createVuetify } from 'vuetify'

const vuetify = createVuetify({
  components,
  directives,
  defaults: {
    global: {
      ripple: false,
    },
    VSheet: {
      elevation: 4,
    },
  },
})

export default vuetify