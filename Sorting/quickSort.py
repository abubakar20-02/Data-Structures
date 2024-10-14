def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def pivot(arr, pivot, end):
    correctPos = pivot

    for index in range(pivot + 1, end + 1):
        if arr[index] < arr[pivot]:
            correctPos += 1
            swap(arr,index, correctPos)
    swap(arr,pivot, correctPos)
    return correctPos

def quickSortHelper(arr,left,right):
    if left < right:
        pivotIndex = pivot(arr,left,right)
        quickSortHelper(arr,left, pivotIndex-1)
        quickSortHelper(arr, pivotIndex + 1, right)
    return arr

def quickSort(arr):
    return quickSortHelper(arr,0,len(arr)-1)


if __name__ =="__main__":
    print(quickSort([2,5,3,1,5,6,7,8,9,2,4,5,6]))
