class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s)-1

        while right > left:
            right_w = s[right]
            left_w = s[left]

            s[left] = right_w
            s[right] = left_w

            right = right -1
            left = left + 1