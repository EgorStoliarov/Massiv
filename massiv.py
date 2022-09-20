import random
array = [random.randint(1,100) for i in range(10)]
print(array)
min1 = min(array)
array.remove(min1)
min2 = min(array)
print(min1, min2)





