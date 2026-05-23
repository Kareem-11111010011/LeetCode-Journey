class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int ret = 0;

        for (string pattern : patterns) {
            if (word.contains(pattern)) {
                ret++;
            }
        }

        return ret;
    }
};
