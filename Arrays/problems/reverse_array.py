array = [10, 5, 7, 30]

def reverse_array(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])

    return b

if __name__ == '__main__':
    print(reverse_array(array))