class Solution:
    def _is_vowel(self, c: str) -> bool:
        """Check if a character is a vowel."""
        return c in {"a", "e", "i", "o", "u"}

    def _at_least_k(self, word: str, k: int) -> int:
        """
        Count substrings that contain all five vowels at least once
        and have at least `k` consonants using the sliding window approach.
        """
        num_valid_substrings = 0
        start = 0
        vowel_count = defaultdict(int)  # Tracks frequency of each vowel
        consonant_count = 0

        # Sliding window traversal
        for end in range(len(word)):
            new_char = word[end]

            # Update vowel and consonant counts
            if self._is_vowel(new_char):
                vowel_count[new_char] += 1
            else:
                consonant_count += 1

            # Shrink window while conditions are met
            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end  # Count all valid substrings

                start_char = word[start]
                if self._is_vowel(start_char):
                    vowel_count[start_char] -= 1
                    if vowel_count[start_char] == 0:
                        del vowel_count[start_char]
                else:
                    consonant_count -= 1

                start += 1  # Move window forward

        return num_valid_substrings
        
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Return the number of valid substrings that contain all vowels at least once 
        and exactly `k` consonants.
        """
        return self._at_least_k(word, k) - self._at_least_k(word, k + 1)
