import os 
import shutil

from_dir = "C:/Users/hp/Downloads"
to_dir = "C:/Users/hp/Desktop/war/gun"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
              
    if extension == '':
       continue
    if extension in['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
      path1 = "C:/Users/hp/Downloads/pistol.jpg"
      path2 = "C:/Users/hp/Desktop/war/gun"
      path3 = "C:/Users/hp/Desktop/war/gun/pistol.jpg"
      print("path1", path1)
      print("path3", path3)