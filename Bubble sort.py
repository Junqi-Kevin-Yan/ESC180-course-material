# compare adjacent elements and swap 
def bubble_sort(arr):
    n = len(arr)
    # thru all array elements
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n-1-i):
            # swap if ele found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

# outer loop runs n times, n length of array
# inner loop decrease in size each time, n-1, n-2..
# in worst case, end up doing appox n(n-1)/2 comparisons and swaps, which simplfies to O(n^2)
# for n=5, number of comparison 4+3+2+1 = 10, close to 5x4/2
# O(n^2): (reverse sorted 54321) each element is compared with every other element 