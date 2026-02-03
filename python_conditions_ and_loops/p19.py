even_numbers = [x for x in range(1, 101) if x % 2 == 0]
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
numbers = even_numbers + odd_numbers
 
divisors = [4, 6, 8, 10, 3, 5, 7, 9]
 
for d in divisors:
    divisible = [x for x in numbers if x % d == 0]
    print(f"Numbers divisible by {d}:", divisible)