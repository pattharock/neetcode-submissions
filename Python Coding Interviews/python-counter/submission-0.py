from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    s = Counter(s1)
    s.update(s2)
    return s
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
