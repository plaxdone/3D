from PIL import Image
from PIL.ExifTags import TAGS



from PIL import Image
from resize import resize

def abrirImg(item, tamImg):
    pxl = 11.810833333333333333333333333333
    img = Image.open(item)
    if img.size[1]>img.size[0]:
        prop = img.size[0]/img.size[1]
    else:
        prop = img.size[1]/img.size[0]
    if prop > 0.9:
        img = resize(img, (int((tamImg-2)*pxl)))
    else:
        img = resize(img, (int((tamImg)*pxl)))
    return img

img = 'C:\\Users\\Jorge\\Desktop\\Casadinhas\\CS-19 - Girassol\\19009 (2).png'
img2 = abrirImg(img, 10)
img2.save('imgteste.png')

'''
# read the image data using PIL
image = Image.open('imgteste.png')

# extract EXIF data
exifdata = image.getexif()


for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
    '''