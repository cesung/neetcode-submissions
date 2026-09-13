class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int32_max = 0x7FFFFFFF
        ttl = 0
        c = 0

        for i in range(32):
            a_bit = ((a >> i) & 1)
            b_bit = ((b >> i) & 1)
            ttl |= ((a_bit ^ b_bit ^ c) << i)
            c = (
                (a_bit & b_bit) |
                (a_bit & c) |
                (b_bit & c)
            )
        
        return ttl if ttl <= int32_max else ~(ttl ^ mask)