def sort(list):
    for i in range(len(list) - 1):
        sorted = True
        for j in range((len(list) - 1) - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                sorted = False
        if sorted:
            return list
    return list


if __name__ == "__main__":
    list = [2, 3, 1, 2, 4, 5, 6, 4, 3, 6, 8, 8, 1]
    print(sort(list))
