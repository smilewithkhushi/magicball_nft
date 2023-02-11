from PIL import Image, ImageDraw
def create_img(q,r):
    img = Image.new('RGB', (500, 500), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10,10), q, fill=(0,0,0))
    im2 = Image.open('8-Ball.jpg')
    img.paste(im2, (100, 100))
    d.text((10,450), r, fill=(0,0,0))
    img.save('final.jpg', quality=100)