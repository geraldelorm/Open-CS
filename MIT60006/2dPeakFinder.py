# solution  https://www.geeksforgeeks.org/find-peak-element-2d-array/

#  did is for 1D, can build up from here
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

numbers = [[1, 3, 20], [4, 1, 0], [7, 6, 3]]
print(peakFinder(numbers))