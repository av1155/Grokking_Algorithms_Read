def binary_search(array, item):
    """
    Perform a binary search on a sorted array to find the index of a specific item.

    Parameters:
    array (list): A sorted list of items to search through.
    item (int): The item to search for in the array.

    Return:
    int: The index of the item in the array if found, None if the item is not in the array.
    """

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == item:
            return mid  # return the index of the found item

        elif guess > item:
            # Set the new high to the middle - 1 (because of 0 indexing, and because we know that at mid there was nothing)
            high = mid - 1

        else:
            # Set the new low to mid + 1 (because of 0 indexing, and because we know that at mid there was nothing)
            low = mid + 1

    return None


array = [1, 3, 6, 7, 10, 12, 7]
print(f"{binary_search(array, 3)}")
# Binary search function found item 3 at index 1 -> 1
print(f"{binary_search(array, -1)}\n")
# Binary search function did not find item -1 -> None

unsortedArray = [7, 3, 2, 9, 21, 0, 1]
print(f"{binary_search(unsortedArray, 7)}")
print(f"{binary_search(unsortedArray, -1)}\n")
