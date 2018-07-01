class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        idx,total,size=0,1,len(nums)
        ans=0
        while n>=total:
            if size>idx and nums[idx]<=total:
                
                total+=nums[idx]
                idx+=1
            else:
                total=total<<1
                ans+=1
        return ans
假设数组nums的“部分元素和”可以表示范围[1, total)内的所有数字，

那么向nums中添加元素add可以将表示范围扩充至[1, total + add)，其中add ≤ total，当且仅当add = total时取到范围上界[1, 2 * total)

若nums数组为空，则构造[1, n]的nums为[1, 2, 4, 8, ..., k]，k为小于等于n的2的幂的最大值。

若nums数组非空，则扩展时利用nums中的已有元素，详见代码。