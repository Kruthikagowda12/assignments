numbers = list(range(1, 101))
divisors = [4, 6, 8, 10, 3, 5, 7, 9]

for d in divisors:
    print(f"Numbers divisible by {d}:",
          [n for n in numbers if n % d == 0])
