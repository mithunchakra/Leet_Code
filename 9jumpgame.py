# "Given an array where each element represents the maximum jump length from that position, 
# determine whether it is possible to reach the last index starting from the first index."

class Jumpgame:

    def canjump(self, nums):

        max_reach = 0

        for i in range(len(nums)):

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True


J1 = Jumpgame()

# Input
nums = list(map(int, input("Enter Values: ").split()))

# Function call
print(J1.canjump(nums)) 