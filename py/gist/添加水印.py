##################### 添加文字水印 #####################
from PIL import Image, ImageDraw, ImageFont
img = Image.open('aa.jpg').convert('RGBA')
txt = Image.new('RGBA', img.size, (0, 0, 0, 0))
fnt = ImageFont.truetype('c:/Windows/fonts/Tahoma.ttf', 20)
draw = ImageDraw.Draw(txt)
draw.text((txt.size[0]-80, txt.size[1]-30), 'Logo', font=fnt, fill=(255, 255, 255, 255))
out = Image.alpha_composite(img, txt)
# out.show()
out.convert('RGB').save('b.jpg')

##################### 添加图片水印 #####################
from PIL import Image
img = Image.open('aa.jpg')
mark = Image.open('favicon.ico')
layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
layer.paste(mark, (img.size[0]-150, img.size[1]-60))
out = Image.composite(layer, img, layer)
# out.show()
out.save('b.jpg')