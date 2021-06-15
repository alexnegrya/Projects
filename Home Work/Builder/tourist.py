class Tourist:
    def __init__(self, name, age):
        if len(name) >= 3:
            self.name = name
        else:
            raise ValueError('minimum name lenght must be 3 symbols')
        if age >= 1:
            self.age = age
        else:
            raise ValueError('wrong age value')

    def __str__(self):
        return f"{self.name} ({self.age} years)"     # e.g. "John Doe (31years)"
