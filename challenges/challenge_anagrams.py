def sort(letters, start, end):
    if (end - start) > 1:
        mid = (start + end) // 2
        sort(letters, start, mid)
        sort(letters, mid, end)
        merge(letters, start, mid, end)


def merge(letters, start, mid, end):
    left = letters[start:mid]
    right = letters[mid:end]
    left_index, right_index = 0, 0

    for i in range(start, end):
        if left_index >= len(left):
            letters[i] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            letters[i] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            letters[i] = left[left_index]
            left_index += 1
        else:
            letters[i] = right[right_index]
            right_index += 1


def is_anagram(first_string, second_string):
    """Retorna se uma string é um anagrama da outra"""
    if first_string == "" and second_string == "":
        return ("", "", False)

    first_arr = list(first_string.lower())
    second_arr = list(second_string.lower())

    sort(first_arr, 0, len(first_arr))
    sort(second_arr, 0, len(second_arr))

    first = "".join(first_arr)
    second = "".join(second_arr)

    return (first, second, first == second)
