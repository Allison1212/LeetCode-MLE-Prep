class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000
        }
        out = 0
        # zip length is equal to the shorter list length
        for a,b in zip(s,s[1:]):
            if symbol_map.get(a) < symbol_map.get(b):
                out = out - symbol_map.get(a)
            else:
                out = out + symbol_map.get(a)
        
        out = out + symbol_map.get(s[-1])
        return out





        # symbol_map = {'I':1,
        #             'V':5,
        #             'X':10,
        #             'L':50,
        #             'C':100,
        #             'D':500,
        #             'M':1000,
        #             'IV':4,
        #             'IX':9
        # }
        # out = 0
        # for a,b in zip(s,s[1:]):
        #     roman_a = symbol_map.get(a)
        #     roman_b = symbol_map.get(b)
        #     if roman_a < roman_b:
        #         out = out - roman_a
        #     else:
        #         out = out + roman_a
        # out = out + symbol_map.get(s[-1])
        
        # return out



