> 想成为优秀的斗鱼主播，首先得掌握优秀的自拍技能；这次写个有意思的, 爬取斗鱼小姐姐的自拍头像...

## 效果图: 
> ![001](https://upload-images.jianshu.io/upload_images/3203841-888ac8e61e229958.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![002](https://upload-images.jianshu.io/upload_images/3203841-f3e928e2944555a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![003](https://upload-images.jianshu.io/upload_images/3203841-7e468400d2e34f9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![004](https://upload-images.jianshu.io/upload_images/3203841-e8813fcb51a6146f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> ![005](https://upload-images.jianshu.io/upload_images/3203841-8d372f6694b348fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 分析频道
> ![频道API](https://upload-images.jianshu.io/upload_images/3203841-0068694fb428b2d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 获取关键参数
> ![分析参数](https://upload-images.jianshu.io/upload_images/3203841-c3b811b3dd7a5016.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 查看Json
> ![请求API, 爬虫负责翻页,https://www.douyu.com/gapi/rkc/directory/2_201/1](https://upload-images.jianshu.io/upload_images/3203841-5376251edee62a73.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 脚本运行界面
> ![脚本运行](https://upload-images.jianshu.io/upload_images/3203841-b55f5b1ee7e56145.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 源码:

> 4月13日10时更新: 可按照主播人气, 对图片进行排序, 并实现了图片去重

```python
import requests
from lxml import etree
import json
import os
import time

def getResponse(url):
    headers = {
        # 设置用户代理头(为狼披上羊皮)
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    response = requests.get(url, headers = headers)
    return response

def getAllChannelMark(response):
    data_etree = etree.HTML(response.content)
    title_list = data_etree.xpath('//div[@class="leftnav-cate"]//li/a')
    title_mark_list = []
    for title in title_list:
        title_name = title.xpath('@title')
        title_mark = title.xpath('@data-rk')
        if title_name and title_mark:
            tmp_title = {"title_name": title_name, "title_mark": title_mark}
            title_mark_list.append(tmp_title)

    return title_mark_list

def getChanneTitleMark(title_mark_list):
    for index, title_mark in enumerate(title_mark_list):
        print("编号:",index,"=>",title_mark["title_name"], end="")
        if index%4 == 0:
            print()

    checkNumPass = True
    while checkNumPass:
        try:
            channelNum = int(input("请输入主题对应的编号(例如: 33):"))
            checkNumPass = False
        except:
            print("输入的编号格式有误")

    ChanneTitleMark = title_mark_list[channelNum]["title_mark"]
    return ChanneTitleMark

def checkNumFormat(message):
    canPass = False
    num = 0
    while not canPass:
        try:
            num = int(input(message))
            canPass = True
        except:
            print("输入的格式有误请重新输入!")
    return num


def getSourceJson(ChanneTitleMark):
    num = checkNumFormat("请输入需要爬取的主播图片数量(例如: 200):")
    # 用于生产url的变量
    url_index = 0
    # 设置去重列表
    name_list = []
    while num > 0:
        JsonUrl = "https://www.douyu.com/gapi/rkc/directory/"+str(ChanneTitleMark[0])+"/" + str(url_index)
        SourceJson = getResponse(JsonUrl).content
        # 获取多个主播的信息
        anchors = json.loads(SourceJson)["data"]["rl"]

        # # 计算本轮获取的主播数量
        # anchor_num = len(anchors)
        # # 计算出待获取的图片数量
        # last_num = num
        # num = num - anchor_num
        # # 如果本次信息过量,则截取部分json信息
        # if num <= 0:
        #     anchors = anchors[0:last_num]
        groupAnchorInfoList = []
        for anchor in anchors:
            tmp_anchor_info = {}
            # 主播照片
            tmp_anchor_info["anchor_img"] = anchor["rs1"]
            # 主播名
            tmp_anchor_info["anchor_name"] = anchor["nn"]
            # 直播房间id
            tmp_anchor_info["anchor_rid"] = anchor["rid"]
            # 主题
            tmp_anchor_info["anchor_rn"] = anchor["rn"]
            # 即时热度(人气)
            tmp_anchor_info["anchor_ol"] = str(anchor["ol"])
            # 将人气补齐到百万级别
            if len(str(anchor["ol"])) < 7:
                ol_tmp = "0000000" + str(anchor["ol"])
                tmp_anchor_info["anchor_ol"] = ol_tmp[-7:]

            # 频道名
            tmp_anchor_info["channelName"] = anchor["c2name"]

            # 如果已经存在此主播图片, 则不添加
            if tmp_anchor_info["anchor_name"] not in name_list:

                groupAnchorInfoList.append(tmp_anchor_info)
                name_list.append(tmp_anchor_info["anchor_name"])

        # 获取一页, 保存一次
        url_index += 1

        num = saveImage(groupAnchorInfoList, num)

def saveImage(groupAnchorInfoList, num):
    # 延迟0.2秒
    time.sleep(0.2)
    for AnchorInfo in groupAnchorInfoList:
        if num > 0:
            # 建立文件夹
            try:
                os.makedirs("./images/%s"%(AnchorInfo["channelName"]))
            except Exception as e:
                pass

            # 写入图片
            file_path = "./images/%s/%s"%(AnchorInfo["channelName"], AnchorInfo["anchor_ol"]+"_"+AnchorInfo["anchor_name"]+"_"+AnchorInfo["anchor_rn"]+".jpg")
            file_data = getResponse(AnchorInfo["anchor_img"]).content

            try:
                with open(file_path, "wb+") as f:

                    f.write(file_data)
                    print(">",file_path, "下载成功", "剩余", num, "张")
            except Exception as e:
                pass
        num = num - 1
    return num

def main():
    response = getResponse("https://www.douyu.com/directory/all")
    title_mark_list = getAllChannelMark(response)
    ChanneTitleMark = getChanneTitleMark(title_mark_list)
    getSourceJson(ChanneTitleMark)



if __name__ == '__main__':
    main()
```

> 由于分析获取了API, 所以爬虫效率很高, 斗鱼的"颜值"(第33个)频道大概有940个主播, 耗时1分钟全部爬完...