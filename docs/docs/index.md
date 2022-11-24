# Cookiecutter 数据科学

_一个合乎逻辑、合理标准化但灵活的项目结构，用于进行和共享数据科学工作。_

## 为什么要使用这个项目结构？

> 我们不是在谈论摆脱缩进美学或迂腐的格式标准——归根结底，数据科学代码质量是关于正确性和可重复性的。

当我们考虑数据分析时，我们通常只考虑生成的报告、见解或可视化。 虽然这些最终产品通常是主要事件，但很容易将注意力集中在使产品 看起来漂亮 而忽略 生成它们的代码的质量上 。 因为这些最终产品是以编程方式创建的，所以 代码质量仍然很重要 ！ 而且我们不是在谈论摆脱缩进美学或迂腐的格式标准——归根结底，数据科学代码质量是关于正确性和可重复性的。

众所周知，好的分析往往是非常分散和偶然探索的结果。 尝试性实验和可能行不通的快速测试方法都是获得好东西的过程的一部分，并且没有灵丹妙药可以将数据探索转化为简单的线性进展。

话虽如此，一旦开始，它就不是一个有助于仔细考虑代码结构或项目布局的过程，因此最好从一个干净、合乎逻辑的结构开始，并始终坚持下去。 我们认为使用像这样的相当标准化的设置是一个相当大的胜利。 原因如下：

###  其他人会感谢你

> 在创建一个新的 Rails 项目之前，没有人会坐在那里弄清楚他们想把他们的观点放在哪里； 他们只是跑 rails new像其他人一样获得标准的项目框架。

A well-defined, standard project structure means that a newcomer can begin to understand an analysis without digging in to extensive documentation. It also means that they don't necessarily have to read 100% of the code before knowing where to look for very specific things.

组织良好的代码往往是自文档化的，因为组织本身可以为您的代码提供上下文，而无需太多开销。 人们会为此感谢你，因为他们可以：

- 在此分析中更轻松地与您协作
- 从您的分析中了解流程和领域
- 对分析得出的结论充满信心

在任何主要的 Web 开发框架（如 `Django` 或 `Ruby on Rails` ）中都可以找到这方面的一个很好的例子。 在创建一个新的 Rails 项目之前，没有人会坐在那里弄清楚他们想把他们的观点放在哪里； 他们只是跑 rails new像其他人一样获得标准的项目框架。 因为默认的项目结构 中都是合乎逻辑 的并且 在大多数项目 是合理的标准，所以对于从未见过特定项目的人来说更容易弄清楚他们在哪里可以找到各种活动部分。

另一个很好的例子是 的文件系统层次结构标准 类 Unix 系统 。 这`/etc` 目录有一个非常特定的目的，就像 `/tmp` 文件夹，每个人（或多或少）都同意遵守该社会契约。 这意味着 Red Hat 用户和 Ubuntu 用户都大致知道在哪里可以找到特定类型的文件，即使在使用彼此的系统时也是如此——或者任何其他符合标准的系统！

理想情况下，当同事打开您的数据科学项目时应该是这样的。

### 你会感谢你

是否曾尝试重现您几个月前甚至几年前所做的分析？ 您可能已经编写了代码，但现在无法破译您是否应该使用 `make_figures.py.old`, `make_figures_working.py`或者 `new_make_figures01.py`把事情做好。 以下是我们学会带着存在主义恐惧感提出的一些问题：

> 我们是否应该在开始之前进入并将 X 列连接到数据中，还是来自其中一个笔记本？
> 想一想，在运行绘图代码之前我们必须先运行哪个笔记本：它是“处理数据”还是“干净数据”？
> 地理图的 shapefile 从哪里下载？
> 等等，无限次。

这些类型的问题很痛苦，是项目混乱的症状。 良好的项目结构鼓励使更容易回到旧工作的实践，例如关注点分离、将分析抽象为 DAG 以及版本控制等工程最佳实践。

### 这里没有任何约束力

    “愚蠢的一致性是小脑袋的妖精”——拉尔夫·沃尔多·爱默生（和 PEP 8！ ）

不同意几个默认文件夹名称？ 正在从事一个有点不标准且不完全适合当前结构的项目？ 更喜欢使用与（少数）默认值之一不同的包？

**去吧！** 这是一个轻量级的结构，旨在成为许多项目的良好 起点 。 或者，正如 PEP 8 所说：

> 项目内的一致性更为重要。 一个模块或功能内的一致性是最重要的。 ... 然而，知道什么时候不一致——有时风格指南的建议并不适用。 如有疑问，请使用您的最佳判断。 查看其他示例并确定最好的示例。 不要犹豫，问！

## 入门

考虑到这一点，我们为 Python 项目创建了一个数据科学 `cookiecutter` 模板。 您的分析不必使用 Python，但模板确实提供了一些您想要删除的 Python 样板文件（在 `src`例如文件夹，以及 mdocs 文档骨架 docs).
要求

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

## 意见

项目结构中隐含了一些意见，这些意见是根据我们在数据科学项目上合作时对什么有效和什么无效的经验得出的。 有些意见是关于工作流程的，有些意见是关于让生活更轻松的工具的。 以下是构建该项目的一些信念——如果您有任何想法，请 贡献或分享 。
数据是不可变的

永远不要编辑原始数据，尤其不要手动编辑，尤其不要在 Excel 中编辑。 不要覆盖您的原始数据。 不要保存原始数据的多个版本。 将数据（及其格式）视为不可变的。 您编写的代码应该通过管道将原始数据移动到您的最终分析。 您不必每次想制作新图形时都运行所有步骤（请参阅 分析是 DAG ），但任何人都应该能够仅使用中的代码重现最终产品 src和数据在 data/raw.

此外，如果数据是不可变的，则它不需要像代码那样需要源代码控制。 因此， 默认情况下，数据文件夹包含在 .gitignore文件。 如果您有很少更改的少量数据，您可能希望将数据包含在存储库中。 Github 目前会在文件超过 50MB 时发出警告并拒绝超过 100MB 的文件。 存储/同步大数据的其他一些选项包括 AWS S3 （例如， 带有同步工具的 s3cmd)、 Git 大文件存储 、 Git 附件 和 dat 。 目前默认情况下，我们要求一个 S3 存储桶并使用 AWS CLI 同步数据 data与服务器的文件夹。
笔记本是用来探索和交流的

和其他文学编程工具等笔记本包 Jupyter notebook 、 Beaker notebook 、 Zeppelin 对于探索性数据分析非常有效。 但是，这些工具在重现分析方面可能不太有效。 我们在工作中使用笔记本的时候，往往会细分 notebooks文件夹。 例如， notebooks/exploratory包含初步探索，而 notebooks/reports是更精致的作品，可以作为 html 导出到 reports目录。

由于笔记本是源代码控制的挑战性对象（例如，差异 json通常不是人类可读的，合并几乎是不可能的），我们建议不要在 Jupyter notebooks 上直接与他人合作。 我们推荐两个有效使用笔记本的步骤：

    遵循显示所有者和分析完成顺序的命名约定。我们使用格式 <step>-<ghuser>-<description>.ipynb（例如， 0.3-bull-visualize-distributions.ipynb).

    重构好的部分。 不要编写代码在多个笔记本中执行相同的任务。 如果是数据预处理任务，就放到pipeline中 src/data/make_dataset.py并从加载数据 data/interim. 如果它是有用的实用程序代码，请将其重构为 src.

现在默认情况下，我们将项目转换为 Python 包（请参阅 setup.py文件）。 您可以导入您的代码并在带有如下单元格的笔记本中使用它：

# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset

分析是有向无环图（ DAG ）

通常在分析中，您需要长时间运行的步骤来预处理数据或训练模型。 如果这些步骤已经运行（并且您已将输出存储在某处，例如 data/interim目录），您不想每次都等待重新运行它们。 我们喜欢 make用于管理相互依赖的步骤，尤其是长期运行的步骤。 Make 是基于 Unix 的平台上的常用工具（并且 可用于 Windows ）。 继 make文档 、 Makefile 约定 和 可移植性指南 将有助于确保您的 Makefile 跨系统有效工作。 下面 一些 示例 是 入门 。 许多数据人员使用 make作为他们选择的工具，包括 Mike Bostock 。

还有其他用于管理 DAG 的工具，它们是用 Python 而不是 DSL 编写的（例如 Paver 、 Luigi 、 Airflow 、 Snakemake 、 Ruffus 或 Joblib ）。 如果它们更适合您的分析，请随意使用它们。
从环境开始构建

重现分析的第一步始终是重现运行它的计算环境。您需要相同的工具、相同的库和相同的版本才能使所有内容很好地协同工作。

一种有效的方法是使用 virtualenv （我们推荐使用 virtualenvwrapper 来管理 virtualenvs）。 通过在存储库中列出您的所有需求（我们包括一个 requirements.txt文件），您可以轻松跟踪重新创建分析所需的包。 这是一个很好的工作流程：

    跑 mkvirtualenv创建新项目时
    pip install您的分析需要的包
    跑 pip freeze > requirements.txt固定用于重新创建分析的确切包版本
    如果你发现你需要安装另一个包，运行 pip freeze > requirements.txt再次将更改提交到版本控制。

如果您对重新创建环境有更复杂的要求，请考虑使用基于虚拟机的方法，例如 Docker 或 Vagrant 。 这两种工具都使用基于文本的格式（分别是 Dockerfile 和 Vagrantfile），您可以轻松地将其添加到源代码管理中，以描述如何创建具有所需要求的虚拟机。
将秘密和配置置于版本控制之外

您 真的 不想在 Github 上泄露您的 AWS 密钥或 Postgres 用户名和密码。 说得够多了——请参阅关于这一点的 十二因素应用程序 原则。 这是执行此操作的一种方法：
将您的秘密和配置变量存储在一个特殊文件中

创建一个 .env项目根文件夹中的文件。 非常感谢 .gitignore，此文件永远不应提交到版本控制存储库中。 这是一个例子：

# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something

使用包自动加载这些变量。

如果您查看中的存根脚本 src/data/make_dataset.py，它使用一个名为 python-dotenv 的包将此文件中的所有条目加载为环境变量，以便可以访问它们 os.environ.get. 这是改编自 python-dotenv文档：

# src/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")

AWS CLI 配置

使用 Amazon S3 存储数据时，管理 AWS 访问的一种简单方法是将访问密钥设置为环境变量。 然而，在一台机器上管理多组密钥（例如，在处理多个项目时）最好使用 凭证文件 ，通常位于 ~/.aws/credentials. 一个典型的文件可能如下所示：

[default]
aws_access_key_id=myaccesskey
aws_secret_access_key=mysecretkey

[another_project]
aws_access_key_id=myprojectaccesskey
aws_secret_access_key=myprojectsecretkey

您可以在初始化项目时添加配置文件名称； 假设没有设置适用的环境变量，默认情况下将使用配置文件凭据。
在更改默认文件夹结构时要保守

为了使这种结构广泛适用于许多不同类型的项目，我们认为最好的方法是自由地更改项目周围的文件夹 ， 的默认结构时要保守。 但在更改所有 项目

我们 创建了一个文件夹布局 专门针对建议添加、删除、重命名或移动文件夹的问题 标签。 更一般地说，我们还 创建了一个需求讨论标签。 为在实施之前应该进行仔细讨论和广泛支持的问题
贡献

Cookiecutter 数据科学项目固执己见，但不怕犯错。 最佳实践不断变化，工具不断发展，经验教训不断汲取。 该项目的目标是使开始、构建和共享分析变得更加容易。 拉取请求 和 归档问题 鼓励 。 我们很想听听什么对您有用，什么不适合您。

如果您使用 Cookiecutter 数据科学项目，请链接回此页面或 给我们打电话 让 我们知道 ！
相关项目和参考资料的链接

项目结构和可重复性在 R 研究社区中讨论得更多。 如果您在 R 中工作，这里有一些项目和博客文章可能会对您有所帮助。

    项目模板 - 一个 R 数据分析模板
    “ 设计项目” Nice R 代码上的
    “ 我的研究工作流程” Carlboettiger.info 上的
    组织 计算生物学项目的快速指南” PLOS Computational Biology 中的“

最后，非常感谢 Cookiecutter 项目 ( github )，它帮助我们所有人花更少的时间思考和编写样板文件，将更多的时间用于完成工作。 
