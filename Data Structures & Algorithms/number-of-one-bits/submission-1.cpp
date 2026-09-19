class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        uint32_t twobitmask = 0x55555555;
        uint32_t twobitsum = (n & twobitmask) + ((n >> 1) & twobitmask); 

        uint32_t fourbitmask = 0x33333333;
        uint32_t fourbitsum = (twobitsum & fourbitmask) + ((twobitsum >> 2) & fourbitmask);

        uint32_t bytemask = 0x0F0F0F0F;
        uint32_t bytesum = (fourbitsum & bytemask) + ((fourbitsum >> 4) & bytemask);

        uint32_t twobytemask = 0x00FF00FF;
        uint32_t twobytesum = (bytesum & twobytemask) + ((bytesum >> 8) & twobytemask);
 

        return (twobytesum & 0xFFFF) + ((twobytesum >> 16) & 0xFFFF);
    }
};
