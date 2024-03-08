a = [10, 5, 20, 8]

def largest_element(a):
    largest_element = -1
    if a:
        for i in range(0, len(a)):
            if a[i] > largest_element:
                largest_element = a[i]

    return largest_element

if __name__ == '__main__':
    print(largest_element(a))