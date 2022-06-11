# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    word1 = list(word1)
    word2 = list(word2)
    
    return (sorted(word1) == sorted(word2))


print(find_anagrams("python","lol"))

