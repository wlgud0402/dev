#파이썬에서 Stack 의 경우 별다른 라이브러리 사용 필요 X

#후입선출 구조 => 마지막에 들어온것이 제일 먼저 나감.

stack = []

stack.append(5)
stack.append(9)
stack.append(1)

stack.pop()

stack.append(3)
stack.append(6)
stack.append(2)

print(stack)
