# Function for insertion sort
def insertion_sort(A,n):
    for i in range(1,n):
        value = A[i]
        hole = i

        while (hole > 0 and A[hole-1] > value):
            A[hole] = A[hole-1]
            hole = hole-1
        A[hole] = value
    return

# main function
if __name__ == "__main__":
    arr = [7, 2, 4, 1, 5, 3]
    size_of_arr = len(arr)

    insertion_sort(arr,size_of_arr)
    print(arr)