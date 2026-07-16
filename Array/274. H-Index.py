class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # # Brute Force O(n^2)
        # if len(citations) == 1:
        #     return min(len(citations),citations[0])
        # else:
        #     h = 1

        #     while h <= len(citations):
        #         count = 0
        #         for c in citations:
        #             if c>= h:
        #                 count+=1
        #         if count >= h:
        #             if count == h:
        #                 return h
        #             else:        
        #                 h+=1
        #         else:
        #             return h-1
        # Counting sort nlog(n)

        h = len(citations)
        papar_count = [0]*(h+1)

        for i in citations:
            if i >= h:
                papar_count[-1] = papar_count[-1]+ 1
            else:
                papar_count[i] = papar_count[i] + 1
        
        print(papar_count)

        papers = papar_count[h]

        while papers < h:
            h-=1
            papers+=papar_count[h]
        
        return h
