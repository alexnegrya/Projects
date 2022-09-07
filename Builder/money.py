class Money:
    _currencies = ("MDL", "USD", "EUR", "RUB", "RON")

    def __init__(self, amount, currency):
        if amount > 0: self.amount = amount
        else: raise ValueError('wrong amount value')
        if currency in self._currencies: self.currency = currency
        else: raise TypeError('unsupported type of currency')

    def __str__(self): return f"{self.amount} {self.currency}"
