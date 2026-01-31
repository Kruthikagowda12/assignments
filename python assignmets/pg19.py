s = "hi this is kruthika"
words = s.split()   
smallest = min(words, key=len)
largest = max(words, key=len)
print("Smallest word:", smallest)
print("Largest word:", largest)
