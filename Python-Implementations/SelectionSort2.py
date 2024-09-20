def selectionSort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array


print(selectionSort([3, 4, 2, 5, 1, 8, 7, 9]))
