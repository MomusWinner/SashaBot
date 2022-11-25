class Verify:
    def __init__(self, word: str, test_letter1: str, test_letter2: str):
        self.word = word
        self.letterToCheck1 = test_letter1
        self.letterToCheck2 = test_letter2
        self.number = 0

    def search_for_word(self, _word) -> bool:
        _word += "\n"
        with open('russian.txt', 'r', encoding="utf-8") as ru:
            a = ru.readlines()
            if _word in a:
                return True
            else:
                return False

    def select_letter(self, _word) -> str:
        _wordList = list(_word)
        _wordList[self.number] = _wordList[self.number].upper()
        _wordList.insert(self.number, "(")
        _wordList.insert(self.number + 2, ")")
        return "".join(_wordList)

    def change(self, _word: list, value) -> str:
        counter = 0
        wordList_word = _word.copy()
        for i in wordList_word:
            if i == "_":
                wordList_word.remove("_")
                wordList_word.insert(counter, value)
                self.number = counter
                return "".join(wordList_word)

            counter += 1
        return "underscore not found"

    def correct_word(self):
        self.word = list(self.word)
        new_word1 = self.change(self.word, self.letterToCheck1)
        new_word2 = self.change(self.word, self.letterToCheck2)

        if new_word1 != "underscore not found":
            if self.search_for_word(new_word1)  and self.search_for_word(new_word2):
                return 'Написание данного слова зависит от части речи:\n' \
                       + f'{new_word1 + "--> глагол"} \n {new_word2 + "--> существительное"}'

            elif self.search_for_word(new_word1):
                return self.select_letter(new_word1)
            elif self.search_for_word(new_word2):
                return self.select_letter(new_word2)
        return "Error: The word is not recognized"


if __name__ == "__main__":

    a = Verify('ш_л', 'ё', '0')
    print(a.correct_word())