arr = list(range(0, 100))
print(arr)

points = 19
y = len(arr) / points
print(y)
y = int(round(y, 1))
print(y)

data = []

x = 0

while x < len(arr):
    data.append(arr[x])
    x += y
    
print(data)
print(len(data))