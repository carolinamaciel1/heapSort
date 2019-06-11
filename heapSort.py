import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it
from timeit import timeit
from random import randint

# sort by selection. data structure called heap, that is a kind of special binary tree
# min-heap is a kind of heap structure
def heapSort(listToSort):
  for start in range((len(listToSort)-2)//2, -1, -1):
    siftdown(listToSort, start, len(listToSort)-1)

  for end in range(len(listToSort)-1, 0, -1):
    listToSort[end], listToSort[0] = listToSort[0], listToSort[end]
    siftdown(listToSort, 0, end - 1)
  return listToSort

# repair the heap whose root element is at index 'start', assuming the heaps rooted at its children are valid
def siftdown(listToSort, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and listToSort[child] < listToSort[child + 1]:
      child += 1
    if listToSort[root] < listToSort[child]:
      listToSort[root], listToSort[child] = listToSort[child], listToSort[root]
      root = child
    else:
      break

#generate unSorted array with gave lenght
def listGenerator(lenList):
    generated = []
    for i in range(lenList):
        while len(generated) != lenList:
            n = randint(1,1*lenList)
            if n not in generated: generated.append(n)
    return generated

def drawGraph(listQt,medium,best,worst,xl = "Elementos", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(listQt,medium, label = "Caso Medio")
    ax.plot(listQt,best, label = "Melhor Caso")
    ax.plot(listQt,worst, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    fig.savefig('heapSort2.png')

#lenghts to diferent arrays
length = [100,200,300,400,500]
# length = [10000,20000,30000,40000,50000]

#array to store the necessary time to sort each array
mediumTimes = []
bestTimes = []
worstTimes = []

for i in length:
    mediumList = listGenerator(i)
    bestList = sorted(mediumList)
    worstList = sorted(bestList, reverse=True)

    mediumTimes.append(timeit("heapSort({})".format(mediumList),setup="from __main__ import heapSort",number=1))
    bestTimes.append(timeit("heapSort({})".format(bestList),setup="from __main__ import heapSort",number=1))
    worstTimes.append(timeit("heapSort({})".format(worstList),setup="from __main__ import heapSort",number=1))

drawGraph(length, mediumTimes, bestTimes, worstTimes)

# Verify the worst case
worstCaseExperience = list(it.permutations([1,2,3,4,5,6],6))

# permutimes and worstcase will have the same len, so the index is equivalent each other
permuTimes = []
swaps = []

for permutation in worstCaseExperience:
    listToSort = list(permutation)
    permuTimes.append(timeit("heapSort({})".format(listToSort),setup="from __main__ import heapSort",number=1))
    swaps.append(heapSort(listToSort))

smallerTime = min(permuTimes)
greaterTime = max(permuTimes)

smallerTimeIndex = permuTimes.index(smallerTime)
greaterTimeIndex = permuTimes.index(greaterTime)

# worst case list
print("May be the worst: {}".format(worstCaseExperience[smallerTimeIndex]))
print("May be the best: {}".format(worstCaseExperience[greaterTimeIndex]))
print(swaps)
