from sys import argv

from joblib import load
from numpy import argmax

from data import Dataset

if len(argv) > 2:
    raise RuntimeError("Only expect Model path")
elif len(argv) == 1:
    raise RuntimeError("Model path must be given.")

DATASET = Dataset(argv[1] + ".dict")
CLASSIFIER = load(argv[1] + ".model")


def classification(sentence: str) -> tuple[str, float]:
    p = CLASSIFIER.predict_proba(DATASET.sentence2vector(sentence)[None])[0]
    c = argmax(p)
    return DATASET.categories[c], 100 * p[c]


while True:
    text = input("\nPlease enter text: ")
    category, probability = classification(text)
    print(f"It's {category}, similarity: ", end="{:.2f}%".format(probability))
