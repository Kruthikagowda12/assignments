# Write a python class to convert an integer into a roman numeral and viceversa
class RomanConverter:
 
    def int_to_roman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]
 
        result = ""
 
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
 
        return result
 
 
    def roman_to_int(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000}
 
        total = 0
 
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
 
        return total

obj = RomanConverter()
 
print(obj.int_to_roman(45))     # XLV
print(obj.roman_to_int("XLV"))  # 45

    