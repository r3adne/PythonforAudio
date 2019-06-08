import tensorflow as tf 
from tensorflow import keras
import librosa
import os

import numpy as np 
import matplotlib.pyplot as plt 

# fashion_mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class LearningRecording:
    def __init__(self, path):
        # defines self.path
        self.path = path

        # defines self.audio, self.label
        if path[0] in [0, 1, 2, 3, 4] and path[1] != '_':
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0])
        if path[2] == '_':
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0:2]) 
        elif path[0] in [5, 6, 7, 8, 9]:
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0]) 

        self.nsamples = len(self.audio)
        self.image = None


    def makeImage(self, maxNumSamp, spectSize=1024):
        if self.nsamples < maxNumSamp: # if the clip is shorter than the longest clip:
            self.audio.append(np.zeros((1, maxNumSamp - self.nsamples)))
        pass


data_path = '~/data/recordings/'
data = []
maxlen = 0
for i in os.listdir(data_path):
    a = LearningRecording(i)
    if a.nsamples > maxlen:
        maxlen = a.nsamples
    data.append(a)

for i in data:
    i.makeImage(maxlen)
    

class_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


train_images = train_images / 255.0

test_images = test_images / 255.0


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)


predictions = model.predict(test_images)

correct = 0
incorrect = 0

for i in range(len(predictions)):
    if np.argmax(predictions[0]) == test_labels[0]:
        correct += 1
    else:
        incorrect += 1

print('correct {}; incorrect {}'.format(correct, incorrect))
print('loss: {}; accuracy: {}'.format(test_loss, test_acc))