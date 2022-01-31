import os
from platform import python_build
import shutil

m=os.listdir("C:/Users/USER/OneDrive/Desktop/Python/Backup C99/mh")
print(m)

for h in m :
    n=os.path.splitext(h)
    print(n[1])
    if n[1]==".py":
        print("python")
        shutil.move("C:/Users/USER/OneDrive/Desktop/Python/Backup C99/mh/"+h,"C:/Users/USER/OneDrive/Desktop/Python/Backup C99/python")
    elif n[1]==".txt":
        print("txt")
        shutil.move("C:/Users/USER/OneDrive/Desktop/Python/Backup C99/mh/"+h,"C:/Users/USER/OneDrive/Desktop/Python/Backup C99/text")
    else :
        print("folder")
        shutil.move("C:/Users/USER/OneDrive/Desktop/Python/Backup C99/mh/"+h,"C:/Users/USER/OneDrive/Desktop/Python/Backup C99/folders")

    
