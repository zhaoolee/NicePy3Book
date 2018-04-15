#### 上网除了需要IP, 还需要Mac地址, Mac与网卡绑定, 记录了设备的Mac, 相当于标记了设备使用者

> 关于Mac和IP的关系: [<讲个故事>为什么IP地址与Mac地址缺一不可?](https://www.jianshu.com/p/0ce15c07b294)

> ![星巴克无线网](https://upload-images.jianshu.io/upload_images/3203841-08d59922b545e41c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 初级玩法: 哪个时段顾客人数最多?
> 今天放假，人格外多，想统计一下有多少台设备在上网(有多少IP被占用)
> 原理: 批量发送ping, 按照协议, 对方会对我们的ping,产生应答，然后记录应答的ip
```
from scapy.all import *
for i in range(100):
	# 生成目标IP
	ip = "192.168.31."+str(i)
	# 打印生成的目标IP
	print("=目标ip为=>", ip)
	# 根据目标IP组包, ICMP可以看做Ping
	p = IP(dst=ip)/ICMP()
	# 将数据包发出, 等待0.5秒,无回应则放弃等待
	r = sr1(p, timeout=0.5)
```
> ![神器wireshark查看结果](https://upload-images.jianshu.io/upload_images/3203841-cc1b319c282052dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
ip.dst == 192.168.31.19 and (ip.src >= 192.168.31.1  and 192.168.31.255 >= ip.src)
```
> 关于wireshark的使用: ["杀手级"抓包软件wireshark入门](https://www.jianshu.com/p/28035d90c3c8)

## 进阶玩法: 今天来了几名新顾客? (信息自动化编程实现局域网扫描)
- 功能1: 针对不同网段扫描
> 我的计算机内存在两个虚拟路由器(同时安装了Parallels, Vmware, 两个网段), 同时我连接了公共场所的无线网(一个网段), 编程实现自动识别三个网段, 可选择性的扫描
> ![选择网段](https://upload-images.jianshu.io/upload_images/3203841-f2aa4fbc4fe93114.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 功能2: 记录在线设备的mac地址 
> 初级的玩法是记录ip(网络层), 既然是高级玩法, 我们把Mac地址(数据链路层)也记录下来
> ![记录Mac地址](https://upload-images.jianshu.io/upload_images/3203841-ebaf977b199d1fa5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


- 功能3: 将mac地址转换为网卡厂商
> wireshark实现了这个功能, 这个功能的实现原理就是查字典, 我直接从github找了一个专门翻译mac地址的库[仓库](https://github.com/hustcc/mac.py)
> ![value](https://upload-images.jianshu.io/upload_images/3203841-37d1e21c05461ae8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 功能4: 保存结果:
> 程序会以完成的时间作为文件名,将分析结果保存到同级目录下
> ![保存的结果](https://upload-images.jianshu.io/upload_images/3203841-7df9a7619250e712.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 功能5: 开启多线程?
> 这个程序默认设置的是0.2秒的等待, 如果收不到回应, 就转到下一个IP, 如果开启了多线程, 平均时间会更短, 但出于不作恶的原则, 这里就不放了
--- 
> ![运行界面](https://upload-images.jianshu.io/upload_images/3203841-9c99a18d4d03aa3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


```python
import os
import re
from scapy.all import *
from scapy.layers import l2
import json
import time
from macpy import Mac
# A类地址：10.0.0.0--10.255.255.255
# B类地址：172.16.0.0--172.31.255.255 
# C类地址：192.168.0.0--192.168.255.255

def get_all_ip_range():
	result = []
	ip_des_list = os.popen("ifconfig | grep inet").readlines()
	for ip_des in ip_des_list:
		try:
			if re.match(r'\tinet[^6]([0-9]{1,3}).*', ip_des).group(1) in ["192", "172", "10"]:
				ip_des = re.match(r'\tinet[^6]([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*', ip_des).group(1)
				ip_range = re.match(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.', ip_des).group()
				result.append(ip_range)
		except:
			pass
	return result


def getIPAndMac(ip_range):
	result_list = {}
	for ip in ip_range:
		# 打印生成的目标IP
		print("=检测ip=>", ip)
		# 根据目标IP组包, ICMP可以看做Ping, 程序员式招呼
		p = IP(dst=ip)/ICMP()/b'HelloWorld'
		# 将数据包发出, 等待0.3秒,无回应则放弃等待, 屏蔽提示消息
		r = sr1(p, timeout=0.3, verbose = False)
		# 如果收到了返回的数据包,则存到一个数组中
		try:
			if r.getlayer(IP).fields['src'] == ip and r.getlayer(ICMP).fields['type'] == 0:
				net_info = {}
				mac = l2.getmacbyip(ip)
				getcom = Mac()
				com = getcom.search(mac)
				mac = mac+ "|" + str(com)
				result_list[str(ip)] = mac
				print("成功获取一个mac地址:", ip, mac)
		except Exception as e:
			pass
	return result_list


def select_ip_range(all_ip_range):
	choose_ip_dic = {}
	for index, ip_range in enumerate(all_ip_range):
		all_ip = []
		for num in range(256):
			all_ip.append(ip_range+str(num))

		choose_ip_dic[index] = all_ip

	index_list = []
	for index, ip_range in enumerate(all_ip_range):
		index_list.append(index)
		print("序列号:", index, "ip范围", ip_range+"0"+"-"+ip_range+"255")
	print(index_list)
	while 1:
		user_choose = input("请输入您需要扫描的ip范围序号:")
		try:
			user_choose = int(user_choose)
		except:
			print("请您输入数字!!!")
			pass
		if user_choose in index_list:
			user_ip_list = choose_ip_dic[int(user_choose)]
			break
		else:
			print("您的输入有误, 请查正后输入!!!")
	return user_ip_list

def genderTxt(result_dic):
	file_name = time.strftime("%Y%m%d%H%M%S")+"IPAndMac.txt"
	print(file_name)
	for key in result_dic:
		with open(file_name, "a") as f:
			f.write("设备的IP:"+key+" Mac地址"+result_dic[key]+"\n")

	result_json = json.dumps(result_dic, ensure_ascii=False)

def main():
	all_ip_range = get_all_ip_range()
	ip_range = select_ip_range(all_ip_range)
	print(ip_range)
	result_dic = getIPAndMac(ip_range)
	# result_dic = {"k1": "001", "k123": "msdf", "k213": "00213"}
	genderTxt(result_dic)

if __name__ == '__main__':
	main()
```
> 处理scapy的各种依赖确实恶心, 如果没有经验, 从零开始处理种种依赖包起码半小时,可以直接用Kali, Kali是内置scapy的, 能省掉处理依赖包的时间


> scapy是小众工具,Wireshark是网络流量分析神器,二者配合, 让计算机网络的研究变容易

> 以前的Wireshark的Mac版时经常崩溃, 这次下载了最新版的Wireshark, 用了2天, 没有遇到崩溃的状况, 有兴趣的, 可以试一下

>文章涉及到的资源我会通过百度网盘分享，为便于管理,资源整合到一张独立的帖子，链接如下:
http://www.jianshu.com/p/4f28e1ae08b1





