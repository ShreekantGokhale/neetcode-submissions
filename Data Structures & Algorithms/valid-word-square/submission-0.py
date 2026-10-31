class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i,j in enumerate(words):
            temp= []
            for m in words:
                try:
                    temp.append(m[i])
                except:
                    break
            if list(j)==temp:
                continue
            else:
                return False
        return True