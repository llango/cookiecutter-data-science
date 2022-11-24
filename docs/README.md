文档生成
----------

安装依赖:

    pip install -r requirements.txt

进入docs目录:

    cd docs

使用 [mkdocs](http://www.mkdocs.org/) 结构更新文档。 在本地测试： 

    mkdocs serve

一旦文档看起来不错，发布到 `gh-pages` 分支:

    mkdocs gh-deploy --clean

**注意**：切勿手动编辑生成的站点，因为使用 `gh-deploy` 吹走 `gh-pages` 分支，您将丢失您的编辑。 
