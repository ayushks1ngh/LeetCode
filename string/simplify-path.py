class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        # if .. then remove prev item
        # if . remove it
        stack = []
        for i in p:
            if i == '.' or not i:
                continue
            
            if i == '..':
                if not stack:
                    continue
                else:
                    stack.pop()
                    continue
            stack.append(i)
        return "/" + "/".join(stack)