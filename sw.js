self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('neuro-app').then(cache => {
      return cache.addAll([
        '/',
        '/index.html',
        '/asconi_json_por_rango/edad_0_3.json',
        // agrega los demás JSON aquí
      ])
    })
  )
})

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(response => response || fetch(e.request))
  )
})
