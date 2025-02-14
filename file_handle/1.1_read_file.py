
#*--------- Read whole file -----------
""" file = open("file_handle/data.txt","r")
content = file.read()
print(content)
file.close() """

#* ------------ Read Line-by-line ------------
file = open("file_handle/data.txt","r")
content = file.readline() # Reads first line
print(content)
file.close()

#*-------------- Read all Lines -------------
file = open("file_handle/data.txt","r")
lines = file.readlines()  # Reads all lines into a list
print(lines)
file.close()
