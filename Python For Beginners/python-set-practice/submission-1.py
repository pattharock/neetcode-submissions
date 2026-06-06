from typing import List

def contains_duplicate(words: List[str]) -> bool:
    seen = set()

    for w in words:
        seen.add(w)
    
    return len(seen) < len(words)

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
