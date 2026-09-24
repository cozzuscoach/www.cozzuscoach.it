self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
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
