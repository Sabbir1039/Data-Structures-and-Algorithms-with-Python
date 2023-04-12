# Function for selection sort

def selection_sort(A):
    n = len(arr)
    
    for i in range(n-1):
        iMin = i

        for j in range(i+1, n):
            if A[j] < A[iMin]:
                iMin = j
        A[i], A[iMin] = A[iMin], A[i]
    return


# main function
if __name__ == "__main__":
    arr = [7, 2, 4, 1, 5, 3]
    selection_sort(arr)
    print(arr)