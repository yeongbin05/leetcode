class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for (int i = 0; i<n ;i ++ ){
            int j = n - i;
            if ((to_string(i)+to_string(j)).find('0') == string::npos){
                return {i,j};
            }
        }
        return {};
    }
};
