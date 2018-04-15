> ![Kali](https://upload-images.jianshu.io/upload_images/3203841-6a3401d18b624a93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### Kali是一套用于安全渗透(黑客)的Linux发行版, 好处在于, 系统内置了大量的安全渗透方面的软件, 新手可以免于配置, 开箱即用! 
> 即使不打算做安全, 开阔一下眼界也是好的~
 > ![动图: 内置工具](https://upload-images.jianshu.io/upload_images/3203841-cec3e73788f15fa8.gif?imageMogr2/auto-orient/strip)
###### Kali安装的过程中, 给出了太多的选项, 这里详细记录了安装配置的过程

## 第一部分: 获取镜像(kali-linux-2018.1-amd64), 配置虚拟机(VMware 专业版 10.1.0 )
####  获取Kali[镜像](https://images.offensive-security.com/kali-linux-2018.1-amd64.torrent)
> ![Kali镜像](https://upload-images.jianshu.io/upload_images/3203841-7c5f8fcae92e772e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

####  第二部分: 建立虚拟机
###### 从镜像安装
> ![从镜像安装](https://upload-images.jianshu.io/upload_images/3203841-6cb1fcb2d9b3a1ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 选择镜像, 继续
> ![选择镜像](https://upload-images.jianshu.io/upload_images/3203841-c173ad51ff0c0901.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 选择最新 Debian64位
> ![选择Debain64位](https://upload-images.jianshu.io/upload_images/3203841-bde7fc32993ddd25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 选择传统BIOS引导, 继续
> ![传统BIOS引导](https://upload-images.jianshu.io/upload_images/3203841-dd4774a0e701a8e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 自定设置
> ![自定设置](https://upload-images.jianshu.io/upload_images/3203841-071d25436d1c6099.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 选择位置后, 配置内存为4G 和硬盘容量为 64G(物理机资源充足, 为了虚拟机流畅,可以多配置一些物理资源)
> ![硬盘64G](https://upload-images.jianshu.io/upload_images/3203841-d8ac633ddacc842f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![内存4G](https://upload-images.jianshu.io/upload_images/3203841-50ff545aa996aa80.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 第三部分: 开启虚拟机
> ![安装图形化界面](https://upload-images.jianshu.io/upload_images/3203841-16c1764747738cc6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 语言:中文简体
> ![中文简体](https://upload-images.jianshu.io/upload_images/3203841-3d9d459c827c4123.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 地区: 中国
> ![中国](https://upload-images.jianshu.io/upload_images/3203841-e56a0816bad3b0d8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 语言: 汉语
> ![语言选择](https://upload-images.jianshu.io/upload_images/3203841-41a38a36cb50dd54.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 自动安装
> ![自动安装](https://upload-images.jianshu.io/upload_images/3203841-2db9cb4b10f69f1b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 配置网络
> ![网络配置](https://upload-images.jianshu.io/upload_images/3203841-cc789fb5db963550.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###### 配置域名
>![配置域名](https://upload-images.jianshu.io/upload_images/3203841-120199ac3c5dd05a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 填写密码(两次一致)
> ![填写密码](https://upload-images.jianshu.io/upload_images/3203841-f2677f7900e3d8ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

##### 自动校对时钟
> ![校对时钟](https://upload-images.jianshu.io/upload_images/3203841-3a2b09cc2641d4fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 使用整个磁盘
> ![使用整个磁盘](https://upload-images.jianshu.io/upload_images/3203841-a1c919e67aae6e52.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 选择需要分区的磁盘
> ![磁盘分区](https://upload-images.jianshu.io/upload_images/3203841-4c6e0e864c705155.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 选择分区方式
> ![选择分区方式](https://upload-images.jianshu.io/upload_images/3203841-480dea53d8dec417.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 确认分区
> ![确认分区](https://upload-images.jianshu.io/upload_images/3203841-5def650c0d6d5d0b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 真的确认了? 真的!
> ![确认分区](https://upload-images.jianshu.io/upload_images/3203841-04534c5b6932ccec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 安装系统
> ![安装系统](https://upload-images.jianshu.io/upload_images/3203841-5f75716f533f85bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 使用网络镜像吗? 否!
> ![选择否](https://upload-images.jianshu.io/upload_images/3203841-9a3a8b78c5a1e587.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###### 将GRUB安装至硬盘? 是!
> ![是](https://upload-images.jianshu.io/upload_images/3203841-e2163dbb0405676e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 选择启动器安装位置
> ![选择启动器安装位置](https://upload-images.jianshu.io/upload_images/3203841-7692f846cbd17224.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


###### 重启, 完成安装!
> ![重启](https://upload-images.jianshu.io/upload_images/3203841-07578c930467d6e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##  第四部分: 登录系统 
###### 登录root账户
> ![输入用户名](https://upload-images.jianshu.io/upload_images/3203841-885306abad8fe51d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![输入密码](https://upload-images.jianshu.io/upload_images/3203841-fddf872817471ef0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![安装完成](https://upload-images.jianshu.io/upload_images/3203841-7322b7c36b247e77.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 第五部分: Kali的基本配置

###### 安装VMware Tools(物理机和虚拟机可共享粘贴板, 拖拽传输文件)
> ![安装VMware Tools](https://upload-images.jianshu.io/upload_images/3203841-f5edd1376f0e26f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![挂载安装](https://upload-images.jianshu.io/upload_images/3203841-282b5d0db612bc87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![复制tool](https://upload-images.jianshu.io/upload_images/3203841-7ddbeebbe2864aa7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![解包](https://upload-images.jianshu.io/upload_images/3203841-6457285755b7338b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![一路回车](https://upload-images.jianshu.io/upload_images/3203841-c19c06607111fc97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 重启生效

###### 更换镜像源
1. 编辑 `vim /etc/apt/sources.list`
2. 将镜像源写入`sources.list`文件, 
3. `:wq`,退出保存文件
4. 更新镜像源`apt-update`
```
#阿里云
deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
 
#清华大学
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free

#中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
  
#浙大
#deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
#deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
 
#东软大学
#deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
#deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
 
#官方源
#deb http://http.kali.org/kali kali-rolling main non-free contrib
#deb-src http://http.kali.org/kali kali-rolling main non-free contrib
 
#重庆大学
#deb http://http.kali.org/kali kali-rolling main non-free contrib
#deb-src http://http.kali.org/kali kali-rolling main non-free contrib
```
> ![清华, 阿里, 科大 源更新成功](https://upload-images.jianshu.io/upload_images/3203841-cc9eb9e43fe285d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

###### 安装google拼音输入法
```
apt-get install fcitx
apt-get install fcitx-googlepinyin
```
重启系统后生效, 输入法切换, ctrl+space

###### 更改目录为英文, 方便跳转
```
mv 桌面 Desktop
mv 文档 Documents
mv 图片 Pictures
mv 音乐 Music
mv 下载 Downloads
mv 视频 Video
mv 公共 Public
mv 模板 Template
```
> ![before](https://upload-images.jianshu.io/upload_images/3203841-85a79c2b42594aba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ![after](https://upload-images.jianshu.io/upload_images/3203841-e93710566debaa3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)