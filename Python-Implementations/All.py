# BINARY SEARCH ========================: O(log n)
def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == item:
            return mid

        elif guess < item:
            low = mid + 1

        elif guess > item:
            high = mid - 1

    return None


# INSERTION SORT =======================: O(n^2)
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


# SELECTION SORT =======================: O(n^2)
def selection_sort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array


# MERGE SORT ===========================: O(n log n) | Not in-place
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    L = R = 0

    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            result.append(left[L])
            L += 1
        else:
            result.append(right[R])
            R += 1

    result.extend(left[L:])
    result.extend(right[R:])

    return result


# QUICK SORT ===========================: O(n log n) | In-place


# -----------------------------------------------------------------------
def main():
    array_for_search = [1, 3, 6, 7, 8, 11, 13, 15, 21, 27, 33, 34]
    print(
        "Binary Search -> The item was in the index: ",
        binary_search(array_for_search, 27),
    )

    array_to_sort = [5, 2, 8, 12, 1, 6, 3, 21, 11, 99, 10, 12, 9]
    print("Insertion Sort -> ", insertion_sort(array_to_sort.copy()))
    print("Selection Sort -> ", selection_sort(array_to_sort.copy()))
    print("Merge Sort -> ", merge_sort(array_to_sort.copy()))
    # print("Quick Sort -> ", quick_sort(array_to_sort.copy()))


if __name__ == "__main__":
    main()
