import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Daily Reminder",
            message = "It's time to check your emails",
            timeout = 10 #in sec always
        )
        time.sleep(86400)