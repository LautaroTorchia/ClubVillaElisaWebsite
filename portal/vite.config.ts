import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Club Deportivo Villa Elisa',
        short_name: 'CDVE',
        description: 'Club Deportivo Villa Elisa. Camino Centenario y 48',
        theme_color: '#ffffff',
        lang: 'es',
        icons:[
          {
            src:'cdve-192x192.png',
            sizes:'192x192',
            type:'image/png'
          },
          {
            src:'cdve-512x512.png',
            sizes:'512x512',
            type:'image/png'
          },
        ]
      },
    }),
    vue(),
  ],
})
