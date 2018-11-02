# **Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 5x5 filter sizes and depths between 32 and 128 (model.py lines 18-24) 
I used the NVIDIA model introduced in the classroom.
The architecture is below:
1. Normalization layer using Keras Lambda layer (code line 52)
2. Convolution layer: depth of 24, Filter size 5x5. Activation method of Relu.
3. Convolution layer: depth of 36, Filter size 5x5. Activation method of Relu.
4. Convolution layer: depth of 48, Filter size 5x5. Activation method of Relu.
5. Convolution layer: depth of 64, Filter size 3x3. Activation method of Relu.
6. Convolution layer: depth of 64, Filter size 3x3. Activation method of Relu.
7. Flatten
8. Fully connected layer: dense to 100
9. Fully connected layer: dense to 50
10. Fully connected layer: dense to 10
11. Fully connected layer: dense to 1 

#### 2. Attempts to reduce overfitting in the model

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 68). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 66).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, and the flipped version of center lane driving. 

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

I usde a convolution neural network model introduced in the Udacity classroom as "NVIDIA" network. I thought this model might be appropriate because it was developed by NVIDIA autonomous driving team and it is more powerful than LeNet.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. 

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 50-64) consisted of a convolution neural network with the following layers and layer sizes:
1. Normalization layer using Keras Lambda layer (code line 52)
2. Convolution layer: depth of 24, Filter size 5x5. Activation method of Relu.
3. Convolution layer: depth of 36, Filter size 5x5. Activation method of Relu.
4. Convolution layer: depth of 48, Filter size 5x5. Activation method of Relu.
5. Convolution layer: depth of 64, Filter size 3x3. Activation method of Relu.
6. Convolution layer: depth of 64, Filter size 3x3. Activation method of Relu.
7. Flatten
8. Fully connected layer: dense to 100
9. Fully connected layer: dense to 50
10. Fully connected layer: dense to 10
11. Fully connected layer: dense to 1 

#### 3. Creation of the Training Set & Training Process

I used the driving data provided in Udacity classroom because I found it was very difficult to control the vehicle and make it drive smoothly for good data.

I preprocessed this data by normalization and centralization.

I then randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 3 as evidenced by the validation lossed. I used an adam optimizer so that manually training the learning rate wasn't necessary.
