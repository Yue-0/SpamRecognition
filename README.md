__English__ | [简体中文](docs/README_cn.md)

# Spam Recognition

## Brief Introduction

This project is my sophomore machine learning curriculum design project.
The goal of this project is to train a naive Bayesian classifier for spam recognition.

## File Structure

```
SpamRecognition
├── data              # Dataset code package
    └── __init__.py   # Dataset and sentence2vector code
├── docs              # Project Documents
    ├── help.txt      # Help file for train.py
    └── README_cn.md  # Chinese description document
├── LICENSE           # LICENSE
├── main.py           # Inference program
├── README.md         # English description document
├── requirements.txt  # List of requirements
└── train.py          # Train program
```

## Quick Start

### 1.Clone

```shell
git clone https://github.com/Yue-0/SpamRecognition.git
cd ./SpamRecognition
```

### 2.Install requirements

Requirements are include：
* numpy
* joblib
* sklearn

```shell
pip install -r requirements.txt
```

### 3.Prepare dataset

The dataset is a file.
Each line contains a section of text and the label corresponding to the text.
The label must be one of "spam" and "ham" at the beginning of 
each line and separated by "\t" and text.
__Currently, only English datasets are supported.__

You can [download sample dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip)
for experiment.

### 4.Train model

Run [train.py](train.py) to train the model. 
You need to specify your dataset path:

```shell
python train.py --dataset={your_dataset_path}
```

You can also specify other training parameters, 
run the following code to get more help, 
or view the [document](docs/help.txt) directly.

```shell
python train.py --help
```

### 5.Inference

The trained model will be saved in the path you specified
(the default is the "model" folder).
Specify the path and start inference:

```shell
python main.py {your_model_path}
```

__Currently, only English text is supported.__
