a = [20, 5, 7, 25]


def search(number, a):
    for i in range(0, len(a)):
        if a[i] == number:
            return i
    
    return -1


if __name__ == '__main__':
    print(search(7, a))
    print(search(23, a))


