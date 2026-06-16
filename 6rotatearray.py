'''
Interview Definition

If the interviewer asks:

What is Rotate Array?

You can answer:

Rotate Array means shifting the elements of an array by k positions. 
In a right rotation, the last k elements are moved to the beginning while preserving their order





'''
class Rotate:
    def rot(self, nums, k):
        k = k % len(nums)
        result = nums[-k:] + nums[:-k]

        return result


result = list(map(int, input("Enter array elements: ").split()))

k = int(input("Enter k value: "))

obj = Rotate()

print(obj.rot(result, k))    

