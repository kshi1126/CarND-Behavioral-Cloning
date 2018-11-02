import zipfile
import os

#Create the folder for un-zipped data
if not os.path.exists("/opt/data_unzip"):
    os.makedirs("/opt/data_unzip")
    
#Copy data.zip into /opt directory and un-zip
from shutil import copyfile
src = "/home/workspace/CarND-Behavioral-Cloning-P3/data.zip"
dst = "/opt/data.zip"

copyfile(src, dst)
zip_ref = zipfile.ZipFile(src, 'r')
zip_ref.extractall("/opt/data_unzip")
zip_ref.close()