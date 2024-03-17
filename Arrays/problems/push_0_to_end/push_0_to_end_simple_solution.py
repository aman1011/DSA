array = [8, 5, 0, 10, 0 ,20]


def push_0_to_end(a):
    count = 0
    length = len(a)
    for i in range(0, length):
        if a[i] != 0:
            a[count] = a[i]
            count = count + 1


    # lets add back 0 at the end.
    while count < length:
        a[count] = 0
        count += 1

    return a

if __name__ == '__main__':
    modified_array = push_0_to_end(array)
    print(modified_array)
