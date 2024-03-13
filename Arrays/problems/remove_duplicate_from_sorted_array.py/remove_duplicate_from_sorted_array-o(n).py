#array = [10, 20, 20, 30, 30, 30, 30]
array = [10, 10, 10]
def remove_from_srted_array(a):
    i = 0
    j = 1
    total_removed = 0
    while (i < len(a) - 1 and j < len(a)):
        if (a[i] == a[j]):
            a[j] = None
            j = j + 1
            total_removed = total_removed + 1
        elif a[i] is None:
            i = i + 1
        else:
            i = i + 1
            j = j + 1

    return a, len(a) - total_removed


if __name__ == '__main__':
    modified_array, size = remove_from_srted_array(array)
    print(modified_array)
    print(size)
