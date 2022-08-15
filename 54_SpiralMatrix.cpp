class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int x = 0;
        int y = 0;
        int x_size = matrix[0].size();
        int y_size = matrix.size();
        vector<int> output;
        if(y_size == 1) return matrix[0];
        x--;
        output = matrix[0];
        x = x_size-1;
        while(true){
        for(int i=1; i<y_size; ++i){
            y++;
            output.push_back(matrix[y][x]);
        }
        y_size--;
        if(x_size == 1) break;
        for(int i=1; i<x_size; ++i){
            x--;
            output.push_back(matrix[y][x]);
        }
        x_size--;
        if(y_size == 1) break;
        for(int i=1; i<y_size; ++i){
            y--;
            output.push_back(matrix[y][x]);
        }
        y_size--;
        if(x_size == 1) break;
        for(int i=1; i<x_size; ++i){
            x++;
            output.push_back(matrix[y][x]);
        }
        x_size--;
        if(y_size == 1) break;
        cout<<x_size;
        cout<<y_size;
        }
        
        return output;
    }
};