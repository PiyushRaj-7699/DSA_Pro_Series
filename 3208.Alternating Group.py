#include <vector>
#include <iostream>

class Solution {
public:
    int numberOfAlternatingGroups(std::vector<int>& colors, int k) {
        int n = colors.size();
        int ans = 0;
        int count = 0;
        for (int i = 1; i < n + k-1; i++) {
            if ((colors[(i - 1) % n] == 0 && colors[i % n] == 1) || (colors[(i - 1) % n] == 1 && colors[i % n] == 0)) {
                count++;
            } else {
                count = 0;
            }
            if (count >= k - 1) {
                ans++;
            }
        }
        return ans;
    }
};