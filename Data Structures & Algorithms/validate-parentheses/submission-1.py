class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for p in s:
            if p in ["(","{","["]:
                stack.append(p)
            else:
                if len(stack) <= 0:
                    return False
                if stack[-1] == lookup[p]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0