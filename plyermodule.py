import time
from plyer import notification

seconds = 2

while True:
    time.sleep(seconds)
    notification.notify(title = "water",
                        message = "you should drink water",
                        timeout = 2)
