def find_duplicate(nums):
    """Faça o código aqui."""
    nums.sort()

    for i in range(len(nums) - 1):
        if type(nums[i + 1]) == str or nums[i + 1] < 0:
            return False
        if nums[i + 1] == nums[i]:
            return nums[i]

    return False
