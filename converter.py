from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
class converters:
    def __init__(self,fileinput,convertto,ext,ext1):
        self.fileinput = fileinput
        self.convertto = convertto
        self.ext = ext
        self.ext1 = ext1
    
    def imgconverter(set):
        capimage = Image.open(set.fileinput)
        if set.ext == "png" :
            capimage = capimage.convert('RGB')
        capimage.save("{0}.{1}".format(set.ext1,set.convertto))
        print('File conversion done')

if __name__ == '__main__':
    fileinput,convertto= askopenfilename(),input("Enter Conversion Format: ")
    ext,ext1= fileinput.split(".")[-1],fileinput.split(".")[0]
    converters(fileinput,convertto,ext,ext1).imgconverter()
