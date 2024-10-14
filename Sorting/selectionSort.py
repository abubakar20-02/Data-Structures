def sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j

        if list[i] != list[min]:
            list[i], list[min] = list[min], list[i]
    return list


if __name__ == "__main__":
    list = [2, 3, 1, 2, 4, 5, 6, 4, 3, 6, 8, 8, 1]
    print(sort(list))
