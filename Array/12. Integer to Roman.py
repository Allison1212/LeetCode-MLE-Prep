class Solution:
    def intToRoman(self, num: int) -> str:
        sym_map = (
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        )
        res = ""
        for val, sym in sym_map:
            floor = num//val
            if floor != 0:
                res = res + floor*sym
            num = num - floor*val
        
        return res
    
        
