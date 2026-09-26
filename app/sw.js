// Cozzu's Coach - service worker
// La pagina viene sempre richiesta alla rete: la copia salvata serve solo offline.
const CACHE = "cc-v2";

self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
  await self.clients.claim();
})()));

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;              // Supabase e font: nessuna cache
  if (req.mode === "navigate" || url.pathname.endsWith(".html") || url.pathname.endsWith("/")) {
    e.respondWith((async () => {
      try {
        const fresh = await fetch(req, { cache: "no-store" });
        const c = await caches.open(CACHE); c.put(req, fresh.clone());
        return fresh;
      } catch (_) {
        return (await caches.match(req)) || (await caches.match("/app/")) || Response.error();
      }
    })());
  }
});

self.addEventListener("push", e => {
  let d = {};
  try { d = e.data ? e.data.json() : {}; } catch (_) { d = { title: "Cozzu's Coach", body: e.data && e.data.text() }; }
  e.waitUntil(self.registration.showNotification(d.title || "Cozzu's Coach", {
    body: d.body || "", icon: "/app/icon-192.png", badge: "/app/icon-192.png",
    data: { url: d.url || "/app/" }, tag: d.tag || "daily"
  }));
});

self.addEventListener("notificationclick", e => {
  e.notification.close();
  const url = (e.notification.data && e.notification.data.url) || "/app/";
  e.waitUntil(self.clients.matchAll({ type: "window", includeUncontrolled: true }).then(list => {
    for (const c of list) if (c.url.includes("/app/") && "focus" in c) return c.focus();
    return self.clients.openWindow(url);
  }));
});
