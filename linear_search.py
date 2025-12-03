def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        

my_array = [2,5,7,10,14,20]   
print(linear_search(my_array, 10))

#Time Complexity - O(n)
#Space Complexity - O(1)