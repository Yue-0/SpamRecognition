[English](../README.md) | __简体中文__

# 垃圾文本识别

## 简介

本项目是我大二的机器学习课程设计的课题。
本项目的目标是训练一个用于垃圾文本识别的朴素贝叶斯分类器，
可用于垃圾邮件过滤、垃圾短信过滤等任务。

## 文件结构

```
SpamRecognition
├── data              # 数据集代码包
    └── __init__.py   # Dataset类的定义和sentence2vector代码
├── docs              # 项目文档文件夹
    ├── help.txt      # train.py的帮助文档
    └── README_cn.md  # 中文说明文件
├── LICENSE           # LICENSE文件
├── main.py           # 推理程序
├── README.md         # 英文说明文件
├── requirements.txt  # 依赖库列表
└── train.py          # 训练程序
```

## 快速开始

### 1.克隆项目

```shell
git clone https://github.com/Yue-0/SpamRecognition.git
cd ./SpamRecognition
```

### 2.安装依赖

项目依赖的库包括：
* numpy
* joblib
* sklearn

```shell
pip install -r requirements.txt
```

### 3.准备数据

数据集是一个文件，每行包含一段文本和这段文本对应的标签，
标签必须是“spam”和“ham”中的一个，且位于每行的开头，并用“\t”与文本分隔。
__目前只支持英文数据集。__

你可以[下载样例数据集](https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip)来进行实验。

### 4.训练模型

运行[train.py](../train.py)来训练模型。 
你需要指定你的数据集路径：

```shell
python train.py --dataset={your_dataset_path}
```

你还可以指定其他训练参数，
通过运行下面的代码来查看帮助文档，或者直接[查看帮助文档](help.txt)。

```shell
python train.py --help
```

### 5.推理

训练好的模型会被保存在你指定的路径下（默认为model文件夹），
指定模型的路径来开始推理：

```shell
python main.py {your_model_path}
```

__目前只支持输入英文文本。__
