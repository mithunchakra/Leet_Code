class Solutions:

    def removeDuplicates(self, nums):


        k = 1

        for i in range(1, len(nums)):
            
            if nums[i] <= 0:
                 continue

            if nums[i] != nums[i - 1]:

                nums[k] = nums[i]

                k += 1

        return k


nums = list(map(int, input("Enter the array elements: ").strip().split()))

sol = Solutions()

result = sol.removeDuplicates(nums)

print(result)

print(nums[:result])