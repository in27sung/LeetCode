class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Map each number in nums2 to its index
        index_in_nums2 = {num: i for i, num in enumerate(nums2)}

        # Translate nums1's order into nums2's index space
        translated = [index_in_nums2[num] for num in nums1]

        tree = FenwickTree(n)
        result = 0

        for i, pos in enumerate(translated):
            # Count how many elements before current `pos` exist (left count)
            left_count = tree.query(pos)
            # Insert current position into Fenwick Tree
            tree.update(pos, 1)
            # Elements after `pos` minus how many of them are already placed after current index
            right_count = (n - 1 - pos) - (i - left_count)
            result += left_count * right_count

        return result
