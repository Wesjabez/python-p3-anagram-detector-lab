class Anagram:
    def __init__(self, word):
        self.word = word

    @staticmethod
    def match(words_list):
        anagrams = []
        for candidate in words_list:
            if sorted(candidate.lower()) == sorted(self.word.lower()) and candidate.lower() != self.word.lower():
                anagrams.append(candidate)
        return anagrams
