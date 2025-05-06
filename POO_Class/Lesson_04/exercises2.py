class ticket:
    def __init__(self):
        self.day = "sun"
        self.hour = 18
    def ticketPrice(self):
        price = 16
        if self.day == "sun" or self.day == "sat" or self.day == "fri":
            price = 20
        elif self.day == "mon" or self.day == "tue" or self.day == "thu":
            price = 16
        elif self.day == "wed":
            price = 8
        if not self.day == "wed" and self.hour >= 17 or self.hour == 0:
            price = price * 1.5
        return price
            


x = ticket()
x.day = "wed"
x.hour = 17
print(x.ticketPrice())