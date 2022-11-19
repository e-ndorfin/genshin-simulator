from PIL import Image 

im = Image.open(r"/Users/zacharytang/desktop/coding/webDev/genshin_scam/img/cursor.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
im = im.resize((40,40), Image.LANCZOS)
# Shows the image in image viewer
im.show()
im.save('/Users/zacharytang/desktop/coding/webDev/genshin_scam/img/cursor_resized.png', "PNG")