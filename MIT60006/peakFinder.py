import math
from operator import indexOf
# Non efficient = complexity of O(n)

# def peakFinder(array: list):
#     for idx in range(len(array)):
#         if array[idx] >= array[idx + 1] and array[idx] >= array[idx - 1]:
#             return array[idx]

# Efficient solution with divide and conquer = complexity of O(logN)
def peakFinder(array: list):
    if len(array) == 0:
        return "No peak"
    elif len(array) == 1:
        return array[0]

    midIndex = int((len(array) -1 )/2)
    leftHalf = array[0:midIndex]
    rightHalf = array[midIndex + 1: len(array)]
    if array[midIndex - 1] > array[midIndex]:
        peakFinder(leftHalf)
    elif array[midIndex + 1] > array[midIndex]:
        peakFinder(rightHalf)
    else: return array[midIndex]

numbers = [1, 3, 20, 4, 1, 0]
print(peakFinder(numbers))