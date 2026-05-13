class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freq = defaultdict(list)

        for anagram in strs:
            count = [0] * 26

            for char in anagram:
                idx = ord(char) - ord('a')
                count[idx] += 1
            
            char_freq[tuple(count)].append(anagram)
        
        return list(char_freq.values())