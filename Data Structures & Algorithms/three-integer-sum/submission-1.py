class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        store = defaultdict(set)
        res_store = set()
        for i,num in enumerate(nums):
            store[num].add(i)
        #print(store)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                search = - nums[i] - nums[j]
                #print(f"{nums[i]},{nums[j]}, s:{search}")
                if search in store:
                    #print(f"found:{store[search]}")
                    if len(store[search] - {i,j}) > 0:
                        trio = tuple(sorted([nums[i],nums[j],search]))
                        res_store.add(trio)
        return list(res_store)