def merge(left, right, A):
    nL = len(left)
    nR = len(right)
    i = j = k = 0

    while(i < nL and j < nR):
        if(left[i] <= right[j]):
            A[k] = left[i]
            i = i+1
        else:
            A[k] = right[j]
            j = j+1
        k = k+1
    while(i < nL):
        A[k] = left[i]
        i = i+1
        k = k+1
    while(j < nR):
        A[k] = right[j]
        j = j+1
        k = k+1
    return

def merge_sort(A):
    n = len(A)
    if(n < 2):
        return
    mid  = int(n/2)
    left = []
    right = []
    for i in range(mid):
        left.append(A[i])
    for j in range(mid, n):
        right.append(A[j])
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)

if __name__ == "__main__":
    arr = [2, 4, 1, 6, 8, 5, 3, 7]
    merge_sort(arr)
    print(arr)