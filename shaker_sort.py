import random

num = 100
array = []
for i in range(num):
    array.append(i)
random.shuffle(array)

a = 0
b = len(array)-1

while a <= b:
    for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    for i in range(len(array)-2, -1, -1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    a +=2

print(array)