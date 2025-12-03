def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
        
my_array = [1,3,5,7,9,11,13]
print(binary_search(my_array, 9))

#Time Complexity - O(log n)
#Space Complexity - O(1)