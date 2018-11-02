import zipfile
import os
import csv
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
#import matplotlib.pyplot as plt
from scipy import ndimage

#Read data from driving_log.csv
lines = []
with open("/opt/data_unzip/data/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    first_row = next(reader)
    for line in reader:
        lines.append(line)

#Read image file and save to a list
#Read steering angle and save to a list
images = []
measurements = []
for line in lines:
    source_path= line[0]
    #print(source_path)
    filename = source_path.split('/')[-1]
    current_path = '/opt/data_unzip/data/IMG/'+filename
    image = ndimage.imread(current_path)
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)

#Augment data by flipping the image and steering angle
augmented_images, augmented_measurements = [], []
for image, measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image, 1))
    augmented_measurements.append(measurement*-1.0)

#Save image files and steering angles as X_train and y_train
X_train= np.array(augmented_images)
y_train = np.array(augmented_measurements)
#print(len(X_train))
#print(len(y_train))

#Build a neural network introduced in the Udacity classroom as "NDIVIA" network
model = Sequential()
#Add a Lambda layer to normalize and center the image data
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3))) 
#Crop out to top and botttom of image to avoid distraction
model.add(Cropping2D(cropping=((70,25),(0,0))))
model.add(Conv2D(24, (5, 5),subsample=(2,2), activation="relu"))
model.add(Conv2D(36, (5, 5),subsample=(2,2), activation="relu"))
model.add(Conv2D(48, (5, 5),subsample=(2,2), activation="relu"))
model.add(Conv2D(64, (3, 3),activation="relu"))
model.add(Conv2D(64, (3, 3),activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
#Use MSE as loss function and Adam as optimizer
model.compile(loss='mse', optimizer='adam')
#Split the data for traning and validation, train for 3 epochs
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=3)
#Save the model as model.h5
model.save('/home/workspace/CarND-Behavioral-Cloning-P3/model.h5')
exit()