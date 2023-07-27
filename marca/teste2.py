from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy


tamanho = 660, 1060
img2 = Image.new("RGB", (tamanho), color='#b3b3b3')
marca = Image.open('marca dagua cartelao.png')
marca.putalpha(40)
base = Image.open('mix147_12.png').resize((int(tamanho[0]*0.9), int(tamanho[1]*0.9)), Image.Resampling.LANCZOS)
img2.paste(base, (int(tamanho[0]*0.05), int(tamanho[1]*0.05)), mask=base)
img2.paste(marca, (0, 0), mask=marca)
font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 150)


img2.show()


