class Solution:
    def reverseWords(self, s: str) -> str:
        # My solution 1
        # word = ""
        # res = ""
        # for i in s:
        #     print(word)
        #     if i != " ":
        #         word = word + i
        #     else:
        #         if word != "":
        #             res = " " + word + res
        #             word = ""
        # res = word + res
        # return res.strip()

        # My solution2
        # Split can remove mutiple space
        return " ".join(s.split()[::-1])

        # One pointer solution
        # A deque stands for Double-Ended Queue. It is a type of data structure that allows to add and remove elements from both ends efficiently.Allows fast insertion and deletion from both the front and rear ends.Works as both a queue (FIFO) and a stack (LIFO).
        stack = deque()

        start = -1
        i = 0

        while i <len(s):
            if i != " ":
                start = i
                i+=1 
                while i != " ":
                    i +=1
                stack.append(s[start:i])
        
        return " ".join(stack)