> K近邻思想: 根据你的"邻居们"来确定你的类别

> 你一觉醒来,不知道自己身在何方里,你能通过计算机定位到周围5个"最近的"邻居,其中有4个身处火星,1个身处月球,你认为应该自己距火星更近,自己应该在火星...(K近邻算法又称为Knn算法,属于分类算法)

# 案例1

```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def knncls():

    """
    预测电影分类
    :return:
    """
    data = pd.read_csv("./data/movies.csv")
    # 提取特征值, 目标值
    x = data.drop(["type", "movie_name"], axis=1)
    y = data["type"]
    # 分割数据集
    x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.25)

    # 通过knn进行预测
    knn = KNeighborsClassifier()

    knn.fit(x_train, y_train)

    y_predict = knn.predict(x_test)
    print(x_test, "的预测结果为:", y_predict)

    print("预测准确率为:", knn.score(x_test, y_test))

if __name__ == '__main__':
    knncls()
```
> ![准确率](http://upload-images.jianshu.io/upload_images/3203841-249c12af6b219b58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
movie_name,fight,kiss,type
California Man,3,104,1
He's not Really into dues,2,100,1
Beautiful Woman,1,81,1
Kevin Longblade,101,10,2
Robo Slayer 3000,99,5,2
Amped II,98,2,2
unname,18,90,1
vampire,90,15,2
```



# 案例2 [Facebook入住地点](https://www.kaggle.com/c/facebook-v-predicting-check-ins/data)
>![facebook预测入住地点](http://upload-images.jianshu.io/upload_images/3203841-55688330701f46f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![train_data](http://upload-images.jianshu.io/upload_images/3203841-242eb6724ff0d18a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def knncls():
    """
    facebook题目:k近邻算法预测入住位置
    :return:
    """
    # 使用pandas读取100000数据
    train_data = pd.read_csv("./data/fb/train.csv", nrows = 100000)

    # 特征工程
    # 1.缩小x,y的范围
    train_data = train_data.query("x>1.0 & x<1.5 & y>1.0 & y<2.5")

    # 2.解析时间戳
    time_value = pd.to_datetime(train_data["time"], unit="s")
    time_value = pd.DatetimeIndex(time_value)

    # 3.添加特征(时间)
    train_data["weekday"] = time_value.weekday
    train_data["year"] = time_value.day
    train_data["hour"] = time_value.hour
    train_data["minute"] = time_value.minute

    # 4.删除特征(时间戳)
    train_data = train_data.drop(["time"], axis=1)

    # 5.只保留入住人数大于5的place,生成新的train_data
    place_count = train_data.groupby("place_id").count()
    place_count_r = place_count[place_count.row_id > 3].reset_index()
    train_data = train_data[train_data["place_id"].isin(place_count_r["place_id"])]

    # 提取特征值和目标值
    x = train_data.drop(["place_id", "row_id"], axis=1)

    y = train_data["place_id"]

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行标准化
    std = StandardScaler()

    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 实例化knn估计器
    knn = KNeighborsClassifier()

    knn.fit(x_train, y_train)

    # 预测结果
    y_predict = knn.predict(x_test)

    # 打印准确率
    print("准确率为:",knn.score(x_test, y_test))

    return None

if __name__ == '__main__':
    knncls()
```
