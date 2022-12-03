import random

num = 100
array = []
for i in range(num):
    array.append(i)
random.shuffle(array)

step = int(len(array)/1.247)

while step > 0:
    for i in range(len(array) - 1):
        if i + step - 1 >= 10:
            break
        if array[i] > array[i+step-1]:
            array[i], array[i+step-1] = array[i+step-1], array[i]
    step_num = int(step/1.247)
    step = step_num

    if step == 1:
        for i in range(len(array) - 1):
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

print(array)