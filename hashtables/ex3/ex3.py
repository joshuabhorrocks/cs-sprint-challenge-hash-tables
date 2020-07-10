def intersection(arrays):
    result = []
    temp = []
    count = 0

    print("arrays: ", arrays)
    for i in arrays:
        temp += i

    for x in temp:
        count += 1
        for y in temp:
            if x == y:
                count += 1
                
            if count >= 3:
                result.append(x)
        count = 0

        result = list(dict.fromkeys(result))

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays.append(list(range(4, 6)) + [1, 2, 3])
    arrays.append(list(range(7, 9)) + [1, 2, 3])
    arrays.append(list(range(10, 12)) + [1, 2, 3])

    print(intersection(arrays))
