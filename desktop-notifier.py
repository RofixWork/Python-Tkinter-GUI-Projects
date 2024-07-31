from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="first message",
            app_icon='./notify.ico',
            timeout=5
        )
        time.sleep(3600)