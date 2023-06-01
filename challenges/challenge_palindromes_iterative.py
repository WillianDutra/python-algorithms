def is_palindrome_iterative(word):
    """Retorna se a palavra passada é um palíndromo"""
    if not word:
        return False

    word_array = list(word)
    right = len(word) - 1
    for letter in word:
        if letter == word_array[right]:
            if len(word) // 2 >= right:
                return True
            right -= 1
        else:
            return False


print(is_palindrome_iterative("civic"))
