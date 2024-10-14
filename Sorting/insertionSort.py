def sort(list):
    for i in range(1, len(list)):
        value = list[i]
        sortedIndex = i - 1

        while sortedIndex >= 0 and value < list[sortedIndex]:
            list[sortedIndex + 1] = list[sortedIndex]
            sortedIndex -= 1
        list[sortedIndex + 1] = value
    return list


if __name__ == "__main__":
    list = [2, 3, 1, 2, 4, 5, 6, 4, 3, 6, 8, 8, 1]
    print(sort(list))
