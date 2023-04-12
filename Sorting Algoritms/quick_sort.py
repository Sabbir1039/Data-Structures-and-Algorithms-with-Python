def partition(A, start, end):
    pivot = A[end]
    pIndex = start

    for i in range(start,end):
        if(A[i] <= pivot):
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex = pIndex + 1
    A[pIndex], A[end] = A[end], A[pIndex]
    return pIndex


def quick_sort(A, start, end):
    if(start < end):
        pIndex = partition(A, start, end)
        quick_sort(A, start, pIndex-1)
        quick_sort(A, pIndex+1, end)
    return


if __name__ == "__main__":
    arr = [7, 3, 4, 1, 5, 6, 2]
    n = len(arr)
    start = 0
    end = n-1
    quick_sort(arr, start, end)
    print(arr)