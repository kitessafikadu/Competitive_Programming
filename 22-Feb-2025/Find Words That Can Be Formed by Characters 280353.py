# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[ch] <= char_count[ch] for ch in word):
                total_length += len(word)
        
        return total_length