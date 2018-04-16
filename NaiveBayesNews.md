![朴素贝叶斯](http://upload-images.jianshu.io/upload_images/3203841-a7352b6c766cecd4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> 朴素指的是"独立"
> 朴素贝叶斯是分类算法,可以给出每种类别发生的概率
> 善于计算几个独立事件同时发生的概率(文章分类)

## 关于独立事件(职业, 体型, 身高 各自独立)

样本编号 | 职业 | 体型 | 身高 | 女神的喜好
---| --- | --- | --- | ---
1 | 程序员| 匀称 | 很高 | 喜欢
2 | 产品 | 瘦 | 很矮 | 不看
3 | 美术 | 胖 | 中等 | 喜欢
4 | 产品 | 胖 | 中等 | 喜欢
5 | 程序员 | 胖 | 很矮 | 不看
6 | 美术 | 瘦 | 很高 | 不看

- ####在女神喜欢的条件下, 职业是产品,并且身高很高, 并且体型匀称的概率?  1/27
```
P(产品, 很高, 匀称,|女神喜欢) = P(产品 | 女神喜欢) * P(很高 | 女神喜欢)* P( 匀称 | 女神喜欢 ) 
1/27 = (1/3)*(1/3)*(1/3)
```

## 朴素贝叶斯公式:
> ![朴素贝叶斯](http://upload-images.jianshu.io/upload_images/3203841-893ff92422001b41.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> W为文章的特征组(特定文章中各词组出现的频率)，C为特定的类别
>![上式等价式](http://upload-images.jianshu.io/upload_images/3203841-c10e5f818d5a3a0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> - #### 公式右侧
> - P(F1, F2, ... | C) = P(F1 | C) * P(F2 | C) * (F... | C),表示 特定类别下,特定词组出现的概率  的乘积
> - P(C), 表示 特定类别的文章, 在所有文章中出现的概率
> - P(F1, F2, F...) = P(F1) * P(F2) * P(F...) , 表示 特定词组在所有文章中出现的概率  的乘积  



## 案例:为文章进行分类
```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def naivebayes():
    # 获取数据集级
    news = fetch_20newsgroups(subset="all")
    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 进行tfidf特征抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)

    # 通过朴素贝叶斯进行预测(拉普拉斯平滑系数为设置为1)
    mlb = MultinomialNB(alpha=1)
    mlb.fit(x_train, y_train)

    rate = mlb.score(x_test, y_test)
    print("预测准确率为:", rate)

if __name__ == '__main__':
    naivebayes()
```

> ![为文章进行分类](http://upload-images.jianshu.io/upload_images/3203841-35d4000cf67116c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

