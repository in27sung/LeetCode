class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Record the last occurrence of each character
        last = {c: i for i, c in enumerate(s)}
        
        partitions = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions
