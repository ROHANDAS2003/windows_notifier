import win10toast
import time

toaster = win10toast.ToastNotifier()

while True:
    toaster.show_toast("Water Time", "It's Time To Drink Water!", duration=10)
    # Wait for 1 hour before showing the next notification
    time.sleep(3600)  # 3600 seconds = 1 hour
