#  Write a Python class to find the three elements that sum to zero from a set of n 
# real numbers. 
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] 
# Output : [[-10, 2, 8], [-7, -3, 10]] 
class TripletFinder:
    def find_triplets(self, nums):
        result = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                target = -nums[i] - nums[j]
                if target in seen:
                    result.add(tuple(sorted([nums[i], nums[j], target])))
                seen.add(nums[j])
        return list(result)

finder = TripletFinder()
nums = [-25, -10, -7, -3, 2, 4, 8, 10]
print(finder.find_triplets(nums))


