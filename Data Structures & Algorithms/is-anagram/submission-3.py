class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s)!=len(t):
            return False 
        counts={}
        for ch in s:
            if ch not in counts:
                counts[ch]=1
            else:
                counts[ch]+=1
        for ch in t:
            if ch not in counts:
                return False
            else:
                counts[ch]-=1
        for val in counts:
            if counts.get(val)>0:
                return False
        return True
        