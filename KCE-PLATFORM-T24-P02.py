def classify(nums):
    result = {
        "even": [],
        "odd": []
    }
    
    for n in nums:
        if n % 2 == 0:
            result["even"].append(n)
        else:
            result["odd"].append(n)
    
    return result


# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(classify(numbers))