def intersection(arrays):
    length = len(arrays)
    cache = {}

    for arr in arrays:
      for num in arr:
        if num not in cache:
          cache[num] = 1
        else:
          cache[num] += 1

    result = []

    for item in list(cache.items()):
      if item[1] == length:
        result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


# Initial Pass
    # result = []
    # temp = []
    # count = 0

    # for i in arrays:
    #     temp += i

    # for x in temp:
    #     count += 1
    #     for y in temp:
    #         if x == y:
    #             count += 1

    #         if count >= 3:
    #             result.append(x)
    #     count = 0

    #     result = list(dict.fromkeys(result))