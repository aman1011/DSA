# https://leetcode.com/problems/rotate-array/

class Solution:

    def reverse_between_two_indexes(self, first, last, arr):
        count = 0
        for i in range(first , first + (last- first) // 2):
            target = last - 1 - count
            temp = arr[i]
            arr[i]= arr[target]
            arr[target]  = temp

            count += 1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        if k != 0:
            self.reverse_between_two_indexes(0, len(nums) - k, nums)
            self.reverse_between_two_indexes(len(nums) - k, len(nums), nums)
            self.reverse_between_two_indexes(0, len(nums), nums)
            

    