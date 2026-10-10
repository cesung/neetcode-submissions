class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pat_len, words_len = len(pattern), len(words)
        if pat_len != words_len:
            return False

        ch_to_word, word_to_ch = {}, {}
        for ch, word in zip(pattern, words):
            if (
                (ch in ch_to_word and ch_to_word[ch] != word) or
                (word in word_to_ch and word_to_ch[word] != ch)
            ):
                return False
            ch_to_word[ch] = word
            word_to_ch[word] = ch
        
        return True
