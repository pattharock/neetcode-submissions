class TextProcessor:
    def format_text(self, word1: str, word2: str = None) -> str:
        if word2 is None:
            return word1.upper()
        return word1 + word2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
