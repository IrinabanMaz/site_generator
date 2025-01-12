import os
import shutil

def copy_dir(source = None , target = None):
    if source == None:
        src_directory = os.path.relpath("static")
    else:
        src_directory = source
    if target == None:
        tar_directory = os.path.relpath("public")
    else:
        tar_directory = target

    if os.path.exists(tar_directory):
        shutil.rmtree(tar_directory)

    
    os.mkdir(tar_directory)

    for item in os.listdir(src_directory):
        if os.path.isfile(os.path.join(src_directory ,item)):
            shutil.copy(os.path.join(src_directory , item) ,os.path.join( tar_directory , item))
        else:
            copy_dir(os.path.join(src_directory , item), os.path.join(tar_directory , item))
        
