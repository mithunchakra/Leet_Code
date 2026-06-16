## For sorted array

'''class Solution:

    def Removeelements(self, nums):

        if len(nums) <= 2:
            return len(nums)

        k = 2

        for i in range(2, len(nums)):

            if nums[i] != nums[k - 2]:

                nums[k] = nums[i]

                k += 1

        return k


nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()

result = sol.Removeelements(nums)

print(result)
print(nums[:result])
'''

## for unsorted array
'''
class Solution:

    def removeDuplicates(self, nums):

        count = {}

        result = []

        for num in nums:

            if num not in count:
                count[num] = 1
                result.append(num)

            elif count[num] < 2:
                count[num] += 1
                result.append(num)

        return result


nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()

result = sol.removeDuplicates(nums)

print("Output:", result)
'''
#------------------------------------------------>

# using continue
class Solution1:

    def removeDuplicates(self, nums):

        count = {}
        result = []

        for num in nums:

            if num not in count:

                count[num] = 1
                result.append(num)

                continue

            if count[num] >= 2:

                continue

            count[num] += 1
            result.append(num)

        return result


nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution1()

result = sol.removeDuplicates(nums)

print("Output:", result)