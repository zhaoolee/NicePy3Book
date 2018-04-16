>1912年4月15日凌晨2点20分,“永不沉没”的“泰坦尼克”走完了它短暂的航程,缓缓沉入大西洋这座安静冰冷的坟墓。
>![Titanix](http://upload-images.jianshu.io/upload_images/3203841-e379709bcab0cf53.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>欢迎你们说我幼稚荒诞，也欢迎你们继续成熟苍凉。说起来，titanic是我至今觉得最为美妙的爱情电影，如饮蜜酒，甘不可言。这是一份绚烂到极致，使得人类的大难做了背景，还妄想突破时间和生死直达永恒的爱情。露丝从救生船上一跃而起，扑到窗边的一刹，因了这份勇敢和贪求，最为美丽。在有生的瞬间能遇到你，竟花光所有运气。

>you're going to go on and you're going to make babies and watch them grow and you're going to die an old lady. 
你将长寿，子孙满堂
---
> 乘客存活数据:http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt

### 这里用决策树算法,按照乘客的社会阶层(pclass),年龄(age), 性别(sex)三个因素,来预测乘客最终的生存状况(survived) 

```python

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import  DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier


def descsion():
    # 获取数据, 提取特征值和目标值
    Titanic_data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 打印字段名
    print(Titanic_data.columns)

    # 分割出特定的字段(社会阶层, 年龄, 性别)对生存率的影响
    titanic_x = Titanic_data[["pclass", "age", "sex"]]
    titanic_y = Titanic_data[["survived"]]
    # 处理缺失值
    titanic_x["age"].fillna(titanic_x['age'].mean(), inplace=True)

    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(titanic_x, titanic_y, train_size=0.25)

    # 对特征们进行字典特征抽取
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    x_test = dict.transform(x_test.to_dict(orient="records"))

    # 查看抽取后特征的名字
    feature_names = dict.get_feature_names()
    print(feature_names)


    # 进行决策树预测(可选:限制决策树最大深度为10)
    my_decision_tree = DecisionTreeClassifier(max_depth=10)
    my_decision_tree.fit(x_train, y_train)

    print("单棵决策树预测的准确率为:", my_decision_tree.score(x_test, y_test))

    # 将树的结构保存到本地
    export_graphviz(my_decision_tree, "./my_decision_tree.dot", feature_names = feature_names)

    """
    将dot文件装换为png的方法
    在本机安装graphviz ubuntu版安装: sudo apt install graphviz   mac版安装: brew install graphviz
    然后运行命令: dot -Tpng my_decision_tree.dot -o my_decision_tree.png
    生成png格式图片my_desion_tree.png
    """
    # 随机树森林算法, 建立20棵数, 树的最大深度为15
    rf = RandomForestClassifier(n_estimators=21, max_depth=20)
    rf.fit(x_train, y_train)
    print("随机数森林预测的准确率为:", rf.score(x_test, y_test))

if __name__ == '__main__':
    descsion()


```
>![运行结果](http://upload-images.jianshu.io/upload_images/3203841-823bfaf7847a991d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###  使用graphviz绘制决策树
#### 1. 安装graphviz
- ubuntu安装方式:
```
sudo apt install graphviz
```
- mac安装方式
```
brew install graphviz
```

#### 2. 通过终端,在.dot所在的目录运行命令,将.dot转换为png图片

```
dot -Tpng my_decision_tree.dot -o my_decision_tree.png
```

> ![my_decision_tree](http://upload-images.jianshu.io/upload_images/3203841-49d43aa8bc6e6025.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>那些古板的绅士们要死得很体面。女士和儿童先上，男人们等待死亡。船上的乐队，从容演奏到了最后一刻。谁能告诉我，身边是世界末日的惊恐，但依然安静地演奏，是因为拥有了什么样的力量？  “很高兴今晚和你们合作。”想起另外一部电影的一句台词：“假装我们明天还会再见。”生离死别，说了再见，但是没有明天。
