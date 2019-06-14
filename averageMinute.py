class AverageMinute:
    def __init__(self, minute, average):
        self.minute = minute
        self.average = average

    def draw(self):
        print(f"AverageMinute, minute: {self.minute}, {self.average}")
