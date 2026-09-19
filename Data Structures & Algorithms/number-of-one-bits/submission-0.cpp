class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t result = 0;
        uint32_t mask = 0x1;
        while (n) {
            result += (n & mask);
            n >>= 1;
        }
        return result;
    }
};
