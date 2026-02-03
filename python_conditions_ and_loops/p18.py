even_numbers = []
odd_numbers = []
prime_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)

