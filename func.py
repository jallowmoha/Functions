
"""The first_smallest function finds 
the smallest integer in the array"""

def first_smallest(array):
    if len(array) == 0:
        print(" The Array is empty")         
        return False 
    smallest = array[1]
    for num in array:
        if type(num) == int: 
            if  num < int(smallest):
                smallest = num
        else:
            raise TypeError("Only integers are allowed")
           
    return smallest
            
       
    




"""The second_smallest function finds 
the second smallest integer in the array"""


def second_smallest(array):
    if len(array) == 0:
        print(" The Array is empty")        
        return False 
    for num in array:
        if not type(num) is int:
            raise TypeError("Only integers are allowed")
    new_arr = sorted(array)
    second_smallest = new_arr[1]

    return second_smallest



"""The n_smallest function finds 
the n_th smallest integer in the array"""

def n_smallest(array, n):
    if len(array) == 0 or n == 0:
        print(" The Array is empty or n is less than 1")         
        return False 
    for num in array:
        if not type(num) is int:
            raise TypeError("Only integers are allowed")
        if n > len(array):
            raise IndexError("n is out of range")
    new_arr = sorted(array)
    n_smallest = new_arr[n - 1]
    return n_smallest



arr =[]

print(n_smallest(arr, 1))