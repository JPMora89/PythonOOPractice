"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    def __init__(self, file_path):
        word_file = open(file_path, 'r')
        self.words = self.look_Up(word_file)
        print(f"{len(self.words)} is the number of words read")
    def look_Up(self,word_file):
        return [word.strip() for word in word_file]
    def random(self):
        return random.choice(self.words)    
    
class SpecializedWordFinder(WordFinder):
    def look_Up(self, word_file):
        return [word.strip() for word in word_file if word.strip() and not word.startswith('#')]


