from PIL import Image

class converters:
    def __init__(self,imageinput,convertto,ext,ext1):
        self.imageinput = imageinput
        self.convertto = convertto
        self.ext = ext
        self.ext1 = ext1
    
    def converter(set):
        capimage = Image.open(set.imageinput)
        if set.ext == "png" :
            capimage = capimage.convert('RGB')
        capimage.save("{0}.{1}".format(set.ext1,set.convertto))
        print('File conversion done')


imageinput,convertto= input("Enetr the URL: "),input("Type what image format to convert to: ")
ext,ext1= imageinput.split(".")[-1],imageinput.split(".")[0]
converters(imageinput,convertto,ext,ext1).converter()
