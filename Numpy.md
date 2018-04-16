> ![Numpy](http://upload-images.jianshu.io/upload_images/3203841-3a73a59e2b242150.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>NumPy是Python语言的一个扩充程序库。支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。Numpy内部解除了Python的PIL(全局解释器锁),运算效率极好,是大量机器学习框架的基础库!


## Numpy简单创建数组
```python
import numpy as np
# 创建简单的列表
a = [1, 2, 3, 4]
# 将列表转换为数组
b = np.array(b)
```

## Numpy查看数组属性


#### 数组元素个数
```python
b.size
```
#### 数组形状
```python
b.shape
```
#### 数组维度

```python
b.ndim
```

#### 数组元素类型
```python
b.dtype
```


## 快速创建N维数组的api函数

- 创建10行10列的数值为浮点1的矩阵

```python
array_one = np.ones([10, 10])
```

- 创建10行10列的数值为浮点0的矩阵

```python
array_zero = np.zeros([10, 10])
```

- 从现有的数据创建数组
  - array(深拷贝)
  - asarray(浅拷贝)

## Numpy创建随机数组`np.random`

- ####均匀分布
  
  - `np.random.rand(10, 10)`创建指定形状(示例为10行10列)的数组(范围在0至1之间)
  - `np.random.uniform(0, 100)`创建指定范围内的一个数
  - `np.random.randint(0, 100)` 创建指定范围内的一个整数

- ####正态分布
  给定均值/标准差/维度的正态分布`np.random.normal(1.75, 0.1, (2, 3))`


- 数组的索引, 切片
```python
# 正态生成4行5列的二维数组
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)
```

> ![数组索引](http://upload-images.jianshu.io/upload_images/3203841-397821f4bbb7d18c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 改变数组形状(要求前后元素个数匹配)
> ![改变数组形状](http://upload-images.jianshu.io/upload_images/3203841-34375fe8c429b243.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
print("reshape函数的使用!")
one_20 = np.ones([20])
print("-->1行20列<--")
print (one_20)

one_4_5 = one_20.reshape([4, 5])
print("-->4行5列<--")
print (one_4_5)
```
# Numpy计算(重要)

### 条件运算
> ![原始数据](http://upload-images.jianshu.io/upload_images/3203841-96512a0877ab0be0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![条件判断](http://upload-images.jianshu.io/upload_images/3203841-9e4a2042696fe40f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
import numpy as np
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
stus_score > 80
```


> ![三目运算](http://upload-images.jianshu.io/upload_images/3203841-4bad94aa37f22c07.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
import numpy as np
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
np.where(stus_score < 80, 0, 90)
```

## 统计运算

- #### 指定轴最大值`amax`(参数1: 数组; 参数2: axis=0/1; 0表示列1表示行)

> ![求最大值](http://upload-images.jianshu.io/upload_images/3203841-209d2b8d83e9291a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一列的最大值(0表示列)
print("每一列的最大值为:")
result = np.amax(stus_score, axis=0)
print(result)

print("每一行的最大值为:")
result = np.amax(stus_score, axis=1)
print(result)
```


- #### 指定轴最小值`amin`

> ![求最小值](http://upload-images.jianshu.io/upload_images/3203841-0f034cd82426a780.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的最小值(0表示列)
print("每一列的最小值为:")
result = np.amin(stus_score, axis=0)
print(result)

# 求每一行的最小值(1表示行)
print("每一行的最小值为:")
result = np.amin(stus_score, axis=1)
print(result)
```


- #### 指定轴平均值`mean`
> ![求平均值](http://upload-images.jianshu.io/upload_images/3203841-02a0bff94816cdab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的平均值(0表示列)
print("每一列的平均值:")
result = np.mean(stus_score, axis=0)
print(result)

# 求每一行的平均值(1表示行)
print("每一行的平均值:")
result = np.mean(stus_score, axis=1)
print(result)
```

- #### 方差`std`
> ![求方差](http://upload-images.jianshu.io/upload_images/3203841-c985c2cde795e912.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的方差(0表示列)
print("每一列的方差:")
result = np.std(stus_score, axis=0)
print(result)

# 求每一行的方差(1表示行)
print("每一行的方差:")
result = np.std(stus_score, axis=1)
print(result)
```


## 数组运算

- #### 数组与数的运算
> ![加法](http://upload-images.jianshu.io/upload_images/3203841-2dbd6cdc79c07fb3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print("加分前:")
print(stus_score)

# 为所有平时成绩都加5分
stus_score[:, 0] = stus_score[:, 0]+5
print("加分后:")
print(stus_score)
```
> ![乘法](http://upload-images.jianshu.io/upload_images/3203841-685a27feb0c3a47c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print("减半前:")
print(stus_score)

# 平时成绩减半
stus_score[:, 0] = stus_score[:, 0]*0.5
print("减半后:")
print(stus_score)
```
- ####  数组间也支持加减乘除运算,但基本用不到
> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-c27afaef111daf23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a + b
d = a - b
e = a * b
f = a / b
print("a+b为", c)
print("a-b为", d)
print("a*b为", e)
print("a/b为", f)
```
## 矩阵运算`np.dot()`(非常重要)

> ![根据权重计算成绩](http://upload-images.jianshu.io/upload_images/3203841-28bdb90e9f27144e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- #### 计算规则
> (M行, N列) * (N行, Z列) = (M行, Z列) 


> ![矩阵计算总成绩](http://upload-images.jianshu.io/upload_images/3203841-d3ae003477155f11.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 平时成绩占40% 期末成绩占60%, 计算结果
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)
print("最终结果为:")
print(result)
```

- ##### 矩阵拼接

  - 矩阵垂直拼接

> ![垂直拼接](http://upload-images.jianshu.io/upload_images/3203841-29c4f1eb9a6d3409.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```python
print("v1为:")
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
print(v1)
print("v2为:")
v2 = [[12, 13, 14, 15, 16, 17], 
      [18, 19, 20, 21, 22, 23]]
print(v2)
# 垂直拼接
result = np.vstack((v1, v2))
print("v1和v2垂直拼接的结果为")
print(result)
```

- 矩阵水平拼接
>![水平拼接](http://upload-images.jianshu.io/upload_images/3203841-52b67b6a480aa91c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 
```python
print("v1为:")
v1 = [[0, 1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10, 11]]
print(v1)
print("v2为:")
v2 = [[12, 13, 14, 15, 16, 17], 
      [18, 19, 20, 21, 22, 23]]
print(v2)
# 垂直拼接
result = np.hstack((v1, v2))
print("v1和v2水平拼接的结果为")
print(result)
```

## Numpy读取数据`np.genfromtxt`
> ![csv文件以逗号分隔数据](http://upload-images.jianshu.io/upload_images/3203841-b4c47c46e94f472a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![读取csv格式的文件](http://upload-images.jianshu.io/upload_images/3203841-686307a57dc6211b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 如果数值据有无法识别的值出现,会以`nan`显示,`nan`相当于`np.nan`,为float类型.


























