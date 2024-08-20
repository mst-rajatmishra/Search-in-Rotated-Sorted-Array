from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            
            if nums[mid] == target:
                return mid
            
            
            if nums[left] <= nums[mid]:  
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  
                    left = mid + 1
            else:  
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else:  
                    right = mid - 1
        

        return -1

sol = Solution()

nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(sol.search(nums1, target1)) 

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(sol.search(nums2, target2)) 

nums3 = [1]
target3 = 0
print(sol.search(nums3, target3))
