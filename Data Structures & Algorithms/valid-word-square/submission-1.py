class Solution:
    # def validWordSquare(self, words: List[str]) -> bool:
    #     for i,j in enumerate(words):
    #         temp= []
    #         for m in words:
    #             try:
    #                 temp.append(m[i])
    #             except:
    #                 break
    #         if list(j)==temp:
    #             continue
    #         else:
    #             return False
    #     return True

        def validWordSquare(self, words: List[str]) -> bool:
            t_dict = dict()
            for i in words:
                for j in range(len(i)):
                    if j not in t_dict:
                        t_dict[j] = t_dict.get(j,[])
                    t_dict[j].append(i[j])
            for i in range(len(words)):
                if t_dict[i]==list(words[i]):
                    continue
                else:
                    return False
            return True