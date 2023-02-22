import os
from sys import argv

import joblib
import numpy as np
from sklearn import naive_bayes
from sklearn.model_selection import cross_val_score

from data import Dataset

models = (
    naive_bayes.GaussianNB(),
    naive_bayes.BernoulliNB(),
    naive_bayes.ComplementNB(),
    naive_bayes.MultinomialNB()
)


def scan_parameters():
    if len(argv) == 1:
        raise RuntimeError("'dataset' must be given.")
    if len(argv) == 2 and argv[1] == "--help":
        with open(os.path.join("docs", "help.txt")) as hlp:
            print(hlp.read())
        exit(0)
    dataset, cv, folder, name = None, None, None, None
    for i in range(1, len(argv)):
        if argv[i] == "-k" and cv is None:
            cv = int(argv[i + 1])
            if cv <= 0:
                raise ValueError("K must be a positive integer.")
        elif argv[i][:7] == "--name" and name is None:
            name = argv[i][7:]
        elif argv[i][:7] == "--path=" and folder is None:
            folder = argv[i][7:]
        elif argv[i][:10] == "--dataset=" and dataset is None:
            dataset = argv[i][10:]
        elif argv[i - 1] == "-k":
            continue
        else:
            raise RuntimeError("Parameter error. You can run "
                               "'python train.py --help' to get help.")
    if cv is None:
        cv = 10
    if name is None:
        name = "bayes"
    if folder is None:
        folder = "model"
    if folder not in os.listdir():
        os.mkdir(folder)
    return Dataset(dataset), cv, os.path.join(folder, name)


if __name__ == "__main__":
    data, k, path = scan_parameters()
    best, model = np.zeros(k), None
    for index, bayes in enumerate(models):
        print(f"Test: {index + 1}", end="/4, ")
        score = cross_val_score(bayes, data.x, data.y, cv=k)
        print("score: {:.2f}".format(100 * score.sum() / k))
        delta = np.sum(score) - np.sum(best)
        if delta > 0 or delta == 0 and np.var(score) < np.var(best):
            best, model = score, bayes
    model.fit(data.x, data.y)
    data.save(path + ".dict")
    joblib.dump(model, path + ".model")
    print(f"The highest score: {best.sum() / k}.")
