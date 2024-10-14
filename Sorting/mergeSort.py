def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])


    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    # Compare the elements of left and right lists and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left list, add them
    sorted_list.extend(left[left_index:])

    # If there are remaining elements in the right list, add them
    sorted_list.extend(right[right_index:])

    return sorted_list


# Example usage:
if __name__ == "__main__":
    arr = [3,5,2,1,8,6]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array: {sorted_arr}")
