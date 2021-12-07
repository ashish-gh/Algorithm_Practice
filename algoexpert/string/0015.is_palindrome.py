
# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 1 : ITERATIVE USING STRING
# O(n^2) time | O(n) space
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString+= string[i]

    return string == reversedString 

print(isPalindrome("abcdcba"))

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 2 : ITERATIVE USING LIST
# O(n^2) time | O(n) space
def isPalindrome_1(string):
    reversedStringList =[]
    for i in reversed(range(len(string))):
        reversedStringList.append(string[i])
    
    return string == ''.join(reversedStringList)

print(isPalindrome_1("abcdcba"))

# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 3 : RECURSIVE
# O(n) time| O(n) space

def isPalindrome_2(string):
    return checkPalindrome(string, 0, len(string)-1)

def checkPalindrome(string, left, right):
    if left >= right: 
        return True
    elif string[left] == string[right] and checkPalindrome(string, left+1, right-1):
        return True
    return False

print(isPalindrome_2("abcdcba"))


def isPalindrome_3(string, i =0):
    j = len(string) - 1 -i
    return True if i >= j else string[i] == string[j] and isPalindrome_3(string, i+1)

print(isPalindrome_3("abcdcba"))


# ------------------------------------------------------------------------------------------------- 
# ------------------------------------------------------------------------------------------------- 
# METHOD 4 : ITERATIVE METHOD ==>> (BEST)
# O(n) time| O(1) space
def isPalindrome_4(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left +=1
        right-=1
    return True
     
print(isPalindrome_4("abcdcba"))