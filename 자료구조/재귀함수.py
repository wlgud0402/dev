#recursive_function

# (1)재귀함수의 수행은 스택 자료구조를 이용한다.
# (2)함수를 계속 호출했을때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그앞의 함수 호출이 종료되기 때문이다. 
# (3)ex)factorial n! 에서 5x4x3x2 후에 1이 리턴되어야 종료되는것

def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 1. factorial(5) 를 실행 => n이 1 이상이므로 return 5 * factorial(4)

# 2. factorial(4) 를 실행 => n이 1 이상이므로 return 4 * factorial(3)

# .....

# 3. factorial(1) 를 실행 => n이 1 이하이므로 return 1

# 4. 마지막 실행한 함수가 끝났으므로 모든 함수의 호출이 종료

# 5.. factorial(5)의 결과로 return 5 * 4 * 3 * 2 * 1 이 완성된다.

