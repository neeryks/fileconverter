from tkinter import filedialog
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyheif

class converters:
    def __init__(self,fileinput,convertto,ext,ext1):
        self.fileinput = fileinput
        self.convertto = convertto
        self.ext = ext
        self.ext1 = ext1
    
    def imgconverter(set):
        print('Starting Conversion... {0} ---> {1}'.format(set.ext.upper(),set.convertto.upper()))
        imglist = ['jpg','jpeg','png','webp','pdf']
        heiccodec = ['heic','heif']
        if any(set.ext in extension for extension in imglist) == True :
            capimage = Image.open(set.fileinput)
            if set.ext == "png" :
                capimage = capimage.convert('RGB')
        elif any(set.ext in extension for extension in heiccodec) == True:
            heif_file = pyheif.read(set.fileinput)
            capimage  = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data,"raw",heif_file.mode,heif_file.stride,)
        else :
            print("File type not supported.")
            return
        capimage.save("{0}.{1}".format(set.ext1,set.convertto))
        print('Converted {0} ---> {1}'.format(set.ext.upper(),set.convertto.upper()))
     

if __name__ == '__main__':
    fileinput,convertto= askopenfilename(),input("Enter Conversion Format: ")
    ext,ext1= fileinput.split(".")[-1].lower(),fileinput.split(".")[0]
    converters(fileinput,convertto,ext,ext1).imgconverter()
