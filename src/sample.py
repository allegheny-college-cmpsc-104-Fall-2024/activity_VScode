def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

nums = [1, 2, 3, 4, 5]
print("The mean is", calculate_mean(nums))