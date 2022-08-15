class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxheightleft = height[l]
        maxheightright = height[r]
        maxv = 0
        while(l<r):
            if maxheightleft >= maxheightright:
                maxv = max(maxv, maxheightright*(r-l))
                r-=1
                maxheightright=max(maxheightright, height[r])
            if maxheightleft < maxheightright:
                maxv = max(maxv, maxheightleft*(r-l))
                l+=1
                maxheightleft=max(maxheightleft, height[l])
        return maxv