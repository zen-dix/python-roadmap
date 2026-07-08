class TimeInterval:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        if self.minutes // 60 > 0:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

    def __add__(self, t2):
        if not isinstance(t2, TimeInterval):
            return NotImplemented
        return TimeInterval(self.hours + t2.hours, self.minutes + t2.minutes)

    def __lt__(self, t2):
        if not isinstance(t2, TimeInterval):
            return NotImplemented
        return (self.hours * 60 + self.minutes) < (t2.hours * 60 + t2.minutes)


t1 = TimeInterval(hours=1, minutes=45)
t2 = TimeInterval(hours=0, minutes=30)

t3 = t1 + t2
print(str(t3))

print(t1 < t2)
