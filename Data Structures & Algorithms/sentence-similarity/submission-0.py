class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n1 = len(sentence1)
        n2 = len(sentence2)
        if n1!=n2:
            return False
        for i in range(n1):
            if [sentence1[i],sentence2[i]] in similarPairs or [sentence2[i],sentence1[i]] in similarPairs or sentence1[i]==sentence2[i] :
                continue
            else:
                return False
        return True