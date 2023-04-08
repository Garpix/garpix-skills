import viteFile from './vite.svg'

const isDev = import.meta.env.DEV

const getUrl = (url: string) => new URL(url, isDev ? "http://localhost:3001" : window.location.href).href;

const viteIcon = getUrl(viteFile)

export {
  viteIcon
}