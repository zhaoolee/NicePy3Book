> Pillow是python的一个功能强大的图像处理的库,可对图像进行高质量的压缩变换等操作,前几天看到一些公众号,提供了为用户头像加装饰的操作,于是自己试了一下,20行搞定!

> 网络上能看到的拼接图片的教程,需要手动指定透明位置,下面提供的方法,直接分离了透明图层,可简单快速的图像拼接;而且实现了图片尺寸的简单变换,用户提供任意尺寸的图片,都可以输出300*300的标准头像尺寸

原图:
![image1.png](http://upload-images.jianshu.io/upload_images/3203841-9372713a2555b430.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![hnu.png](http://upload-images.jianshu.io/upload_images/3203841-e7bdb9b60249e002.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
效果图:
![f.png](http://upload-images.jianshu.io/upload_images/3203841-03e013675e3fbd79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 源码:
```python
from PIL import Image
#创建底图
target = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
#打开头像
nike_image = Image.open("./image1.png")
nike_image = nike_image.resize((300, 300))
#打开装饰
hnu_image = Image.open("./hnu.png")
# 分离透明通道
r,g,b,a = hnu_image.split()
# 将头像贴到底图
nike_image.convert("RGBA")
target.paste(nike_image, (0,0))

#将装饰贴到底图
hnu_image.convert("RGBA")
target.paste(hnu_image,(0,0), mask=a)

# 保存图片
target.save("f.png")
```
## [资源](code/)

