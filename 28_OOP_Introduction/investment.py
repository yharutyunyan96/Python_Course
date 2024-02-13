class Investment:
    def __init__(self, principal: float, interest: float) -> None:
        self.p: float = principal
        self.i: float = interest

    def __str__(self) -> str:
        return f"Principal - ${self.p}, Interest rate - {self.i}%"

    def value_after(self, n: int) -> float:
        return self.p * (1 + self.i) ** n


obj = Investment(1000, 0.0512)
print(obj)

# value after 5 years
result = obj.value_after(5)
print(f"Value after 5 years: ${result:.2f}")