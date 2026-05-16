class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        delimiter = "&"
        
        for word in strs:
            str_length = str(len(word))
            encoded_str += f"{str_length + delimiter + word}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        result, idx = [], 0
        delimiter = "&"

        while idx < len(s):
            word_len_idx = idx
            word_len = ""

            while s[word_len_idx] != delimiter:
                word_len += s[word_len_idx]
                word_len_idx += 1
            
            word_len_idx += 1 # Move forward to the start index of word
            word_end_idx = word_len_idx + int(word_len)
            word = s[word_len_idx:word_end_idx]
            result.append(word)
            idx = word_end_idx
        
        return result
                