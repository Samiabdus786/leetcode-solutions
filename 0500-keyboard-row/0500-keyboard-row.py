class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for w in words:
            for r in rows:
                if set(w.lower()) <= set(r):
                    ans.append(w)
                    break
        return ans