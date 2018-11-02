#Import sample data provided in the Udacity classroom
#Data is saved on google drive. Because without GPU on I do not see data.zip under /opt
#Running this file will download data.zip into workspace.

#!/bin/bash
fileid="15WpYVRutUPpd2E-QwMDG2kgWtYCSi2rI"
filename="data.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
