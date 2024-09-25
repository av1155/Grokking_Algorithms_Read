def merge_sort(array):
    # Base case: return if the array is empty or has one element
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left = array[:mid]  # Left part
    right = array[mid:]  # Right part

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # At this point, both 'left' and 'right' are sorted, so merge them
    return merge(left, right)


def merge(left, right):
    result = []
    L = R = 0

    # Merge the two sorted arrays
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            result.append(left[L])
            L += 1
        else:
            result.append(right[R])
            R += 1

    # If there are remaining elements in either left or right, append them
    result.extend(left[L:])
    result.extend(right[R:])

    return result


print("[2, 6, 5, 1, 7, 4, 3]")
print(merge_sort([2, 6, 5, 1, 7, 4, 3]))
