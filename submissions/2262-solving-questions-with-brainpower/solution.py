class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] = max points starting from question i

        # Iterate backwards: from last question to the first
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1

            # Option 1: take current question → add points + jump
            take = points + (dp[next_q] if next_q < n else 0)

            # Option 2: skip current question
            skip = dp[i + 1]

            # Choose the better of take or skip
            dp[i] = max(take, skip)

        return dp[0]
