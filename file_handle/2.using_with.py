
""" 
- The with statement automatically closes the file after use.
 """


with open('file_handle/data.txt') as f:
    # for line in f:
    #     print(line)


    print(f.read(10))
    f.seek(5)
    print(f.read(8))