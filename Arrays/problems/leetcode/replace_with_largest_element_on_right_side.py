# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        b = [-1]
        current_largest = 0

        for i in range(len(arr) - 1, 0, -1):
            if arr[i] >  current_largest:
                b.append(arr[i])
                current_largest = arr[i]
            else:
                b.append(current_largest)

        b.reverse()
        return b
    