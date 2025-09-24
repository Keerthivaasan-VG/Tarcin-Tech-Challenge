def stable_merge_sort(arr):
    comparisons = 0
    # Remove None values before sorting
    arr = [x for x in arr if x is not None]

    if len(arr) <= 1:
        return arr, comparisons

    mid = len(arr) // 2
    left, comp_left = stable_merge_sort(arr[:mid])
    right, comp_right = stable_merge_sort(arr[mid:])
    comparisons += comp_left + comp_right

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i][0] <= right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons


if __name__ == "__main__":
    arr = [
        (3, "apple", None, None, None, None, None, None),
        (1, "orange", None, None, None, None, None, None),
        (2, "banana", None, None, None, None, None, None),
        (1, "grape", None, None, None, None, None, None),
        None, None, None, None, None, None
    ]

    print("Original array:")
    print(arr)

    sorted_arr, comps = stable_merge_sort(arr)
    print("\nSorted array:")
    print(sorted_arr)

    print("\nComparisons made:", comps)
