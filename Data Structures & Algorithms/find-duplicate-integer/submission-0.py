class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = set()
        for num in nums:
            if num in store:
                return num
            store.add(num)
        