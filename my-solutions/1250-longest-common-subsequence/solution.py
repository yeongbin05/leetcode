class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1, common_text1, len_text2, common_text2, common_chars = len(text1), '', len(text2), '', set(text1) & set(text2)
        max_len_text = len_text1 if len_text1 > len_text2 else len_text2
        for idx in range(max_len_text):
            if idx < len_text1 and text1[idx] in common_chars: common_text1 += text1[idx]
            if idx < len_text2 and text2[idx] in common_chars: common_text2 += text2[idx]
        if common_text1 == common_text2: return len(common_text1)
        # Clever algorithm steps
        dp = [0 for _ in range(len_text1)]
        for char in text2:
            current = 0
            for idx_clever in range(len_text1):
                if current < dp[idx_clever]: current = dp[idx_clever]
                elif char == text1[idx_clever]: dp[idx_clever] = current + 1
        return max(dp) if dp else 0
