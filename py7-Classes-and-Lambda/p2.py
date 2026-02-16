class BalancedChecker:
    def __init__(self):
        self.pairs = {'(': ')', '[': ']', '{': '}'}

    def is_balanced(self, s):
        stack = []

        for char in s:
            if char in self.pairs:
                stack.append(self.pairs[char])

            elif char in self.pairs.values():
                if not stack or stack.pop() != char:
                    return False
            else:
                return False

        return not stack

string = input("Enter string: ")
checker = BalancedChecker()

if checker.is_balanced(string):
    print("Balanced")
else:
    print("Not Balanced")
