import csv
import cv2
import numpy as np

lines = []

with open('data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

lines = lines[1:]

images = []
measurements = []
correction = 0.2

for line in lines:
    measurement = float(line[3]) # steering angle
    # center
    source_path = line[0]
    filename = source_path.split('/')[-1]
    originalImage = cv2.imread('data/IMG/' + filename)
    image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    images.append(image)
    measurements.append(measurement)
    # left
    source_path = line[1]
    filename = source_path.split('/')[-1]
    originalImage = cv2.imread('data/IMG/' + filename)
    image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    images.append(image)
    measurements.append(measurement + correction)
    # right
    source_path = line[2]
    filename = source_path.split('/')[-1]
    originalImage = cv2.imread('data/IMG/' + filename)
    image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    images.append(image)
    measurements.append(measurement - correction)

augmented_images = []
augmented_measurements = []

for image, measurement in zip(images, measurements):
    augmented_images.append(image)
    augmented_measurements.append(measurement)
    augmented_images.append(cv2.flip(image,1))
    augmented_measurements.append(measurement*(-1.0))
    
X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D


model = Sequential()
model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160, 320, 3))) # set up lambda layer
model.add(Cropping2D(cropping=((50,25),(0,0))))
model.add(Convolution2D(24,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(36,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(48,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(64,3,3, activation='relu'))
model.add(Convolution2D(64,3,3, activation='relu'))
model.add(Dropout(0.5, noise_shape=None, seed=None))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
saved_model = model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=5)

model.save('model.h5')