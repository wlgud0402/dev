#Counter 라이브러리

from collections import Counter


string = "hello"

print(Counter(string))

print(Counter(string).items())
print(Counter(string).keys())
print(Counter(string).values())