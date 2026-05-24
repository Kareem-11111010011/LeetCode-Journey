class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['*', '/', '+', '-']
        stack = []
        for token in tokens:
            if token in operations:
                match token:
                    case '*':
                        stack.append(stack.pop() * stack.pop())
                    case '/':
                        r = stack.pop()
                        l = stack.pop()
                        stack.append(int(l / r))
                    case '+':
                        stack.append(stack.pop() + stack.pop())
                    case '-':
                        r = stack.pop()
                        l = stack.pop()
                        stack.append(l - r)
            else:
                stack.append(int(token))
        
        return stack[-1]
                    
                    
