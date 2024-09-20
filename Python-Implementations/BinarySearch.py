def binarySearch(array, item):
    low = 0
    high = len(array) - 1

    while low < high:
        middle = (low + high) // 2
        guess = array[middle]

        if guess == item:
            return middle

        elif guess < item:
            low = middle + 1

        elif guess > item:
            high = middle - 1

    return None


def main():
    array = [1, 5, 10, 15, 20, 35, 55, 100, 120, 200, 230]
    item = int(input("Enter the item you want to search for: "))
    result = binarySearch(array, item)
    if result is not None:
        print(f"The item you were looking for is at index {result} of the list.")
    else:
        print("The item was not found in the list.")


main()
