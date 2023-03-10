"""
binary_search1.py file!
"""

from typing import List

class Solution:
    """
    """
    def search(self, nums:List[int], targer:int)-> int:
        """
        Func binary search!
        """
        low = 0
        high = len(nums) - 1 

        while low <= high:
            mid = (low + high)
            guess = nums[mid]
            if guess == targer:
                return mid
            if guess > targer:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search2(self, nums:List[int], target:int) -> int:
        """
        Second func search!
        """
        for i in nums:
            if i == target:
                return nums.index(target)
        return -1

if __name__ == "__main__":
    solution = Solution()
    #print(solution.search([-1,0,3,5,9,12],9))
    print(solution.search2([-1,0,3,5,9,12],9))
    # стр. 45