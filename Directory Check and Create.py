import os
directory_check = (os.path.isdir('C:/Users/Jon/Desktop/PythonProject'))
if (directory_check == True):
    os.chdir('C:/Users/Jon/Desktop/PythonProject')
    file_name = open((input("New File Name:", )),"w+")
    file_name.write(input())
    file_name.close()
    
else:
    os.mkdir('C:/Users/Jon/Desktop/PythonProject')
        
