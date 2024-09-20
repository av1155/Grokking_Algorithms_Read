def selectionSort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Store the larger current value of i
        temp = array[i]
        # Replace the larger current value of i with the new smallest value found
        array[i] = array[min_index]
        # Replace the still existing smallest value found, with the larger current value of i
        array[min_index] = temp

    return array


print(selectionSort([3, 4, 2, 5, 1, 8, 7, 9]))
