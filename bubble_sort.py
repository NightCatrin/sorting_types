#Сортировка пузырьком
import random

num = 100
array = []
for i in range(num):
    array.append(i)
random.shuffle(array)

print(array)

for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print(array)