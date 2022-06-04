if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js");
}

self.addEventListener('install', function(event) {
    // The promise that skipWaiting() returns can be safely ignored.
    self.skipWaiting();
  
    // Perform any other actions required for your
    // service worker to install, potentially inside
    // of event.waitUntil();
  });