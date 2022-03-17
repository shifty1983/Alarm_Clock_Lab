import time

class AlarmClock:
    def __init__(self, alarm_on):
        self.current_time = "00:00 AM"
        self.alarm_on = alarm_on
        self.alarm_set = "00:00 AM"

    def set_current_time(self):
        t = time.localtime()
        self.current_time = time.strftime("%I:%M %p", t)
        print(self.current_time)
    
    def toggle_on_off(self):
        if self.alarm_on == "ON":
            self.alarm_on = "OFF"
        else:
            self.alarm_on = "ON"
        print(self.alarm_on)

    def set_alarm_time(self):
        self.alarm_time= input("Set alarm in format 00:00 AM/PM ")
        print(self.alarm_time)

