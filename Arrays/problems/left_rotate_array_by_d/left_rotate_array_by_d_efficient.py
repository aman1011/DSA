array = [1,2,3,4,5]

def left_rotate_array_by_d(a, d):
    reverse_between_two_indexes(0, d, a)
    reverse_between_two_indexes(d, len(a), a)
    reverse_between_two_indexes(0, len(a), a)

    return a


def reverse_between_two_indexes(first, last, arr):
    count = 0
    for i in range(first , first + (last- first) // 2):
        target = last - 1 - count
        temp = arr[i]
        arr[i]= arr[target]
        arr[target]  = temp

        count += 1

    print(arr)



if __name__ == '__main__':
    new_modfied_array = left_rotate_array_by_d(array, 2)
    print(new_modfied_array)
