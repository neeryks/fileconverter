
from tkinter.filedialog import askopenfilename
from converter import converters as co

def chooser():
    input("Press Any key to select the file for conversion")
    fileinput = askopenfilename()   
    ext,ext1= fileinput.split(".")[-1].lower(),fileinput.split(".")[0]
    if ext == "pdf":
        convertto = "jpeg"
        co(fileinput,convertto,ext,ext1).pdfconverter()
    elif any(ext in listvar for listvar in ['jpg','jpeg','webp','heic','heif','png']) == True:
        convertto = input("Enter Conversion Format: ").lower()
        co(fileinput,convertto,ext,ext1).imgconverter()
chooser()

choose = input("Would You like to do another conversion Y/N :")
if choose == 'Y' or choose == 'y':
    chooser()
elif choose == 'N' or choose == 'n':
    print("Thankyou for using \n\n")
    input("Waiting For Input")
    chooser()


    

