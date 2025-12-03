def total_sum(arr):
    #initialize the total 
    total = 0
    #add each element in the array to the total 
    for i in arr:
        total += i
    return total

my_arr = [1,2,3,4,5,6,7,8,9,10]
print(total_sum(my_arr))