# O(n) time | O(n) space
def balanced_bracket(string):
    openingBracket = "([{"
    closingBracket = ")]}"
    matchedBracket =   {"}":"{", ")":"(", "]":"["}
    stack = []
    for char in string:
        if char in openingBracket:
            stack.append(char)
        elif char in closingBracket:
            if len(stack) == 0:
                return False
            if stack[-1] == matchedBracket[char]:
                stack.pop()
            else :
                return False
    return len(stack) == 0

string = "{(())[]}"
print(balanced_bracket(string))
