from money import Money

_destinations = (
    {"name": "Greece", "price": Money(100, "EUR")},
    {"name": "France", "price": Money(120, "EUR")},
    {"name": "Italy", "price": Money(200, "EUR")},
    {"name": "USA", "price": Money(300, "USD")}
)

class _Tour:
    def __init__(self, destination, name, tourists, period):
        self.destination = destination
        self.name = name
        self.tourists = tourists
        self.period = period
        self.cost = self.calculateCost()

    def calculateCost(self):
        self.cost = 0
        for c in range(len(self.tourists)):
            if self.tourists[c].age in range(7, 16):
                procent = 75
            elif self.tourists[c].age <= 6:
                procent = 50
            else:
                procent = 0
            if self.destination == 'Greece':
                value = 100
                self.currency = 'EUR'
            elif self.destination == 'France':
                value = 120
                self.currency = 'EUR'
            elif self.destination == 'Italy':
                value = 200
                self.currency = 'EUR'
            elif self.destination == 'USA':
                value = 300
                self.currency = 'USD'
            if procent != 0:
                self.cost += value / 100 * procent
            else:
                self.cost += value
        return self.cost

    def __str__(self):
        destination = f"Destination: {self.destination}"
        name = f"\nName: {self.name}"
        tourists = '\nTourists:'
        for t in range(len(self.tourists)):
            tourists = tourists + f"\n{t + 1}) Name: {self.tourists[t].name}; Age: {self.tourists[t].age}"
        period = f"\nPeriod: {self.period.start} - {self.period.end}"
        cost = f"\nCost: {int(self.cost)} {self.currency}"
        output = destination + name + tourists + period + cost
        return output

class TourBuilder:
    def __init__(self, destination, name, tourists, period):
        self._tour = _Tour(destination, name, tourists, period)

    def withEnsurance(self):
        self._tour.ensurance = True
        self._tour.cost += self._tour.cost / 100 * 5
        return self

    def withGuide(self):
        self._tour.guided = True
        self._tour.cost += 100
        return self

    def build(self):
        return self._tour
    