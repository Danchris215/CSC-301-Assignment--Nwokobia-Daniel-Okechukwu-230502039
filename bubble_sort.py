def bubble_sort (arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr

print(bubble_sort([5,8,16,10,3,1,4]))

#Time complexity:
#Best: O(n)
#Average: O(n²) 
#Worst: 0(n²)

#Space complexity - O(1)
