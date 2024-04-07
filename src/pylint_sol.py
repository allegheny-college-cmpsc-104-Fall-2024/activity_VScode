"""Module docstring: Description of what the module does."""

def calculate_mean(numbers):
    """Calculate and return the mean of a list of numbers.

    Args:
        numbers (list): A list of numbers (ints or floats).

    Returns:
        float: The mean of the numbers.
    """
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("The mean is", calculate_mean(nums))
    