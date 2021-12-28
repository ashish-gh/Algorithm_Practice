# Question in : Facebook

# Time Complexity: O(n) - going through the size of the list
# Space Complexity: O(n) - stores the value in the stack 

class Solution:
    def is_valid_parentheses(self, s: str) -> bool:
        stack = []
        kvs = { ")": "(", "]": "[", "}":"{"}
        st = "[]"
        for e in s:
            if e in kvs:
                if stack and stack[-1] == kvs[e]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(e)
        return True if not stack else False


def main():
    string = "{{{()}}}"
    sl = Solution()
    print(sl.is_valid_parentheses(string))


if __name__ == "__main__":
    main()