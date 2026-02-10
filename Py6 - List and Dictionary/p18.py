def func(lst):
    return all(isinstance(d, dict) and not d for d in lst)
print(func([{}, {}]))   
print(func([{1: 2}, {}, {}]))  
