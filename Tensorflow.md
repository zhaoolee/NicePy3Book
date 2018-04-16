# 安装Tensoflow1.0

## Linux/ubuntu:
- python2.7: 
```
pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp27-none-linux_x86_64.whl
``` 
- python3.5:
``` 
pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp35-cp35m-linux_x86_64.whl 
```

## Maxos:

- python2: 
```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py2-none-any.whl
```
- python3: 
```
pip3 install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl
```

### Tensorflow完成加法

```python
import tensorflow as tf
# 消除警告(使用源码安装可自动消除)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(3.0)
b = tf.constant(4.0)

with tf.Session() as sess:
    a_b = tf.add(a, b)
    print("相加后的类型为")
    print(a_b)
    print("真正的结果为:")
    print(sess.run(a_b))
```

> ![tf_add](http://upload-images.jianshu.io/upload_images/3203841-8623ba38fff3f1e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 将加法运算以图形化方式展示

- 在会话中添加记录文件的语句
```python
import tensorflow as tf
# 消除警告(使用源码安装可自动消除)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(3.0)
b = tf.constant(4.0)

with tf.Session() as sess:
    a_b = tf.add(a, b)
    print("相加后的类型为")
    print(a_b)
    print("真正的结果为:")
    print(sess.run(a_b))
    # 添加board记录文件
    file_write = tf.summary.FileWriter('/Users/lijianzhao/tensorBoard/', graph=sess.graph)
```


- 在终端运行`tensorboard --logdir="/Users/lijianzhao/tensorBoard/"`

> ![在终端运行tensorboard](http://upload-images.jianshu.io/upload_images/3203841-7f580de4bbd3557a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 根据终端提示,在浏览器键入`http://192.168.199.213:6006`

>![tensorboard主界面](http://upload-images.jianshu.io/upload_images/3203841-60948a962d46fe3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- 选择GRAPHS
>![选择GRAPHS](http://upload-images.jianshu.io/upload_images/3203841-6d90eb835a11e64b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 实现简单的线性回归
```python
import tensorflow as tf
# 消除警告(使用源码安装可自动消除)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 回归函数
def my_regression():

    # 准备10000 条数据x的平均值为5.0 标准差为1.0
    x = tf.random_normal([100, 1], mean = 5.0, stddev=1.0, name="x")
    # 真实的关系为 y = 0.7x + 0.6
    y_true = tf.matmul(x, [[0.7]]) + 0.6

    # 创建权重变量
    weight = tf.Variable(tf.random_normal([1, 1], mean=1.0, stddev=0.1), name="weight")

    # 创建偏置变量,初始值为1
    bias = tf.Variable(1.0, name="bias")

    # 预测结果
    y_predict = tf.matmul(x, weight) + bias

    # 计算损失
    loss = tf.reduce_mean(tf.square(y_predict - y_true))

    # 梯度下降减少损失,每次的学习率为0.1
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    # 收集变量
    tf.summary.scalar("losses", loss)
    tf.summary.histogram("weightes", weight)

    # 合并变量
    merged = tf.summary.merge_all()

    # 初始化变量
    init_op = tf.global_variables_initializer()

    # 梯度下降优化损失
    with tf.Session() as sess:
        sess.run(init_op)

        print("初始的权重为{}, 初始的偏置为{}".format(weight.eval(), bias.eval()))

        # 添加board记录文件
        file_write = tf.summary.FileWriter('/Users/lijianzhao/tensorBoard/my_regression', graph=sess.graph)


        # 循环训练线性回归模型
        for i in range(20000):
            sess.run(train_op)
            print("训练第{}次的权重为{}, 偏置为{}".format(i,weight.eval(), bias.eval()))

            # 观察每次值的变化
            # 运行merge
            summery = sess.run(merged)
            # 每次收集到的值添加到文件中
            file_write.add_summary(summery, i)


if __name__ == '__main__':
    my_regression()
```

> ![运行结果](http://upload-images.jianshu.io/upload_images/3203841-8d0fa7431af61aa0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![程序流程图](http://upload-images.jianshu.io/upload_images/3203841-749900c1bb0b72fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![损失值降低](http://upload-images.jianshu.io/upload_images/3203841-0df2de6f8c687ae3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

>![权重逐渐接近真实值](http://upload-images.jianshu.io/upload_images/3203841-437461fa51faf696.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 为程序添加作用域
```python
import tensorflow as tf
# 消除警告(使用源码安装可自动消除)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 回归函数
def my_regression():

    # 准备数据
    with tf.variable_scope("data"):
        # 准备10000 条数据x的平均值为5.0 标准差为1.0
        x = tf.random_normal([100, 1], mean = 5.0, stddev=1.0, name="x")
        # 真实的关系为 y = 0.7x + 0.6
        y_true = tf.matmul(x, [[0.7]]) + 0.6

    # 创建模型
    with tf.variable_scope ("model"):
        # 创建权重变量
        weight = tf.Variable(tf.random_normal([1, 1], mean=1.0, stddev=0.1), name="weight")

        # 创建偏置变量,初始值为1
        bias = tf.Variable(1.0, name="bias")

        # 预测结果
        y_predict = tf.matmul(x, weight) + bias

    # 计算损失
    with tf.variable_scope ("loss"):
        # 计算损失
        loss = tf.reduce_mean(tf.square(y_predict - y_true))

    # 减少损失
    with tf.variable_scope("optimizer"):
        # 梯度下降减少损失,每次的学习率为0.1
        train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    # 收集变量
    tf.summary.scalar("losses", loss)
    tf.summary.histogram("weightes", weight)

    # 合并变量
    merged = tf.summary.merge_all()

    # 初始化变量
    init_op = tf.global_variables_initializer()

    # 梯度下降优化损失
    with tf.Session() as sess:
        sess.run(init_op)
        print("初始的权重为{}, 初始的偏置为{}".format(weight.eval(), bias.eval()))
        # 添加board记录文件
        file_write = tf.summary.FileWriter('/Users/lijianzhao/tensorBoard/my_regression', graph=sess.graph)
        # 循环训练线性回归模型
        for i in range(20000):
            sess.run(train_op)
            print("训练第{}次的权重为{}, 偏置为{}".format(i,weight.eval(), bias.eval()))
            # 观察每次值的变化
            # 运行merge
            summery = sess.run(merged)
            # 每次收集到的值添加到文件中
            file_write.add_summary(summery, i)

if __name__ == '__main__':
    my_regression()

```

>![添加作用域](http://upload-images.jianshu.io/upload_images/3203841-8100ebba4bdc0b98.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 模型的保存与恢复(保存会话资源)

- 创建保存模型的saver
```python
saver = tf.train.Saver()
```
- 保存模型
```python
saver.save(sess, "./tmp/ckpt/test")
```
- 恢复模型
```python
save.restore(sess, "./tmp/ckpt/test")
```


