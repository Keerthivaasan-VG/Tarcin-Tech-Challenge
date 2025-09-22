def transform(arr):
    result = []
    n = len(arr)

    for i in range(n):
        if i == 0:  # first element
            result.append(arr[i+1])
        elif i == n-1:  # last element
            result.append(arr[i-1])
        else:  # middle elements
            result.append(arr[i-1] * arr[i+1])
    return result


# Example usage
numbers = [2, 3, 4, 5]
print(transform(numbers))