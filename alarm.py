import time
import datetime

print("Simple Alarm Program")

alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set to:", alarm_time)

while True:

    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M")

    if current_time == alarm_time:
        print("Alarm Ringing!")
        print("Wake up!")
        break

    time.sleep(1)





