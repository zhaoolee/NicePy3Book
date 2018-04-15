今天试用了google的python在线编程工具colab,确实很好用,当时好奇在线环境的主机ip是多少? 在网上查了半小时的方法后, 都不好用,后来灵机一动，不如用爬虫来完成获取外网ip的任务，于是自己写了一个获取主机外网ip的脚本, 可行！



```python
import requests
import re

def get_ip_by_ip138():
    response = requests.get("http://2017.ip138.com/ic.asp")
    ip = re.search(r"\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]",response.content.decode(errors='ignore')).group(0)
    return ip

print("本机的ip地址为:",get_ip_by_ip138())
```

> ![](http://upload-images.jianshu.io/upload_images/3203841-3474512dfe35afbe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> colab 相当于Jupyter notebook的在线版, 如果运行脚本时, 提示缺失requests库, 可以通过`!pip install requests`安装

  


