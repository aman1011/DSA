array = [1,2,3,4,5]

def left_rotate_array_by_d(a, d):

    d = d % len(a)
    count = 0
    while count < d:
        first_elem = a[0]
        for i in range(0, len(a) - 1):
            a[i] = a[i+1]

        a[len(a) - 1] = first_elem

        count += 1

    return a


if __name__ == '__main__':
    new_modified_array = left_rotate_array_by_d(array, 3)
    print(new_modified_array)