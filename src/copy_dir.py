import os
import shutil

def copy_dir(source = None , target = None):
    if source == None:
        src_directory = "static/"
    else:
        src_directory = source
    if target == None:
        tar_directory = "public/"
    else:
        tar_directory = target

    if os.path.exists(tar_directory):
        shutil.rmtree(tar_directory)

    os.mkdir(tar_directory)

    for item in os.listdir(src_directory):
        if os.path.isfile(src_directory + item):
            shutil.copy(src_directory + item , tar_directory + item)
        else:
            copy_dir(src_directory + item +"/", tar_directory + item + "/")
        
