class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # Compute LCS using dynamic programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # Match found, extend LCS
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # No match, take the max

        # Construct the SCS from the LCS information
        i, j = m, n
        scs = []  # hold the characters for the shortest common supersequence

        # Traverse both strings from end to start
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # Add common character only once
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                # Choose character from str1
                scs.append(str1[i - 1])
                i -= 1
            else:
                # Choose character from str2
                scs.append(str2[j - 1])
                j -= 1

        # Add the remaining characters from the beginning of either string
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        # Reverse the result to get correct order
        return ''.join(reversed(scs))

