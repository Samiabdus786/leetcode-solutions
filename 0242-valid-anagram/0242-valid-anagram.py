from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=Counter(s)
        if(len(s)!=len(t)):
            return False
        for i in range(len(t)):
            if m[t[i]]:
                m[t[i]]-=1
            if m[t[i]]==0:
                del m[t[i]]
        return len(m)==0
                

        