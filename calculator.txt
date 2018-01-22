# your code goes here
class Stack(object):
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
         return self.stack == []

    def push(self,item):
        self.stack.append(item)
    
    def peek(self):
        try:
            return self.stack[len(self.stack)-1]
        except:
            return 0

    def size(self):
        return len(self.stack)

    def pop(self,item=None):
        return self.stack.pop(item if item else len(self.stack)-1)
    
    def pa(self):
        a=','.join([str(a) for a in self.stack])
        return a

def calculate(o,a,b):
    if o=='+':
        return a+b
    if o=='-':
        return a-b
    if o=='*':
        return a*b
    if o=='/':
        return a/b
    if o=='%':
        return a%b

def precedence(a,o):
    if o=='(' or o==')':
        return False
    if (a=='*' or a=='/' or a=='%') and (o=='+' or o=='-'):
        return False
    if (a=='/' or a=='%') and (o=='*'):
        return False
    else:
        return True

def main():
    n = int(input())
    operator = Stack()
    numval = Stack()
    pre=None
    curr=None
    temp = 1
    for _ in range(n):
        c = str(input())
        pre = curr
        curr = c
        if c.isdigit():
            if numval.isEmpty():
                numval.push(int(c)*temp)
                temp=1
            else:
                if pre.isdigit():
                    return 'Malformed expression'
                numval.push(int(c)*temp)
                temp=1
        elif c=='(':
            operator.push(c)
        elif c==')':
            while operator.peek() is not '(':
                try:
                    numval.push(calculate(operator.pop(),numval.pop(-2),numval.pop(-1)))
                except:
                    return 'Malformed expression'
            operator.pop()
        elif c=='+' or c=='-' or c=='%' or c=='*' or c=='/':
            if pre=='(' and c=='-':
                temp*=-1
            elif numval.isEmpty() and c=='-':
                temp*=-1
            else:
                last = operator.peek()
                if c=='-' and last=='-':
                    operator.pop()
                    c='+'
                if c=='-' and last=='+':
                    operator.pop()
                    c='-'
                while not operator.isEmpty() and precedence(c,operator.peek()):
                    try:
                        numval.push(calculate(operator.pop(),numval.pop(-2),numval.pop(-1)))
                    except:
                        return 'Malformed expression'
                operator.push(c)
            
    while not operator.isEmpty():
        try:
            numval.push(calculate(operator.pop(),numval.pop(-2),numval.pop(-1)))
        except:
            return 'Malformed expression'
    if operator.isEmpty():
        return numval.pop()
    return 'Malformed expression'

if __name__ == "__main__":
    print(main(),end='')
