# Fraction = numerator / denominator


# Greatest Common Divisor (GCD) for simplifying fractions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Least Common Multiple (LCM) for finding a common denominator
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def parse_fraction(s):
    numerator, denominator = map(int, s.split("/"))
    return Fraction(numerator, denominator)


def fraction_to_string(frac):
    return f"{frac.numerator}/{frac.denominator}"


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        # move sign bit to numerator for mathematical consistency
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1


def add_fraction(frac1, frac2):
    lcm_demon = lcm(frac1.denominator, frac2.denominator)
    new_num1 = frac1.numerator * (lcm_demon // frac1.denominator)
    new_num2 = frac2.numerator * (lcm_demon // frac2.denominator)
    result = Fraction(new_num1 + new_num2, lcm_demon)
    result.simplify()
    return result


def subtract_fraction(frac1, frac2):
    lcm_demon = lcm(frac1.denominator, frac2.denominator)
    new_num1 = frac1.numerator * (lcm_demon // frac1.denominator)
    new_num2 = frac2.numerator * (lcm_demon // frac2.denominator)
    result = Fraction(new_num1 - new_num2, lcm_demon)
    result.simplify()
    return result
