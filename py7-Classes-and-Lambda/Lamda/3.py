a1 = [ {'make': 'Nokia', 'model': 216, 'color': 'Black'},{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_phones = sorted(a1, key=lambda d: d['make'])
print(sorted_phones)

