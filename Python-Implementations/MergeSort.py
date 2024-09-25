def merge_sort(array):
    # Recursion to reduce left and right arrays to size 1. When this condition is true,
    # the left array will complete splitting, and the right array will start.
    # When the right array also meets the condition, then they will move on to call
    # the merge function.
    if len(array) <= 1:
        return array

    # Split the array in two and create two subarrays for left and right side.
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively split left and right arrays until the size is 1
    left = merge_sort(left)
    right = merge_sort(right)

    # Return the sorted array that the merge function will return with the splitted left and right arrays.
    return merge(left, right)


def merge(left, right):
    result = []  # Empty array so we can add the sorted elements one by one.

    L = R = 0  # Initialize the indexes for the left and right array.

    # Find the smallest and append it to the results array until L or R indexes make the condition false.
    # The reasoning is that at some point, left or right will have still one element which has not been
    # checked yet, but we have nothing else to check it with. This "and" condition allows us to exit
    # early so that we can simply append whatever is left on that array to the end of the results array.
    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            result.append(left[L])
            L += 1
        else:
            result.append(right[R])
            R += 1

    # This is where we append whatever was left on that left or right side that we could not compare to anything.
    result.extend(left[L:])
    result.extend(right[R:])

    # Return the sorted array to the merge_sort() function.
    return result


print("[2, 6, 5, 1, 7, 4, 3]")
print(merge_sort([2, 6, 5, 1, 7, 4, 3]))
