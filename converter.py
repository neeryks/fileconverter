from PIL import Image

gv = Image.open("001.png")
br = gv.convert('RGB')
br.save('io.jpg')