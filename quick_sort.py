def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot ]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right) 

print(quick_sort([5,8,16,10,3,1,4]))


#Time complexity:
#Best: O(n log n)
#Average: O(n log n) 
#Worst: 0(n²)

#Space complexity - O(log n)
