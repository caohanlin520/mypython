class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        solution = []
        for i in range (len(nums)-1) :
            for j in range (i+1, len(nums)):
                temp = nums[i] + nums[j]
                if(temp == target):
                    first = i
                    second = j
                    subsolution = [first, second]
                    solution.append(subsolution)


        return solution

solution = Solution()
nums = [ 1, 6, 2, 5 ]

target = 7
answers = solution.twoSum(nums, target)
for i in answers:
    print(i)