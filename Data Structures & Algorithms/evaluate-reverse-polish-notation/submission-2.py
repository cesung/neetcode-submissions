class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stk.append(int(token))
            else:
                if len(stk) < 2:
                    return -1

                opd1, opd2 = stk.pop(), stk.pop()

                if token == '+':
                    stk.append(opd2 + opd1)
                elif token == '-':
                    stk.append(opd2 - opd1)
                elif token == '*':
                    stk.append(opd2 * opd1)
                elif token == '/':
                    # divide by zero
                    if opd1 == 0:
                        return -1

                    stk.append(int(opd2 / opd1))
                else:
                    # it shouldn't happen
                    return -1

        if len(stk) > 1:
            return -1
        
        return stk[-1]