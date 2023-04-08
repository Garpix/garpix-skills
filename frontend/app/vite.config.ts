import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  css: {
    devSourcemap: true,
  },
  build: {
    sourcemap: true,
    manifest: true, // adds a manifest.json
    rollupOptions: {
      input: [
        'src/main.tsx',
      ],
    },
    outDir: '../static/build',
    assetsDir: 'static-backend',
  },
  plugins: [
    react({ fastRefresh: false }),
  ],
  server: {
    port: 3001, // make sure this doesn't conflict with other ports you're using
    open: false,
  }
})
