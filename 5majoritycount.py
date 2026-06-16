class Majority:

    def maj(self, nums):

        count = {}

        for number in nums:

            if number not in count:

                count[number] = 1

            else:

                count[number] += 1

            if count[number] > len(nums) // 2:

                return number


nums = list(map(int, input("Enter array elements: ").split()))

obj = Majority()

result = obj.maj(nums)

print(f"Array: {nums}")
print(f"Majority Element = {nums} : {result}")