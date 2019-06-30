import time
import numpy as np

# def lookupArrays(arrays, lookups):
#     for i in lookups:
#         _ = a[i]

# def lookupLists(lists, lookups):
#         _ = lists[i]


print('preparing...')

length = 1000000
numtests = 10

listtotime = []

for i in range(numtests):
    listtotime.append([np.random.random() for i in range(length)])
arraystotime = [np.array(i) for i in listtotime]

lookups = np.array([np.random.randint(0, length-1) for i in range(numtests)])


print('beginning...')

a = time.time_ns()

for i in range(numtests):
    _ = listtotime[i][lookups[i]]

b = time.time_ns()

for i in range(numtests):
    _ = arraystotime[i][lookups[i]]

c = time.time_ns()


print('arrays took {} ns\nlists took {} ns\nlength: {} \nnumtests:{}'.format(c-b, b-a, length, numtests))

