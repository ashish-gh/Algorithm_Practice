# Problem Statement
# -------------------

# Given a non-empty string of lowercase letters and a non-negative integer value representing a key, 
# write a function that returns a new string obtained by shifting every letter 
# in the input string by k positions in the alphabet, where k is the key. Note that 
# letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns 
# the letter "a".

# Sample input:"xyz", 2 
# Sample output:"zab"
# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 


# METHOD 1:
# O(n) time | O(n) space
def ceaserCypherEncryptor(string, key):
    newLetter = []
    newKey = key % 26
    for letter in string:
        newLetter.append(getNewLetter(letter, newKey))
    return "".join(newLetter)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode<= 122 else chr(96+ newLetterCode % 122)

print(ceaserCypherEncryptor('xyz', 2))



# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 2:
# O(n) time | O(n) space

def ceaserCypherEncryptor_1(string, key):
    newLetter = []
    newKey = key % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in string:
        newLetter.append(getNewLetter_1(letter, newKey, alphabet))
    return "".join(newLetter)

def getNewLetter_1(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode] if newLetterCode < 25 else alphabet[-1+ newLetterCode%25]    
    
print(ceaserCypherEncryptor_1('xyz', 2))


