class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        savex = 0
        savey = 0
        for x in range(1,len(horizontalCuts)):
            if horizontalCuts[x] - horizontalCuts[x-1] >= savex:
                savex = horizontalCuts[x] - horizontalCuts[x-1]
        for y in range(1,len(verticalCuts)):
            if verticalCuts[y] - verticalCuts[y-1] >= savey:
                savey = verticalCuts[y] - verticalCuts[y-1]
        return (savex * savey)%(pow(10,9)+7)