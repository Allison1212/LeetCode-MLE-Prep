class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        one = 0
        two = 0

        for i in nums:
            one = one ^i & ~two
            two = two ^i & ~one

        return one

# number AND ~(number) = 0
# number XOR number = 0
# number XOR 0 = number
# there two bucket:
# Add bucket two first bucket if number is not in bucket 1 and 2
# Remove number from bucket one if another same number enter and add number two bucket two
# If number enter third time, remove it out from bucket 2