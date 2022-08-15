class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int maxleft = height[l];
        int maxright = height[r];
        int maxvolume = 0;
        while(l<r){
            if (maxleft >= maxright){
                maxvolume = max(maxvolume,(r-l)*maxright);
                r--;
                maxright = max(maxright, height[r]);
            }
            if (maxleft < maxright) {
                maxvolume = max(maxvolume,(r-l)*maxleft);
                l++;
                maxleft = max(maxleft, height[l]);
            }
        }
    
    return maxvolume;
    }
};