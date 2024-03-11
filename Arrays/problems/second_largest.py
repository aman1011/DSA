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

    return second_largest

print(find_second_largest(array))
