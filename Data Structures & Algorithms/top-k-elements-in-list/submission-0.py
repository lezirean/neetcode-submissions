class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(lambda: 0)
        freq = [ [] for count in range(len(nums) + 1) ]

        for num in nums:
            num_count[num] += 1
        
        for num, count in num_count.items():
            freq[count].append(num)
        
        top_k = []
        for freq_num in reversed(freq):
            for num in freq_num:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
