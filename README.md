# Cookiecutter 数据科学项目

_一个逻辑合理、标准且灵活的项目结构，用于进行和共享数据科学工作。_

### 使用cookiecutter 模板的依赖:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python 包](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: 这可以通过 pip 或 conda 安装，具体取决于您管理 Python 包的方式:

``` bash
$ pip install cookiecutter
```

或者

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### 开始一个新项目:
------------

    cookiecutter  https://github.com/llango/cookiecutter-data-science



### 生成的目录结构
------------

新项目的目录结构如下: 

```
├── LICENSE
├── Makefile           <- 可以使用 `make data` 或 `make train` 等操作Makefile 文件。
├── README.md          <- 使用此项目的开发人员的顶级README。
├── data
│   ├── external       <- 来自第三方的数据。
│   ├── interim        <- 已转换的中间数据。
│   ├── processed      <- 用于建模的规则数据。
│   └── raw            <- 原始的、不可变的数据转储。
│
├── docs               <- mkdocs文档，使用shadocs主题。
│
├── models             <- 训练和序列化模型、模型预测或模型总结。
│
├── notebooks          <- Jupyter笔记本。命名约定是一个数字(用于排序)，创作者姓名的首字母和用“-”分隔的简短描述。 
│                        `1.0-jqp-initial-data-exploration`.
│
├── references         <- 数据字典、手册和所有其他解释性材料。
│
├── reports            <- 生成HTML, PDF, LaTeX等分析报告。
│   └── figures        <- 生成用于报告的图形和数字
│
├── requirements.txt   <- 用于再现分析环境的需求文件。生成于 `pip freeze > requirements.txt`
│
├── setup.py           <- 使项目PIP可安装(PIP install -e .)，因此可以导入src
├── src                <- 此项目中使用的源代码。
│   ├── __init__.py    <- 使src成为Python包
│   │
│   ├── data           <- 用于下载或生成数据的脚本
│   │   └── make_dataset.py
│   │
│   ├── features       <- 将原始数据转换为用于建模的特性的脚本
│   │   └── build_features.py
│   │
│   ├── models         <- 脚本用来训练模型，然后使用训练过的模型来制作预测。
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- 用于创建探索性和面向结果的可视化的脚本
│       └── visualize.py
│
└── tox.ini            <- 带有运行Tox的设置的Tox文件; 可以参考 tox.readthedocs.io
```

## 贡献

欢迎贡献！

### 安装依赖
------------

    pip install -r requirements.txt

### 运行测试
------------

    py.test tests
