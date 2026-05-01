self.addEventListener("install", function (event) {
  console.log("AbleBot service worker installed.");
});

self.addEventListener("fetch", function (event) {
  event.respondWith(fetch(event.request));
});