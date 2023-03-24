import os
import shutil

fromdir="C:/Users/Ivonne/Downloads"
todir="C:/Users/Ivonne/Archivos_Documentos"

list_of_files=os.listdir(fromdir)
print(list_of_files)

for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    if extension=="":
        continue
    
    if extension in ['.txt','.doc','.docx','.pdf']:
        path_1=fromdir+'/'+filename
        path_2=todir+'/'+'ArchivosDocumentos'
        path_3=todir+'/'+'ArchivosDocumentos'+'/'+filename
        print("path_1: ",path_1)
        print("path_3: ",path_3)
        if os.path.exists(path_2):
            print("Moviendo "+filename+'......')
            shutil.move(path_1,path_3)
        else:
            os.makedirs(path_2)
            print("Moviendo "+filename+'......')
            shutil.move(path_1,path_3)