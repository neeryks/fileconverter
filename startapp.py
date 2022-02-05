
from tkinter.filedialog import askopenfilename
from converter import converters as co

i = 0
while i < 1:
    input("Press Any key to select the file for conversion")
    fileinput = askopenfilename()   
    ext,ext1= fileinput.split(".")[-1].lower(),fileinput.split(".")[0]
    if ext == "pdf":
        convertto = "jpeg"
        co(fileinput,convertto,ext,ext1).pdfconverter()
    elif any(ext in listvar for listvar in ['jpg','jpeg','webp','heic','heif']) == True:
        convertto = input("Enter Conversion Format: ").lower()
        co(fileinput,convertto,ext,ext1).imgconverter()



    

