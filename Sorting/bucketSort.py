import math


def bubbleSort(list):
    for i in range(len(list) - 1):
        sorted = True
        for j in range((len(list) - 1) - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                sorted = False
        if sorted:
            return list
    return list


def sort(list):
    NoOfBuckets = round((len(list) ** 0.5))
    buckets = {}
    for i in range(NoOfBuckets):
        if i not in buckets:
            buckets[i] = []

    maxVal = 0

    for item in list:
        if item > maxVal:
            maxVal = item

    for item in list:
        appropriateBucket = math.ceil(item * (NoOfBuckets / maxVal)) - 1
        buckets[appropriateBucket].append(item)

    sorted = []
    for _, v in buckets.items():
        sorted.extend(bubbleSort(v))

    return sorted


if __name__ == "__main__":
    list = [2, 3, 1, 2, 4, 5, 6, 4, 3, 6, 8, 8, 1]
    print(sort(list))
