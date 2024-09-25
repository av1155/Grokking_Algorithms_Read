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


print(merge_sort([7, 3, 2, 16, 24, 4, 11, 9]))
