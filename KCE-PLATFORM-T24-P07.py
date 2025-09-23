def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    # sort left half
    left_result = merge_sort(arr[:mid])
    left = left_result[0]
    comp_left = left_result[1]

    # sort right half
    right_result = merge_sort(arr[mid:])
    right = right_result[0]
    comp_right = right_result[1]

    # merge both halves
    merged_result = merge(left, right)
    merged = merged_result[0]
    comp_merge = merged_result[1]

    total_comparisons = comp_left + comp_right + comp_merge
    return merged, total_comparisons


def custom_sort(arr):
    result = merge_sort(arr)
    sorted_arr = result[0]
    comparisons = result[1]
    return sorted_arr, comparisons


# Example usage
numbers = [5, 2, 8, 3, 1, 7]
sorted_list, count = custom_sort(numbers)
print("Sorted List:", sorted_list)
print("Comparisons:", count)
