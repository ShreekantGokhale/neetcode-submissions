class Solution:
    def evalRPN(self, tokens):
        t_stack = []
        for i in tokens:
                
            if i in ("+","-","*","/"):
                a = t_stack.pop()
                b = t_stack.pop()
                if i=="+":
                    t_stack.append(b+a)
                elif i=="-":
                    t_stack.append(b-a)
                elif i=="*":
                    t_stack.append(b*a)
                elif i=="/":
                    t_stack.append(int(b/a))
            else:    
                t_stack.append(int(i))
        return t_stack[0]
