array = [10, 20, 20, 30, 30, 30, 30]

def remove_duplicate_from_array(a):
    total_to_remove = 0
    for i in range(0, len(a) - 1):
        if a[i] is not None:
            for j in range(i+1, len(a)):
                if a[i] == a[j]:
                    a[j] = None
                    total_to_remove = total_to_remove + 1
                    print(total_to_remove)


    return a, len(a) - total_to_remove

if __name__  == '__main__':
    modified_array, size = remove_duplicate_from_array(array)
    print(modified_array)
    print(size)