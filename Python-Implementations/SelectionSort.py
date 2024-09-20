def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallest_index = i

    return smallest_index


def selectionSort(array):
    newArray = []
    copiedArray = list(array)

    for i in range(len(copiedArray)):
        smallest = findSmallest(copiedArray)
        newArray.append(copiedArray.pop(smallest))

    return newArray


print(selectionSort([64, 25, 12, 22, 11, 1, 5, 19]))
