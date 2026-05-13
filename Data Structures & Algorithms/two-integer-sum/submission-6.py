class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in indexMap:
                return [indexMap[diff], idx]
            
            indexMap[num] = idx
            
        return []
