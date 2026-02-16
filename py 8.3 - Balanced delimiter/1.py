def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char not in "()[]{}":
            return False
        
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:   
                return False

            top = stack.pop()
            if top != pairs[char]:
                return False

    return len(stack) == 0


string = input("Enter string: ")
print(is_balanced(string))
