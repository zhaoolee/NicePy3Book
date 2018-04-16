
> ![base64转换过程](http://upload-images.jianshu.io/upload_images/3203841-7a89603bdc2be46b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


>这几天写web,需要将用户上传的图片,实时显示到前端页面,然后通过Jcrop裁剪,并将裁剪后的图片通过canvas实时显示到前端,最后将canvas显示的图片装换为base64格式,传到后端django,但pillow是无法直接读取base64格式的图片的,所以特地查阅了一些资料,发现python3内置了base64转换函数,这里分享一下使用方法...

```python
import os, base64

# 图片装换
with open("./robot.png", "rb") as f:
	# 将读取的二进制文件转换为base64字符串
	bs64_str = base64.b64encode(f.read())
	# 打印图像转换base64格式的字符串,type结果为<class 'bytes'>
	print(bs64_str, type(bs64_str))
	# 将base64格式的数据装换为二进制数据
	imgdata = base64.b64decode(bs64_str)
	# 将二进制数据装换为图片
	with open("./robot2.png", "wb") as f2:
		f2.write(imgdata)

```

# base64使用场景
##### 对某些无关紧要的信息进行表面加密,也就是说不行让别人看到你明文传数据,但别人看到也是无所谓的(浏览器可以直接解析base64格式的图片文件)




> base64加密文本
```python
import os, base64
# 文本简单加密
bs64_my_time = base64.b64encode("真的羡慕你们这种18岁的,我还差15年呢!".encode("utf-8"))
print("bs64格式的文本(伪加密)",bs64_my_time)
my_time = base64.b64decode(bs64_my_time).decode("utf-8")
print("原文本:",my_time)
```
> ![伪加密](http://upload-images.jianshu.io/upload_images/3203841-476cd5e6c67be10b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### base64图片在网页上的表现形式
```html
<html><body><img src="data:image/jpeg;base64,这里放的是base64编码" /></body></html>
```
```python
# 使用正则从上面src中抽取base64格式的图片信息
file = re.match(r"data:image/jpeg;base64,(.*)", file).group(1)
```

