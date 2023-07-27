from PIL import Image, ImageDraw, ImageFont

caption = 'I need to update my Pillow'
tamanho = 1894, 3000
img = Image.new("RGB", (tamanho[0], tamanho[1]), color='#b3b3b3')
d = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 150)
d.text((tamanho[0]/2, tamanho[1]/2),"DC001",fill='black' ,anchor="mm",font=font, stroke_width=5, stroke_fill='white')
img.show()