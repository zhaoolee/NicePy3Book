> ![pandas](http://upload-images.jianshu.io/upload_images/3203841-b75459db6e582aa8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> #### Pandas是基于Numpy开发出的,专门用于数据分析的开源Python库

# Pandas的两大核心数据结构
- Series(一维数据)
> ![Series](http://upload-images.jianshu.io/upload_images/3203841-11b74156da497fa7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![创建Series的方法](http://upload-images.jianshu.io/upload_images/3203841-9dcf6c4eca606bec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![允许索引重复](http://upload-images.jianshu.io/upload_images/3203841-b3b9ead61722c10e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- DataFrame(多特征数据,既有行索引,又有列索引)
> ![DataFrame](http://upload-images.jianshu.io/upload_images/3203841-3831067a3d900038.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![索引方法](http://upload-images.jianshu.io/upload_images/3203841-0dab7ce3b482ae8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 创建一个3行4列的DataFrame类型数据
data_3_4 = pd.DataFrame(np.arange(10, 22).reshape(3, 4))
# 打印数据
print(data_3_4)

# 打印第一行数据
print(data_3_4[:1])
# 打印第一列数据
print(data_3_4[:][0])
```
  - DataFrame的属性
> ![原始数据](http://upload-images.jianshu.io/upload_images/3203841-ff2cd0903fb0235e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![DataFrame的属性](http://upload-images.jianshu.io/upload_images/3203841-1c21986007d40675.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
# 读取数据
result = pd.read_csv("./students_score.csv")
# 数据的形状
result.shape
# 每列数据的 类型信息
result.dtypes
# 数据的维数
result.ndim
# 数据的索引(起/始/步长)
result.index
# 打印每一列 属性的名称
result.columns
# 将数据放到数组中显示
result.values
```
> ![整体查询](http://upload-images.jianshu.io/upload_images/3203841-0cea033b45f06402.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
# 打印前5个
print("-->前5个:")
print(result.head(5))
# 打印后5个
print("-->后5个:")
print(result.tail(5))
# 打印描述信息(实验中好用)
print("-->描述信息:")
print(result.describe())
```


# Panda数据读取(以csv为例)
```
pandas.read_csv(filepath_or_buffer, sep=",", names=None, usecols = None)

filepath_or_buffer : 文件路径(本地路径或url路径)
sep: 分隔符
names: 列索引的名字
usecols: 指定读取的列名

返回的类型: DataFrame  
```
> ![读取并返回数据](http://upload-images.jianshu.io/upload_images/3203841-b67496680d23533c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- Dataframe通过布尔索引过滤数据

> ![布尔索引](http://upload-images.jianshu.io/upload_images/3203841-6b274c2e96d5a9e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
# 布尔索引(查询) 找出年龄大于23岁的人
result[result["age"]>23]
```

## 小案例: 分析2006年至2016年1000部IMDB[电影数据](https://www.kaggle.com/damianpanek/sunday-eda/data)
> ![2006年----2016年IMDB最受欢迎的1000部电影](http://upload-images.jianshu.io/upload_images/3203841-f95f29435413d64d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![评分降序排列](http://upload-images.jianshu.io/upload_images/3203841-c890999f37c7d582.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![统计时长](http://upload-images.jianshu.io/upload_images/3203841-6a88b0abc9db4e7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
IMDB_1000 = pd.read_csv("./IMDB-Movie-Data.csv")
# 获取数据字段
print(IMDB_1000.dtypes)
# 根据1000部电影评分进行降序排列,参数ascending, 默认为True(升序), 这里为False(降序)
IMDB_1000.sort_values(by="Rating", ascending=False)
# 时间最长的电影
IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].max()]
# 时间最短的电影
IMDB_1000[IMDB_1000["Runtime (Minutes)"]==IMDB_1000["Runtime (Minutes)"].min()]
# 电影时长平均值
IMDB_1000["Runtime (Minutes)"].mean()
```
# 数据处理

- 存在缺失值, 直接删除数据(删除存在缺失值的样本)

> ![删除存在缺失值的样本](http://upload-images.jianshu.io/upload_images/3203841-31b0796323226d06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 删除存在缺失值的样本
IMDB_1000.dropna()
```

> 不推荐的操作: 按列删除缺失值为`IMDB_1000.dropna(axis=1)`

- 存在缺失值, 直接填充数据`fillna`

> ![填充空缺值](http://upload-images.jianshu.io/upload_images/3203841-60d78204cb5999de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![使用平均值填充数据](http://upload-images.jianshu.io/upload_images/3203841-137381be43209c63.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
# 为一些电影缺失的总票房添加平均值
IMDB_1000["Revenue (Millions)"].fillna(IMDB_1000["Revenue (Millions)"].mean(), inplace=True)
```


### 小案例: 乳腺癌数据预处理 (在线获取数据,并替换缺失符号为标准缺失符号`np.nan`)
>![替换默认的缺失符号](http://upload-images.jianshu.io/upload_images/3203841-f00ebb389a88a552.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>![各列命名](http://upload-images.jianshu.io/upload_images/3203841-f99f946dd3dea81d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![读取原始数据](http://upload-images.jianshu.io/upload_images/3203841-1f0b98d7084ea9ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
# 在线读取数据,并按照说明文档, 并对各列信息进行命名
bcw = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", names=["Sample code number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape", "Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class:"])
```

> ![预处理,把?替换为np.nan](http://upload-images.jianshu.io/upload_images/3203841-5f0e260d39f78178.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 小案例: 日期格式转换 [数据来源](https://www.kaggle.com/c/facebook-v-predicting-check-ins/data)
> ![facebook](http://upload-images.jianshu.io/upload_images/3203841-650c4c9c9eb0e906.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![日期格式转换](http://upload-images.jianshu.io/upload_images/3203841-c486f8310732eaa6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 读取前10行数据
train = pd.read_csv("./train.csv", nrows = 10)
# 将数据中的time转换为最小分度值为秒(s)的计量单位
train["time"] = pd.to_datetime(train["time"], unit="s")
```
- 从日期中拆分出新的列

> ![新增列](http://upload-images.jianshu.io/upload_images/3203841-2a9b57d53aa84fdb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 新增列year, month, weekday
train["year"] = pd.DatetimeIndex(train["time"]).year
train["month"] = pd.DatetimeIndex(train["time"]).month
train["weekday"] = pd.DatetimeIndex(train["time"]).weekday
```

## 数据表的合并(merge)
>![数据](http://upload-images.jianshu.io/upload_images/3203841-ee56e74477752900.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```csv
user_info.csv
user_id,姓名,age
1,徐三,23
2,徐四,22
3,宝儿,210
4,楚岚,21
5,王也,24
6,诸葛青,21
7,天师,89
8,吕梁,24
9,夏禾,26
```
```csv
goods_info.csv
goods_id,goods_name
G10,三只松鼠
G12,MacBook
G13,iPad
G14,iPhone
```
```csv
order_info.csv
order_id,use_id,goods_name
as789,1,三只松鼠
sd567,2,MacBook
hj456,4,iPad
```

> ![合并过程](http://upload-images.jianshu.io/upload_images/3203841-959cc6c098613eaa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 读取3张表
user_info = pd.read_csv("./user_info.csv")
order_info = pd.read_csv("./order_info.csv")
goods_info = pd.read_csv("./goods_info.csv")
# 合并三张表
u_o = pd.merge(user_info, order_info, how="left", on=["user_id", "user_id"])
u_o_g = pd.merge(u_o, goods_info, how="left", on=["goods_name", "goods_name"])
```

  - 建立交叉表(用于计算分组的频率)
> ![交叉表](http://upload-images.jianshu.io/upload_images/3203841-bbc515c78c1ef3db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
# 交叉表, 表示出用户姓名,和商品名之间的关系
user_goods = pd.crosstab(u_o_g["姓名"],u_o_g["goods_name"])
```

# Pandas的分组和聚合(重要)
> 小案例: 星巴克全球分布情况       [数据来源](https://www.kaggle.com/starbucks/store-locations)
> ![全球星巴克分布情况](http://upload-images.jianshu.io/upload_images/3203841-5ae66ce5892be18f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![读取全球星巴克的位置数据](http://upload-images.jianshu.io/upload_images/3203841-6a6a9a71c0dddc64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![每个国家星巴克的数量](http://upload-images.jianshu.io/upload_images/3203841-545dd2b697deb9f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![每个国家每个省份星巴克的数量](http://upload-images.jianshu.io/upload_images/3203841-328c7e7c70559166.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
starbucks = pd.read_csv("./directory.csv")
# 统计每个国家星巴克的数量
starbucks.groupby(["Country"]).count()
# 统计每个国家 每个省份 星巴克的数量
starbucks.groupby(["Country", "State/Province"]).count()
```

- 全球各国星巴克数量排名
> ![全球星巴克数量排名](http://upload-images.jianshu.io/upload_images/3203841-681b0c70b6752df8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




