def concatenate(s1: str, s2: str) -> str:
    concatenated = s1 + s2
    return "Too long!" if len(concatenated) > 10 else concatenated




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
