# Bubble sort algorithm implementation
def bubble_sort(A):
    n = len(A)
    for k in range(1, n-1):
        flag = 0
        for i in range(n-k):
            if(A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
                flag = flag + 1
        if(flag == 0):
            break
    return


# Main function
if __name__ == "__main__":
    arr = [7, 2, 4, 1, 5, 3]
    arr2 = [1, 2, 3, 4, 5, 6, 7] #for alredy sorted list testing
    bubble_sort(arr)
    print(arr)