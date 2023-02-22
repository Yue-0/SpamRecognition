from typing import Union
from random import shuffle

import numpy as np


class Dataset:
    def __init__(self, file: str):
        self.categories = "spam", "ham"
        if file.split(".")[-1] == "dict":
            with open(file) as dictionary:
                self.dictionary = eval(dictionary.read())
            self.x, self.y = np.array([]), np.array([])
        else:
            x, dictionary = [[], []], set()
            with open(file, encoding="utf-8") as dataset:
                while True:
                    datum = dataset.readline().rstrip("\n").lower().split("\t")
                    if len(datum) == 1:
                        break
                    x[self.categories.index(datum[0])].append("".join(
                        map(self.filter, datum[1])
                    ).split())
            spam, ham = tuple(map(len, x))
            m = min(spam, ham)
            x.sort(key=len)
            shuffle(x[1])
            x = x[0] + x[1][:m]
            for datum in x:
                dictionary |= set(datum)
            n = m << 1
            self.x = []
            self.dictionary = list(dictionary)
            for index, sentence in enumerate(x):
                self.x.append(self.sentence2vector(sentence))
                print(f"\rLoading dataset: {round(100 * index / n)}", end="%")
            print(end="\r")
            self.x = np.array(self.x, int)
            self.y = np.append(np.zeros(m), np.ones(m)).astype(int)
            if spam > ham:
                self.y = np.flip(self.y)

    def __len__(self):
        return len(self.x)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as dictionary:
            dictionary.write(str(self.dictionary))

    def sentence2vector(self, sentence: Union[str, list[str]]) -> np.ndarray:
        vector = np.zeros(len(self.dictionary), int)
        for word in sentence.split() if isinstance(sentence, str) else sentence:
            try:
                vector[self.dictionary.index(word)] = 1
            except ValueError:
                continue
        return vector

    @staticmethod
    def filter(char: str) -> str:
        asc = ord(char)
        return char if 65 <= asc <= 90 or 97 <= asc <= 122 or asc == 32 else ""
