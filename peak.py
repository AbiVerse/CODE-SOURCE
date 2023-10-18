class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        findPeak=-1
        while(findPeak==-1):
            left=0
            right=0
            if(n-1<0):
                left=1
            else:
                if nums[n]>nums[n-1]:
                    left=1
            if(n+1==len(nums)):
                right=1
            else:
                if nums[n]>nums[n+1]:
                    right=1
            if(left==1 and right==1):
                findPeak=n
            else:
                if(left==0):
                    n=n-1
                else:
                    n=n+1
        return findPeak
