from tkinter import filedialog
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyheif
import pdf2image as p2i
import zipfile
class converters:
    def __init__(self,fileinput,convertto,ext,ext1):
        self.fileinput = fileinput
        self.convertto = convertto
        self.ext = ext
        self.ext1 = ext1
        print('Starting Conversion... {0} ---> {1}'.format(self.ext.upper(),self.convertto.upper()))
    
    def imgconverter(set):
        imglist = ['jpg','jpeg','webp']
        heiccodec = ['heic','heif']
        if any(set.ext in extension for extension in imglist) == True :
            capimage = Image.open(set.fileinput)
        elif any(set.ext in extension for extension in heiccodec) == True:
            heif_file = pyheif.read(set.fileinput)
            capimage  = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data,"raw",heif_file.mode,heif_file.stride)
        elif set.ext == "png":
            capimage = Image.open(set.fileinput)
            capimage = capimage.convert('RGB')
        elif set.ext == "pdf":
            capimage = p2i.convert_from_path(set.fileinput,fmt="jpeg",output_folder='media')
            capimage
            print('Converted PDF ---> ZIP')
            return
            
        else :
            print("File type not supported.")
            return
        capimage.save("{0}.{1}".format(set.ext1,set.convertto))
        print('Converted {0} ---> {1}'.format(set.ext.upper(),set.convertto.upper()))
        

if __name__ == '__main__':
    fileinput,convertto= askopenfilename(),input("Enter Conversion Format: ")
    ext,ext1= fileinput.split(".")[-1].lower(),fileinput.split(".")[0]
    converters(fileinput,convertto,ext,ext1).imgconverter()
