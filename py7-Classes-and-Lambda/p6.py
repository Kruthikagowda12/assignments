# Write a Python class to implement pow(x, n)  
class PowerCalculator:
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.pow(x, -n)
        elif n % 2 == 0:
            half_pow = self.pow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.pow(x, n - 1)
calculator = PowerCalculator()
print(calculator.pow(3, 10))  