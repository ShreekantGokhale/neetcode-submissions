class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {')': '(',']': '[', '}': '{'}
        for i in s:
            if i in open.values():
                stack.append(i)
            elif i in open:
                if stack:
                    if open[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else: 
            return False