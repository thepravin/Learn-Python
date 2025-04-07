
""" 
- If the file does not exist, Python creates a new one.
- If the file exists, it will be overwritten.
 """

a = ['pravin\n','ganesh\n','shivam\n'];

with open('file_handle/data2.txt','w') as f:
    f.write('Pravin\n')
    f.writelines(a)