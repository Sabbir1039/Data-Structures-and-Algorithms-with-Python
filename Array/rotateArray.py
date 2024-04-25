# Given array left roatation n times

# method 1
def leftRotation(arr, n):
    for _ in range(n):
        first = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = first
    return


def reverseArray(arr, start, end):
    mid = (end-start) // 2
    
    for i in range(mid+1):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
        

# method 2
def leftRotation2(arr, n):
    reverseArray(arr, 0, len(arr)-1)
    reverseArray(arr, 0, len(arr)-n-1)
    reverseArray(arr, len(arr)-n, len(arr)-1)
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = 2
    leftRotation2(arr, n)
    print(arr)