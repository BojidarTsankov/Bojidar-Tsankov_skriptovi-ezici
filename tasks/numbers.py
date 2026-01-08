import math


class Compute:
    def __init__(self):
        pass

    def factorial(self, n):
        print(math.factorial(n))

    def sum(self, n):
        total = 0
        for i in range(1, n+1):
            total += i

        print(total)

    def tableMult(self, n):
        for i in range(1, 11):
            print(f"{i} * {n} = {i*n}")

    def listDiv(self, n):
        div = []

        for i in range(1, n+1):
            if n % i == 0:
                div.append(int(i))

        print(div)


Computation = Compute()

Computation.factorial(5)
Computation.sum(5)
Computation.tableMult(5)
Computation.listDiv(5)
