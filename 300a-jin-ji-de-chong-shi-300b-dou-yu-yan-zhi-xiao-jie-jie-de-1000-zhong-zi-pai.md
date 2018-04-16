> 想成为优秀的斗鱼主播，首先得掌握优秀的自拍技能；这次写个有意思的, 爬取斗鱼小姐姐的自拍头像...



## 效果图: 

&gt;!\[001\]\(https://upload-images.jianshu.io/upload\_images/3203841-888ac8e61e229958.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



&gt; !\[002\]\(https://upload-images.jianshu.io/upload\_images/3203841-f3e928e2944555a0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



&gt; !\[003\]\(https://upload-images.jianshu.io/upload\_images/3203841-7e468400d2e34f9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



&gt; !\[004\]\(https://upload-images.jianshu.io/upload\_images/3203841-e8813fcb51a6146f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



&gt; !\[005\]\(https://upload-images.jianshu.io/upload\_images/3203841-8d372f6694b348fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



\#\# 分析频道

&gt; !\[频道API\]\(https://upload-images.jianshu.io/upload\_images/3203841-0068694fb428b2d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



\#\# 获取关键参数

&gt; !\[分析参数\]\(https://upload-images.jianshu.io/upload\_images/3203841-c3b811b3dd7a5016.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)

\# 查看Json

&gt; !\[请求API, 爬虫负责翻页,https://www.douyu.com/gapi/rkc/directory/2\_201/1\]\(https://upload-images.jianshu.io/upload\_images/3203841-5376251edee62a73.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)

\# 脚本运行界面

&gt; !\[脚本运行\]\(https://upload-images.jianshu.io/upload\_images/3203841-b55f5b1ee7e56145.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240\)



\# 源码\(\):

&gt; 4月13日10时更新: 可按照主播人气, 对图片进行排序, 并实现了图片去重

\`\`\`python

import requests

from lxml import etree

import json

import os

import time



def getResponse\(url\):

    headers = {

        \# 设置用户代理头\(为狼披上羊皮\)

        "User-Agent": "Mozilla/5.0 \(Macintosh; Intel Mac OS X 10\_12\_6\) AppleWebKit/537.36 \(KHTML, like Gecko\) Chrome/63.0.3239.132 Safari/537.36",

    }

    response = requests.get\(url, headers = headers\)

    return response



def getAllChannelMark\(response\):

    data\_etree = etree.HTML\(response.content\)

    title\_list = data\_etree.xpath\('//div\[@class="leftnav-cate"\]//li/a'\)

    title\_mark\_list = \[\]

    for title in title\_list:

        title\_name = title.xpath\('@title'\)

        title\_mark = title.xpath\('@data-rk'\)

        if title\_name and title\_mark:

            tmp\_title = {"title\_name": title\_name, "title\_mark": title\_mark}

            title\_mark\_list.append\(tmp\_title\)



    return title\_mark\_list



def getChanneTitleMark\(title\_mark\_list\):

    for index, title\_mark in enumerate\(title\_mark\_list\):

        print\("编号:",index,"=&gt;",title\_mark\["title\_name"\], end=""\)

        if index%4 == 0:

            print\(\)



    checkNumPass = True

    while checkNumPass:

        try:

            channelNum = int\(input\("请输入主题对应的编号\(例如: 33\):"\)\)

            checkNumPass = False

        except:

            print\("输入的编号格式有误"\)



    ChanneTitleMark = title\_mark\_list\[channelNum\]\["title\_mark"\]

    return ChanneTitleMark



def checkNumFormat\(message\):

    canPass = False

    num = 0

    while not canPass:

        try:

            num = int\(input\(message\)\)

            canPass = True

        except:

            print\("输入的格式有误请重新输入!"\)

    return num





def getSourceJson\(ChanneTitleMark\):

    num = checkNumFormat\("请输入需要爬取的主播图片数量\(例如: 200\):"\)

    \# 用于生产url的变量

    url\_index = 0

    \# 设置去重列表

    name\_list = \[\]

    while num &gt; 0:

        JsonUrl = "https://www.douyu.com/gapi/rkc/directory/"+str\(ChanneTitleMark\[0\]\)+"/" + str\(url\_index\)

        SourceJson = getResponse\(JsonUrl\).content

        \# 获取多个主播的信息

        anchors = json.loads\(SourceJson\)\["data"\]\["rl"\]



        \# \# 计算本轮获取的主播数量

        \# anchor\_num = len\(anchors\)

        \# \# 计算出待获取的图片数量

        \# last\_num = num

        \# num = num - anchor\_num

        \# \# 如果本次信息过量,则截取部分json信息

        \# if num &lt;= 0:

        \#     anchors = anchors\[0:last\_num\]

        groupAnchorInfoList = \[\]

        for anchor in anchors:

            tmp\_anchor\_info = {}

            \# 主播照片

            tmp\_anchor\_info\["anchor\_img"\] = anchor\["rs1"\]

            \# 主播名

            tmp\_anchor\_info\["anchor\_name"\] = anchor\["nn"\]

            \# 直播房间id

            tmp\_anchor\_info\["anchor\_rid"\] = anchor\["rid"\]

            \# 主题

            tmp\_anchor\_info\["anchor\_rn"\] = anchor\["rn"\]

            \# 即时热度\(人气\)

            tmp\_anchor\_info\["anchor\_ol"\] = str\(anchor\["ol"\]\)

            \# 将人气补齐到百万级别

            if len\(str\(anchor\["ol"\]\)\) &lt; 7:

                ol\_tmp = "0000000" + str\(anchor\["ol"\]\)

                tmp\_anchor\_info\["anchor\_ol"\] = ol\_tmp\[-7:\]



            \# 频道名

            tmp\_anchor\_info\["channelName"\] = anchor\["c2name"\]



            \# 如果已经存在此主播图片, 则不添加

            if tmp\_anchor\_info\["anchor\_name"\] not in name\_list:



                groupAnchorInfoList.append\(tmp\_anchor\_info\)

                name\_list.append\(tmp\_anchor\_info\["anchor\_name"\]\)



        \# 获取一页, 保存一次

        url\_index += 1



        num = saveImage\(groupAnchorInfoList, num\)



def saveImage\(groupAnchorInfoList, num\):

    \# 延迟0.2秒

    time.sleep\(0.2\)

    for AnchorInfo in groupAnchorInfoList:

        if num &gt; 0:

            \# 建立文件夹

            try:

                os.makedirs\("./images/%s"%\(AnchorInfo\["channelName"\]\)\)

            except Exception as e:

                pass



            \# 写入图片

            file\_path = "./images/%s/%s"%\(AnchorInfo\["channelName"\], AnchorInfo\["anchor\_ol"\]+"\_"+AnchorInfo\["anchor\_name"\]+"\_"+AnchorInfo\["anchor\_rn"\]+".jpg"\)

            file\_data = getResponse\(AnchorInfo\["anchor\_img"\]\).content



            try:

                with open\(file\_path, "wb+"\) as f:



                    f.write\(file\_data\)

                    print\("&gt;",file\_path, "下载成功", "剩余", num, "张"\)

            except Exception as e:

                pass

        num = num - 1

    return num



def main\(\):

    response = getResponse\("https://www.douyu.com/directory/all"\)

    title\_mark\_list = getAllChannelMark\(response\)

    ChanneTitleMark = getChanneTitleMark\(title\_mark\_list\)

    getSourceJson\(ChanneTitleMark\)







if \_\_name\_\_ == '\_\_main\_\_':

    main\(\)

\`\`\`



> 由于分析获取了API, 所以爬虫效率很高, 斗鱼的"颜值"\(第33个\)频道大概有940个主播, 耗时1分钟全部爬完...



