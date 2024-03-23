

def find_leader_in_array(a):
    b = []
    for i in range(0, len(a) - 1):
        less_found = False
        for j in range(i+1, len(a)):
            if a[i] <= a[j]:
                less_found = True
                break

        if not less_found:
            b.append(a[i])

    # Always append the last element of the original array
    b.append(a[-1])

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

            