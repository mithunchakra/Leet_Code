class RemoveElement:

    def RE(self, nums, val):

        # create k to store valid elements
        k = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[k] = nums[i]

                k += 1

        return k


# Input array
nums = list(map(int, input("Enter array: ").split()))

# Input value to remove
val = int(input("Enter value to remove: "))


# Object creation
obj = RemoveElement()

# Function call
result = obj.RE(nums, val)

print("Number of valid elements:", result)

print("Updated array:", nums[:result])