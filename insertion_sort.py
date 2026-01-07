def insertion_sort(arr):
    #we start from 1 because we assume the first element(index 0) is already sorted
    for i in range(1, len(arr)):
        #the key stores the element to be sorted 
        key = arr[i]
        #this implements a pointer to the last element
        #of the sorted portion for backward comparison
        j = i - 1
        while j >= 0 and arr[j] > key:
            #no swapping, only shifting 
            arr[j+1] = arr[j]
            #moves the pointer left so that the key can be compared 
            #with the earlier elements in the sorted portion
            j = j - 1
        arr[j+1] = key 
    return arr


print(insertion_sort([5,8,16,10,3,1,4]))


#Time complexity:
#Best: O(n)
#Average: O(n²) 
#Worst: 0(n²)

#Space complexity - O(1)

