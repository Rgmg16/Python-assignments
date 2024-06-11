def vowel_remove(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])