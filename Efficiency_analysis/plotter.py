import matplotlib.pyplot as plt
import random as rnd
from time import time

from merge_sort import mergeSort
from selection_sort import selectionSort

def analyse(sorting_func, size, step):

    data = []

    for i in range(0, size+step, step):
        nums = [j for j in range(0, i)]
        rnd.shuffle(nums)
        start = time()

        sorting_func(nums, 0, i-1)

        elapsed = time() - start
        data.append(elapsed)
        print('Array size: %d, time elapsed: %f;' % (i, elapsed))

    return data

# SORTING COMPARISON

size, step = 10000, 1000
steps = [i for i in range(0, size+step, step)]

data_merge = analyse(mergeSort, size, step)
data_selection = analyse(selectionSort, size, step)

plt.plot(steps, data_merge, label='Слиянием')
plt.plot(steps, data_selection, label='Выбором')

plt.title('Сравнение эффективности сортировок')
plt.xlabel('Кол-во элементов в массиве')
plt.ylabel('Затраченное время (секунды)')
plt.legend(loc="upper left")

plt.savefig('comparison.png')

plt.clf()

# MERGE SORT ANALISYS

size, step = 30000, 500
steps = [i for i in range(0, size+step, step)]

data_merge = analyse(mergeSort, size, step)

plt.plot(steps, data_merge, label='Слиянием')

plt.title('Эффективность сортировки слиянием')
plt.xlabel('Кол-во элементов в массиве')
plt.ylabel('Затраченное время (секунды)')
plt.legend(loc="upper left")

plt.savefig('merge.png')

plt.clf()

# SELECTION SORT ANALISYS

size, step = 10000, 300
steps = [i for i in range(0, size+step, step)]

data_merge = analyse(selectionSort, size, step)

plt.plot(steps, data_merge, label='Выбором')

plt.title('Эффективность сортировки выбором')
plt.xlabel('Кол-во элементов в массиве')
plt.ylabel('Затраченное время (секунды)')
plt.legend(loc="upper left")

plt.savefig('selection.png')

plt.clf()