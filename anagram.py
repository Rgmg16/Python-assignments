def is_anagram(string1, string2):
 return sorted(string1) == sorted(string2)
string1 = "wolf"
string2 = "flow"
print("Is Anagram:", is_anagram(string1, string2))