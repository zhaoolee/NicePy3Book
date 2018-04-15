>首先,图虫网是一个很棒的图片网站,这里的爬虫只是为了研究技术,请读者朋友们,不要大量采集网站信息,爬取的图片,请取得版权后再使用...

![图虫网](http://upload-images.jianshu.io/upload_images/3203841-6619cb5066ffac8f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 根据”分类名称”,获取json数据

> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-63c0cba83e59d5b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-74009bc99abf6431.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-a377d44c9dcb4f2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


# 根据json数据,获取图集url与title



> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-a43474b2eec96eed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-da9eed9a167df0f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-78c60d5b8d01ef8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-a4a9c0dc4da2f081.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![image.png](http://upload-images.jianshu.io/upload_images/3203841-5dd8b80baa839cc5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




#爬虫架构:

![爬虫多线程实现](http://upload-images.jianshu.io/upload_images/3203841-67ce1326d49aec9f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 运行界面:

![运行](http://upload-images.jianshu.io/upload_images/3203841-0d78e7d5861e3184.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 最终效果

![效果](http://upload-images.jianshu.io/upload_images/3203841-ac309d262c304519.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

会在同级目录下生成一个images的文件夹,里面有按照原主题命名的图片...

![图片目录](http://upload-images.jianshu.io/upload_images/3203841-a124e3fdad7a9f6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

最后放出源码(仅限交流,请不要用来大量采集网站信息):
```
import requests
import json
import re
import time
import os
from multiprocessing import Process, Queue
import time
from time import sleep
import threading
import sys

class TuChong(object):
	def __init__(self):

		self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
		self.target_image_num = 0
		self.title_name = None
		self.q_json = Queue()
		self.q_album = Queue()
		self.q_image = Queue()

		pass

	# 负责获取响应
	def get_response_content(self, url):
		try:
			response = requests.get(url, headers = self.headers)
			return response.content
		except:
			pass

	def get_json_data(self):

		title =["风光","人像","城市","旅行","纪实","街拍","人文","美女","建筑","静物","夜景","自然","少女","儿童","秋天","光影","花卉","私房","色彩","抓拍","黑白","小清新","情绪","日系","后期","写真","微距","创意","情感","复古","手机","佳能","尼康","胶片","索尼","50mm","35mm","广角","富士","iphone","宾得","85mm","北京","上海","广州",
"深圳","南京","成都","武汉","厦门","杭州","重庆","西藏","西安","四川","大连","新疆","长沙","苏州","日本","中国","浙江","川西","香港","云南","青岛"]

		for i in range(len(title)):
			if i%5 == 0:
				print()
			print("{""代号", i,"-->",title[i],"}",end="")

		print("")
		print("=="*10)		

		title_code =  int(input("请输入代号:"))
		self.title_name = title[title_code]
		self.target_image_num = int(input("请输入图片数量:"))
		print("开始下载-->%s主题"%(self.title_name))
		# 获取json数据
		for m in range(1, 3):
			tc_get_json = "https://tuchong.com/rest/tags/%s/posts?page=%s&count=20"%(self.title_name,m)
			# print("->", tc_get_json)
			tc_json = self.get_response_content(tc_get_json)
			self.q_json.put(tc_json)


	def get_album_url(self):
		while True:
			try:
				str_data = self.q_json.get().decode()
				# print("--->json分界限<---")
				# print("-->", str_data)
			except Exception as e:
				# print("-->获取json数据失败",e)
				sleep(0.1)
				continue

			page_list_jsons = json.loads(str_data)["postList"]

			for page_list_json in page_list_jsons:

				temp = {}
				# 获取图集主题
				try:
					temp["title"] = page_list_json["title"]
					# print("-->获得图集名称-->",temp["title"])
					# 获取图集url
					temp["url"] = page_list_json["url"]
				except Exception as e:
					# print("获取图集信息出错",e)
					pass
				# 过滤帖子类型的图集
				if re.match(r"https://tuchong.com/(\d)*?/(\d)*?/", temp["url"]):
					# 将url与标题,信息加入队列
					self.q_album.put(temp)
					# 记录图集的url
					with open("./目录.json", "a") as f:
						str_data = json.dumps(temp, ensure_ascii=False) + ',\n'
						f.write(str_data)


	# 根据图集获取单张图片url地址
	def get_image_url(self):

		while True:
			sleep(0.1)

			# 获取图集url和标题
			try:
				album = self.q_album.get()
			except Exception as e:
				print("正在获取图集首页...")
				continue
			album_url = album["url"]
			album_title = album["title"]
			# 获取图集首页响应内容
			response_content = self.get_response_content(album_url)
			# 获取图集图片集合信息
			image_info_list = re.findall(r'\"img_id\"\:\d+\,\"user_id\"\:\d+', response_content.decode())

			for image_info in image_info_list:
				img_id = image_info.split(",")[0].split(":")[1]
				user_id = image_info.split(",")[1].split(":")[1]
				image_url = "https://photo.tuchong.com/%s/f/%s.jpg"%(user_id, img_id)
				# 将图片url信息和所在的图集标题加入队列
				temp = dict()
				temp["image_url"] = image_url
				temp["album_title"] = album_title

				self.q_image.put(temp)
				# print("-->put",temp)


	def save_image(self):
		while True:
			
			sleep(0.1)

			try:
				# 获取图片信息
				image_temp = self.q_image.get()
			except Exception as e:
				# print("准备下载图片")
				continue
			image_url = image_temp["image_url"]
			album_title = image_temp["album_title"]
			old_name = re.match(r".*?f\/(.*)",image_url).group(1)
			# print("旧的名字为", old_name)
			new_image_name = album_title +"_"+old_name
			# print(new_image_name)

			# 建立文件夹
			try:
				os.makedirs("./images/%s"%(self.title_name))
			except Exception as e:
				pass

			# 写入图片
			file_path = "./images/%s/%s"%(self.title_name, new_image_name)

			
			if self.target_image_num <= 0:
				print("下载完毕")
				# os._exit()
				sys.exit()
			try:
				print("正在下载第%d张图片.."%(self.target_image_num))
				self.target_image_num -= 1
				print("-->", file_path, image_url)
				image_data = self.get_response_content(image_url)
				with open(file_path, "wb+") as f:

					f.write(image_data)

			except:

				# print("网络故障,图片下载变慢")
				pass

def main():
	tuchong = TuChong()
	tuchong.get_json_data()

	t1 = threading.Thread(target=tuchong.get_album_url)
	t1.start()

	t2 = threading.Thread(target=tuchong.get_image_url)
	t2.start()

	try:

		t3 = threading.Thread(target=tuchong.save_image)
		t3.start()

		t4 = threading.Thread(target=tuchong.save_image)
		t4.start()

	except:
		print("主程序退出")
		sys.exit()

if __name__ == '__main__':
	main()
```
