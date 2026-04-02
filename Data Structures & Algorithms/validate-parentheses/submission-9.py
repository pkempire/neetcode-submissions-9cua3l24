class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '[' or char == '('  or char == '{':
                stack.append(char)
            elif char == ']' or char == ')'  or char == '}':
                if not stack:
                    return False
                temp = stack.pop()
                if temp == '[' and char != ']':
                    return False 
                if temp == '{' and char != '}':
                    return False     
                if temp == '(' and char != ')':
                    return False   
        if (len(stack)==0):
            return True
        else:
            return False    