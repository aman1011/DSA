array = [10, 5, 20, 28, 22]

"""
"""
def find_second_largest(a):
    largest = 0
    second_largest = 0
    for i in range(0, len(a)):
        if a[i] > largest:
            second_largest = largest
            largest = a[i]
            

        if a[i] < largest and a[i] > second_largest:
            second_largest = a[i]

    # if second largest is 0, then most
    # likely the second largest number does 
    # not exist. Returning -1.
    if second_largest == 0:
        second_largest = -1
    
    return second_largest

print(find_second_largest(array))
