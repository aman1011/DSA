

def find_leader_in_array(a):
    b = [a[-1]]
    largest_from_right = a[-1]
    for i in range(len(a) - 2, -1, -1):
        if (a[i] > largest_from_right):
            b.append(a[i])
            largest_from_right = a[i]

    b.reverse()

    return b


if __name__ == "__main__":
    array = [7, 10, 4, 3, 6, 5, 2]
    leader_array = find_leader_in_array(array)
    print(leader_array)

    array = [10, 20, 30]
    leader_array = find_leader_in_array(array)
    print(leader_array)

    array = [30, 20, 10]
    leader_array = find_leader_in_array(array)
    print(leader_array)

            