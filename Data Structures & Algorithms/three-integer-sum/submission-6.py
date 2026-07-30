class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                diff = -(nums[i] + nums[j])

                if diff in seen:
                    triplet = tuple(sorted([nums[i], nums[j], diff]))
                    triplets.add(triplet)

                seen.add(nums[j])

        return [list(triplet) for triplet in triplets]