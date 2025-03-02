class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = []
        i, j = 0, 0 # Two pointers for nums1 and nums 2

        # Merge both lists using a two-pointer approach
        while i < len(nums1) and j < len(nums2):
            key1, value1 = nums1[i]
            key2, value2 = nums2[j]

            if key1 < key2:
                merged.append(nums1[i])
                i += 1
            elif key1 > key2:
                merged.append(nums2[j])
                j += 1
            else:
                # if the keys are equal, sum the valeus 
                merged.append([key1, value1 + value2])
                i += 1
                j += 1

        # Append remaining elements from nums1 or nums2
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        return merged
