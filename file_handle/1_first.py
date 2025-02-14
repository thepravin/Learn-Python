
""" 
-> open("filename", mode)

-> modes :
'r'	Read (default mode, file must exist)
'w'	Write (creates a new file or overwrites existing)
'a'	Append (adds data to the end of the file)
'x'	Create (creates a file, but fails if it exists)
'b'	Binary mode (e.g., images, PDFs)
't'	Text mode (default, reads as a string)

 """


f = open('file_handle/data.txt','r')

# print(f.readline())

for line in f:
    print(line)


f.close()

