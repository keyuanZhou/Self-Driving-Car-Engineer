# **Traffic Sign Recognition** 

## Writeup

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # "Image References"

[image1]: ./examples/visualization.png "Visualization"
[image2]: ./examples/grayscaling.png "Grayscaling"
[image3]: ./examples/normalized.png "Random Noise"
[image4]: ./test_images/1.png "Traffic Sign 1"
[image5]: ./test_images/10.png "Traffic Sign 2"
[image6]: ./test_images/2.png "Traffic Sign 3"
[image7]: ./test_images/3.png "Traffic Sign 4"
[image8]: ./test_images/5.png "Traffic Sign 5"
[image9]: ./test_images/6.png "Traffic Sign 6"
[image10]: ./test_images/8.png "Traffic Sign 7"
[image11]: ./test_images/9.png "Traffic Sign 8"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Data Set Summary & Exploration

#### 1. Provide a basic summary of the data set. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set is ?

  37184

* The size of the validation set is ?

  9296

* The size of test set is ?

  12630

* The shape of a traffic sign image is ?

  (32, 32, 3)

* The number of unique classes/labels in the data set is ?

  43

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a histogram showing how the data is distributed by different classes.

![alt text][image1]

### Design and Test a Model Architecture

#### 1. Describe how you preprocessed the image data. What techniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, and provide example images of the additional data. Then describe the characteristics of the augmented training set like number of images in the set, number of images for each class, etc.)

As a first step, I decided to convert the images to grayscale because this method worked very well for Sermanet and LeCun as described in their paper of traffic sign classification. Also, it reduces the data volume by decrease the color channel from 3 to 1. Here is an example of a traffic sign image before and after grayscaling.

![alt text][image2]

As a last step, I normalized the image data because we could use a singular learning rate even with a wider distribution in the data. Here is an example of a grayscaling image and a normalized image:

![alt text][image3]

I decided to generate additional data because for some classes, the data is far fewer than the rest, which would lead some bias when training the data. To add more data to the the data set, I created copies of the original data and changed them by randomly translating, scaling, warping and brightness adjusting.




#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

|      Layer      |               Description                |
| :-------------: | :--------------------------------------: |
|      Input      |            32x32x1 RGB image             |
| Convolution 5x5 | 1x1 stride, same padding, outputs 28x28x6 |
|      RELU       |                                          |
|   Max pooling   |       2x2 stride,  outputs 14x14x6       |
| Convolution 5x5 | 1x1 stride, same padding, outputs 10x10x16 |
|      RELU       |                                          |
|   Max pooling   |        2x2 stride,  outputs 5x5x6        |
|     Flatten     |               outputs 400                |
| Fully connected |               outputs 120                |
|      RELU       |                                          |
|     Dropout     |                                          |
| Fully connected |                outputs 84                |
|      RELU       |                                          |
|     Dropout     |                                          |
| Fully connected |                outputs 43                |
|     Softmax     |                                          |



#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used the same architecture from the LeNet Lab. This model worked very well and had a validation accuracy at 97.7%.

batch size = 100

epochs = 20

learning rate = 0.0009

mu = 0

sigma = 0.1

dropout = 0.5



#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

My final model results were:
* training set accuracy of ?

  97.6%

* validation set accuracy of ? 

  97.7%

* test set accuracy of ?

  93.1%

If a well known architecture was chosen:
* What architecture was chosen?

  The LeNet architecture.

* Why did you believe it would be relevant to the traffic sign application?

  First, I believed that the problem of traffic sign classification was similiar to the problem dealt by LeNet architecture; second, the input materials was similiar because I changed the colored pictures into grey.

* How does the final model's accuracy on the training, validation and test set provide evidence that the model is working well?

  I believed the final accuracy was good enough.

  ​


### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are 8 German traffic signs that I found on the web:

![alt text][image4] ![alt text][image5] ![alt text][image6] ![alt text][image7]

![alt text][image8]![alt text][image9]![alt text][image10]![alt text][image11]

The 3rd image might be difficult to classify because it might be easily classified into other traffic signs which were similar to this sign.

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

|                 Image                 |              Prediction               |
| :-----------------------------------: | :-----------------------------------: |
| Right-of-way at the next intersection | Right-of-way at the next intersection |
|         Speed limit (60km/h)          |         Speed limit (60km/h)          |
|         Speed limit (30km/h)          |         Speed limit (50km/h)          |
|             Priority road             |             Priority road             |
|              Keep right               |              Keep right               |
|            Turn left ahead            |            Turn left ahead            |
|            General caution            |            General caution            |
|               Road work               |               Road work               |


The model was able to correctly guess 7 of the 8 traffic signs, which gives an accuracy of 87.5%. This compares favorably to the accuracy on the test set of 93.1%.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

For the 3rd image, the model is relatively sure that this is a Speed limit (50km/h) sign (probability of 0.6), but it was wrong. The top five soft max probabilities were:

| Probability |      Prediction      |
| :---------: | :------------------: |
|     .60     | Speed limit (50km/h) |
|     .40     | Speed limit (30km/h) |
|     .00     | Speed limit (70km/h) |
|     .00     | Roundabout mandatory |
|     .00     | Speed limit (20km/h) |
