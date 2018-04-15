> 虽然Word不好用, 但还必须得用它, `python-docx`是专门用于编辑Word文档的一个工具库, 它有两大用途, 自动化生成word文档 and 自动化修改文档

> ![python word](https://upload-images.jianshu.io/upload_images/3203841-e43426023adb4c22.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 1. 自定义样式
> ![自定义样式](https://upload-images.jianshu.io/upload_images/3203841-2cb4601539d3030b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### python可以自定义三类样式
- 段落样式
- 字符样式
- 表格样式(一般用不到)
> 这三类样式的创建方式基本一致, 只是创建参数 略有不同(1为段落样式, 2为字符样式, 3为表格样式)
#### 以设置段落样式为例
```
	# 创建自定义段落样式(第一个参数为样式名, 第二个参数为样式类型, 1为段落样式, 2为字符样式, 3为表格样式)
	UserStyle1 = document.styles.add_style('UserStyle1', 1)
	# 设置字体尺寸
	UserStyle1.font.size = Pt(40)
	# 设置字体颜色
	UserStyle1.font.color.rgb = RGBColor(0xff, 0xde, 0x00)
	# 居中文本
	UserStyle1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
	# 设置中文字体
	UserStyle1.font.name = '微软雅黑'
	UserStyle1._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
```

## 2.理解结构关系
> ![结构关系](https://upload-images.jianshu.io/upload_images/3203841-ac4730390ed1165b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 往文档中插入文本内容, 首先要插入一个段落, 段落后面可追加字符, 但文档不能直接插入字符
- 段落之间会自动以 回车符号 分隔
- 段落 和 字符 可 各自设置独立的样式

#### 实例: 插入段落, 插入段落后追加字符
```
	# 使用自定义段落样式
	document.add_paragraph('自定义段落样式', style = UserStyle1)

	# 使用自定义字符样式
	document.add_paragraph('').add_run('正月里采花无哟花采，二月间采花花哟正开，二月间采花花哟正开。三月里桃花红哟似海，四月间葡萄架哟上开，四月间葡萄架哟上开。', style = UserStyle2)
```

 ## 3. 插入图片
> python-docx支持将图片插入文档, 且可以设置图片大小
> ![插入图片](https://upload-images.jianshu.io/upload_images/3203841-093e8662c378a0b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 实例代码:
```
	document.add_picture('少女17087938.jpg', width=Inches(5))
```
## 4.插入列表
> ![插入列表](https://upload-images.jianshu.io/upload_images/3203841-3f92cf56ada01dee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 插入有序列表
```
	document.add_paragraph('把冰箱门打开', style='List Number')
	document.add_paragraph('把大象装进去', style='List Number')
	document.add_paragraph('把冰箱门关上', style='List Number')
```
#### 插入无序列表
```
	document.add_paragraph('天地匆匆 惊鸿而过 路有千百个', style='List Bullet')
	document.add_paragraph('遑遑无归 闲云逸鹤 人间红尘过', style='List Bullet')
	document.add_paragraph('引势而流 鸿门乱局 各有各选择', style='List Bullet')
	document.add_paragraph('乾震坎艮 坤巽离兑 定一切生克', style='List Bullet')
```

## 5.插入表格

> ![插入表格](https://upload-images.jianshu.io/upload_images/3203841-a76a1220ca92f528.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 把表格看做二维数组, 然后往数组中填数据

```python
	rows_num = 5
	cols_num = 6
	table = document.add_table(rows=rows_num, cols=cols_num, style = 'Table Grid')

	for r in range(rows_num):
		for c in range(cols_num):
			table.cell(r, c).text = "第{r}行{c}列".format(r = r+1, c = c+1)
```


## 完整源码:

```python
from docx import Document
from docx.shared import Inches
from docx.dml.color import ColorFormat
from docx.shared import Pt
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH

def main():
	# 创建文档对象
	document = Document()

	# 设置默认字体
	document.styles['Normal'].font.name = '微软雅黑'
	document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
	
	# 创建自定义段落样式(第一个参数为样式名, 第二个参数为样式类型, 1为段落样式, 2为字符样式, 3为表格样式)
	UserStyle1 = document.styles.add_style('UserStyle1', 1)
	# 设置字体尺寸
	UserStyle1.font.size = Pt(40)
	# 设置字体颜色
	UserStyle1.font.color.rgb = RGBColor(0xff, 0xde, 0x00)
	# 居中文本
	UserStyle1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
	# 设置中文字体
	UserStyle1.font.name = '微软雅黑'
	UserStyle1._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

	
	# 创建自定义字符样式(第一个参数为样式名, 第二个参数为样式类型, 1为段落样式, 2为字符样式, 3为表格样式)
	UserStyle2 = document.styles.add_style('UserStyle2', 2)
	# 设置字体尺寸
	UserStyle2.font.size = Pt(15)
	# 设置字体颜色0c8ac5
	UserStyle2.font.color.rgb = RGBColor(0x0c, 0x8a, 0xc5)
	# 设置段落样式为宋体
	UserStyle2.font.name = '宋体'
	UserStyle2._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')



	# 使用自定义段落样式
	document.add_paragraph('自定义段落样式', style = UserStyle1)

	# 使用自定义字符样式
	document.add_paragraph('').add_run('正月里采花无哟花采，二月间采花花哟正开，二月间采花花哟正开。三月里桃花红哟似海，四月间葡萄架哟上开，四月间葡萄架哟上开。', style = UserStyle2)


	# 设置粗体字
	document.add_paragraph('设置粗体字:').add_run('粗体字').bold = True

	# 设置斜体字
	document.add_paragraph('设置斜体字:').add_run('斜体字').italic = True

	# 设置字号50
	document.add_paragraph('设置字号50:').add_run('50').font.size = Pt(50)

	# 设置字体颜色为 af2626
	document.add_paragraph('设置字体颜色:').add_run('颜色').font.color.rgb = RGBColor(0xaf, 0x26, 0x26)

	# 样式叠加: 将字体改到30号并且将字体改成特定颜色;
	doubleStyle =  document.add_paragraph('同时设置文字颜色和字号:').add_run('颜色和尺寸')
	doubleStyle.font.size = Pt(30)
	doubleStyle.font.color.rgb = RGBColor(0xaf, 0x26, 0x26)

	# 添加分页符
	document.add_page_break()


	# 创建 有序列表	
	document.add_paragraph('').add_run('有序列表').font.size = Pt(30)
	document.add_paragraph('把冰箱门打开', style='List Number')
	document.add_paragraph('把大象装进去', style='List Number')
	document.add_paragraph('把冰箱门关上', style='List Number')

	# 创建 无序列表
	document.add_paragraph('').add_run('无序列表').font.size = Pt(30)
	document.add_paragraph('天地匆匆 惊鸿而过 路有千百个', style='List Bullet')
	document.add_paragraph('遑遑无归 闲云逸鹤 人间红尘过', style='List Bullet')
	document.add_paragraph('引势而流 鸿门乱局 各有各选择', style='List Bullet')
	document.add_paragraph('乾震坎艮 坤巽离兑 定一切生克', style='List Bullet')

	# 添加分页符
	document.add_page_break()
	# 添加图片
	document.add_paragraph('').add_run('添加图片').font.size = Pt(30)
	document.add_picture('少女17087938.jpg', width=Inches(5))

	# 添加分页符
	document.add_page_break()

	document.add_paragraph('').add_run('创建表格').font.size = Pt(30)
	# 创建两行两列的表格
	rows_num = 5
	cols_num = 6
	table = document.add_table(rows=rows_num, cols=cols_num, style = 'Table Grid')

	for r in range(rows_num):
		for c in range(cols_num):
			table.cell(r, c).text = "第{r}行{c}列".format(r = r+1, c = c+1)
	# 保存文档
	document.save('Python生成的文档.docx')

if __name__ == '__main__':
	main()
```

> 将源码保存为单独的python文件后,安装python-docx, 找一张图片,命名为`少女17087938.jpg`, 将图片与python文件放到同一个目录, 然后再python3环境下运行python文件即可!  最后附测试图片一张: 
> ![少女17087938.jpg](https://upload-images.jianshu.io/upload_images/3203841-3524e459cf1d8c7d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 最终效果:![最终效果.png](https://upload-images.jianshu.io/upload_images/3203841-8ad0c3d7dbd2b523.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 自动化修改文档
> ![保留格式并替换](https://upload-images.jianshu.io/upload_images/3203841-6aedf22331b97d1b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 实例: 将当前目录下, 所有docx文件内的"海南大学", 替换为"Hainan University", 并将新文件添加前缀`new`后, 保存到当前目录下

> ![转换前](https://upload-images.jianshu.io/upload_images/3203841-ed1fafb84ee44f61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![转换后](https://upload-images.jianshu.io/upload_images/3203841-36074215431cda50.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![终端打印](https://upload-images.jianshu.io/upload_images/3203841-feb291154b88585d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
import docx
import os
import re
# 传入三个参数, 旧字符串, 新字符串, 文件对象
def replace_text(old_text, new_text, file):
	# 遍历文件对象
	for f in file.paragraphs:
		# 如果 旧字符串 在 某个段落 中
		if old_text in f.text:
			print("替换前:", f.text)
			# 将段落存入 inline
			inline = f.runs
			# 遍历 段落 生成 i
			for i in inline:
				# 如果 旧字符串 在 i 中
				if old_text in i.text:
					# 替换 i.text 内文本资源
					text = i.text.replace(old_text, new_text)
					i.text = text
			print("替换后===>", f.text)

def main():
	# 获取当前目录下所有的文件名列表
	old_file_names = os.listdir()

	# 获取所有docx文件名列表
	docx_file_names = []
	for old_file_name in old_file_names:
		if re.match(r'^[^~].*\.docx', old_file_name):
			print(old_file_name)
			docx_file_names.append(old_file_name)

	for docx_file_name in docx_file_names:
		try:
			# 获取文件对象
			file=docx.Document(docx_file_name)
			# 三个参数: 旧的字符串, 新的字符串, 文件对象
			print("开始替换:", docx_file_name)
			replace_text('海南大学', 'Hainan University', file)
			file.save('new_'+docx_file_name)
			print(docx_file_name, "替换成功")
		except:
			print(docx_file_name, "替换失败")
			pass

if __name__ == '__main__':
	main()
```
