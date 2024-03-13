array = [10, 20, 20, 30, 30, 30, 30]

def remove_duplicate_from_array(a):
    result_index = 0

    for i in range(1, len(a)):
        if a[result_index] != a[i]:
            a[result_index + 1] = a[i]
            result_index = result_index + 1

    return result_index


if __name__  == '__main__':
    size = remove_duplicate_from_array(array) + 1
    print(size)