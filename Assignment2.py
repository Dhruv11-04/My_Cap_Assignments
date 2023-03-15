
r= input("Enter the file name : ")

a,b= r.split(".")



if "py" in b:
    print("The extension of the file is : 'Python'")
elif "docx" in b:
    print("The extension of the file is : 'Word Document'")
elif "txt" in b:
    print("The extension of the file is : 'Text Document File'")

elif "mp3" in b:
    print("The extension of the file is : 'MPEG Audio Layer 3'")

elif "xlsx" in b:
    print("The extension of the file is : 'Microsoft Excel Open XML Spreadsheet'")
else :
    print("The file format is not uploaded!!")