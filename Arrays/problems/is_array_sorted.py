array = [8,12,5]


def is_array_sorted(a):
    if len(a) == 1:
        return True

    for i in range(0, len(a) - 1):
        if a[i] > a[i+1]:
            return False

        return True

if __name__ == '__main__':
    print(is_array_sorted(array))
