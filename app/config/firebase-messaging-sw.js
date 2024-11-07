self.addEventListener("notificationclick", function (event) {
    console.log("[firebase-messaging-sw.js] Notification click Received.", event);

    event.notification.close();

    event.waitUntil(
        clients.openWindow("http://127.0.0.1:8000/users/send-notification")
    );
});

self.addEventListener("push", function (event) {
    const notif = event.data.json().notification;
    event.waitUntil(
        self.registration.showNotification(notif.title, {
            body: notif.body,
            icon: notif.icon,
            data: {
                url: notif.click_action
            }
        })
    );
});