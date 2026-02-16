# Write a Python class to reverse a string word by word.  

# Input string : 'hello .py' Expected Output : '.py hello'  
class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
reverser = StringReverser()
print(reverser.reverse_words('hello .py'))
