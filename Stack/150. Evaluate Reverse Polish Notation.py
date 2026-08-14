class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # My version
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                val_2 = stack.pop()
                val_1 = stack.pop()
                stack.append(int(ops[t](val_1,val_2)))
        return stack.pop()

        # Better solution
        stack = []
        
        # 面试装杯写法：用 lambda 自定义匿名函数
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            # int(a / b) 完美实现向零截断
            '/': lambda a, b: int(a / b) 
        }

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                val_2 = stack.pop()
                val_1 = stack.pop()
                # 直接调用对应的 lambda 函数
                stack.append(ops[t](val_1, val_2))
        return stack.pop()

        # truncate to 0: 小数点后面的数字全部砍掉
        # 1.9 -> 1
        # -1.9 -> -1
        # int 就是强制阶段 小数点前的数就是truncate to 0
        # // 或 math.floor() —— 向下取整
        # math.ceil() —— 向上取整
        # round 四舍五入
        # lambda 写法
        # def my_add(a, b): return a + b
        # def my_sub(a, b): return a - b
        # def my_div(a, b): return int(a / b)
        #|
        #|
        #v
        # '+': lambda a, b: a + b,
        # '-': lambda a, b: a - b,
        # '/': lambda a, b: int(a / b) 