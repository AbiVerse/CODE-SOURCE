class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        start=0
        if(len(s)==0):
            return 0
        maxi=1
        for i in range(0,len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                if d[s[i]]>=start:
                    if(maxi<(i-start)):
                        maxi=i-start
                    start=d[s[i]]+1
                d[s[i]]=i
            if i==len(s)-1:
                if(maxi<(i-start+1)):
                    maxi=i-start+1
        return maxi
