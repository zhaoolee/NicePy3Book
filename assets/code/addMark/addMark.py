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