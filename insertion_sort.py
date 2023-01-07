#Сортировка вставками
import random

num = 100
array = []
for i in range(num):
    array.append(i)
random.shuffle(array)

for i in range(1, len(array)):
    current = array[i]
    prev_cur = i - 1

    while prev_cur >= 0 and array[prev_cur] > current:
        array[prev_cur + 1] = array[prev_cur]
        prev_cur -= 1
        array[prev_cur+1] = current

print(array)