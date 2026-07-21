# class RandomizedSet:

#     def __init__(self):
#         self.my_dict = dict()

#     def insert(self, val: int) -> bool:
#         if not self.my_dict.get(val):
#             self.my_dict[val] =1
#             return True
#         else:
#             return False
        

#     def remove(self, val: int) -> bool:
#         if self.my_dict.get(val):
#             self.my_dict.pop(val, None) 
#             return True
#         else:
#             return False

#     def getRandom(self) -> int:
#         return random.choice(list(self.my_dict))
        
class RandomizedSet:

    def __init__(self):
        self.my_dict = dict()
        self.my_list = list()

    def insert(self, val: int) -> bool:
        # zero index trap, don't use if self.my_dict.get(val), When you call self.my_dict.get(val) for item in 0 index, it returns 0. Because 0 is evaluated as False in Python, your if statement thinks the element doesn't exist!
        if val in self.my_dict:
            return False
        else: 
            self.my_dict[val] = len(self.my_list)
            self.my_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.my_dict:
            last_element,idx = self.my_list[-1],self.my_dict.get(val)
            self.my_list[idx],self.my_dict[last_element] = last_element,idx
            self.my_list.pop()
            del self.my_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()