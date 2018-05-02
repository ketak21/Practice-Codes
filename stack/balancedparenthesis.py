class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[-1]
    def match(self,p1,p2):
        if p1 == '(' and p2 == ')':
            return True
        elif p1 == '{' and p2 == '}':
            return True
        elif p1 == '[' and p2 == ']':
            return True
        else:
            return False


    def balancedparen(self,string):
        balanced = True
        index = 0
        while index < len(string) and balanced:
            paren = string[index]
            if paren in '({[' and balanced:
                self.stack.append(paren)
            else:
                if self.isEmpty() and balanced:
                    balanced = False
                else:
                    p1 = self.pop()
                    balanced = self.match(p1,paren)

            index = index + 1

        if self.isEmpty() and balanced:
            print("String is balanced")
        else:
            print("Unbalanced")

string = "((({{}}))){}"

s = Stack()
s.balancedparen(string)
