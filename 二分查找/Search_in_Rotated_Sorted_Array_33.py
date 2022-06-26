class Solution:

    # 利用二分法求解
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] == target:
                return left
            elif nums[mid] == target:
                return mid
            elif nums[right] == target:
                return  right
            else:
                if nums[left] < nums[mid]:
                    if nums[left] < target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target < nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1