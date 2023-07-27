from PIL import Image, ImageDraw, ImageFont

im = Image.open('marca.png')
text = "I am hero"

tim = Image.new('RGBA', (500,200), (0,0,0,0))
dr = ImageDraw.Draw(tim)
ft = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 50)
dr.text((0, 0), text, font=ft, fill='black', stroke_width=5, stroke_fill='white')
# dr.text((0,0),'texto',fill='black',anchor="mm",font=font, stroke_width=5, stroke_fill='white')
tim = tim.rotate(90,  expand=1)

im.paste(tim, (0,0), tim)
im.show()