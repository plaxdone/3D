from PIL import Image

pxl = 11.810833333333333333333333333333
tam = 44,32
im = Image.new(mode="RGBA", size=(int(tam[0]*pxl),int(tam[1]*pxl)), color = (0,0,0,0))
im.show()
print(int(tam[0]*pxl),int(tam[1]*pxl))