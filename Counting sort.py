'''
[4, 2, 2, 8, 3, 3, 1]
max value is 8, need a count array of size 9
initialize count 
[0, 0, 0, 0, 0, 0, 0]

after count
index: 0, 1, 2, 3, 4, 5, 6, 7, 8
value:[0, 1, 2, 2, 1, 0, 0, 0, 1]

cumulate count: add the count of each index with all previous counts
index: 0, 1, 2, 3, 4, 5, 6, 7, 8
value:[0, 1, 3, 5, 6, 6, 6, 6, 7]
for example, count[3] = 5, meaning last occurance of value 3 will be at index 5, or 6th position
**there are five elements in the input array that are less than or equal to 3

Sorted array is: [1, 2, 2, 3, 3, 4, 8]

after placing the first 3 at index 4 of the output array, we decrement count[3] to 4. 
This means that the next 3 we encounter will be placed at index 4 - 1 = 3 in the output array

'''

def counting_sort(arr):
    # find max element 
    max_val = max(arr)
    # initialize count array with all zeros 
    count = [0] * (max_val + 1)
    # store count of each element 
    for num in arr:
        count[num] += 1 # counts occurance of each number in input array
    # store cumulative count 
    for i in range(1, len(count)):
        count[i] += count[i-1] # iterate count array and add count of the current index to count of previous index 
    # find index of each element in origional array in count array
    # place elements in output array 
    output = [0] * len(arr)
    for num in arr:
        output[count[num]-1] = num  # for each num, place elem in correct position in output array
        count[num] -= 1 
    return output 

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array is:", sorted_arr)

# O(n+k): n the number of element in input array and k is range of input value 


