class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def reduction(self):
        m = self.gcd(self.numerator, self.denominator)
        return fraction(self.numerator // m, self.denominator // m)

    def add(self, other):
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator).reduction()

    def trans(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"


a, b, c, d = map(int, input().split())
fraction_1 = fraction(a, b)
fraction_2 = fraction(c, d)
fraction_3 = fraction_1.add(fraction_2)
result = fraction_3.trans()
print(result)
