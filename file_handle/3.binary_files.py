""" 
- Binary mode is used for images, audio, PDFs, etc.

 """

with open("file_handle/image.jpg","rb") as file:
    content = file.read()
    print(content[:10])