dict1 = {
    "1,3": "9999",
    "1,4": "test2",
    "1,5": "test3"}

key = list(dict1.keys())
print(key)
for i in key:
    line = i.split(',')[0]
    col = i.split(',')[1]
    print(f'line:{line}')
    print(f'col:{col}')



