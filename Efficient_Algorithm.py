#Muhammad Irsyad Jazli Bin Ramli, 223890U, Tutorial Group 1
def algorithm(array, z, lowerbound, upperbound):
    # Base Case 1 - array of 1 or less elements
    if lowerbound >= upperbound:
        return False

    # Base Case 2 - current 2 numbers match
    if array[lowerbound] + array[upperbound] == z:
        return True

    # Recursive Case - Check other algorithms
    if array[lowerbound] + array[upperbound] < z:
        return algorithm(array, z, lowerbound + 1, upperbound)

    if array[lowerbound] + array[upperbound] > z:
        return algorithm(array, z, lowerbound, upperbound - 1)


if __name__ == "__main__":
    array1 = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]

    print(algorithm(array1, 21, 0, len(array1) - 1))
    print(algorithm(array1, 27, 0, len(array1) - 1))