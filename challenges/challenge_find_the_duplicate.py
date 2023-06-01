def sort(numbers, start, end):
    if (end - start) > 1:
        mid = (start + end) // 2
        sort(numbers, start, mid)
        sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]
    left_index, right_index = 0, 0

    for i in range(start, end):
        if left_index >= len(left):
            numbers[i] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            numbers[i] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            numbers[i] = left[left_index]
            left_index += 1
        else:
            numbers[i] = right[right_index]
            right_index += 1


def find_duplicate(nums):
    """Faça o código aqui."""
    sort(nums, 0, len(nums))

    for i in range(1, len(nums)):
        if type(nums[i - 1]) == str or nums[i - 1] < 0:
            return False
        if nums[i - 1] == nums[i]:
            return nums[i]

    return False
