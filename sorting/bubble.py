import random
import time
import matplotlib.pyplot as plt
NO_ITER = 0


def bubble_sort(list_of_num):
    global NO_ITER
    swap = True
    counter = 0
    while swap:
        NO_ITER += 1
        swap = False
        for j in range(len(list_of_num) - 1 - counter):
            NO_ITER += 1
            if list_of_num[j] > list_of_num[j + 1]:
                swap = True
                list_of_num[j], list_of_num[j + 1] = list_of_num[j + 1], list_of_num[j]  # swap
        counter += 1
    return list_of_num


rand_nums = [random.randrange(0, 5000) for i in range(5000)]
times = []
for i in range(0, 5000, 100):
    start_time = time.time()
    nums_to_sort = rand_nums[:i]
    sorted_list = bubble_sort(rand_nums[:i])
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
#print(bubble_sort(rand_nums))
print(NO_ITER)
print(times)
# Visualizing time complexity
x = [i for i in range(0, 5000, 100)]
plt.xlabel('No of elements')
plt.ylabel('Time required')
plt.plot(x, times)
plt.show()
