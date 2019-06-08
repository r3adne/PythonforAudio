# This is designed to show you what an actual codebase might look like. Don't be worried if it doesn't make sense. 
# This is a snippet of a machine learning program that should be able to detect spoken digits. 
# I'm adapting it to tell the difference between different beatbox sound gestures so that I can turn them into midi.
# To do that, I'll also need several other mechanisms including an onset detector for mapped sounds.

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
        self.valid = False

        # defines self.audio, self.label
        if int(path[0]) in [0, 1, 2, 3, 4] and path[1] != '_':
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0])
        elif path[2] == '_':
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0:2]) 
        elif int(path[0]) in [5, 6, 7, 8, 9]:
            self.audio, sr, self.label = librosa.load(path, mono=0, sr=22050), int(path[0]) 
        else: 
            print('loading failed on {}'.format(self.path))

        self.nsamples = len(self.audio)
        self.image = None


    def makeImage(self, maxNumSamp, spectSize=1024):
        if self.nsamples < maxNumSamp: # if the clip is shorter than the longest clip:
            self.audio.append(np.zeros((1, maxNumSamp - self.nsamples)))
        
        self.image = librosa.core.stft(self.audio, n_fft=spectSize, dtype=np.uint8)


data_path = '/Users/zt/data/recordings/'
data, valid = [], []    
maxlen = 0
class_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in os.listdir(data_path):
    a = LearningRecording(i)
    if a.nsamples > maxlen:
        maxlen = a.nsamples
    data.append(a)
for i in data:
    i.makeImage(maxlen)
    

# makes validation set
for i, e in enumerate(data):
    if i % 13 == 0:
        e.valid = True
        valid.append(e)
        data.remove(e)


model = keras.Sequential([
    keras.layers.Flatten(input_shape=data[0].image.shape),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit([i.image for i in data], [i.label for i in data], epochs=5)

test_loss, test_acc = model.evaluate([i.image for i in valid], [i.label for i in valid])


predictions = model.predict([i.image for i in valid])

correct = 0
incorrect = 0

for i in range(len(predictions)):
    if np.argmax(predictions[0]) == test_labels[0]:
        correct += 1
    else:
        incorrect += 1

print('correct {}; incorrect {}'.format(correct, incorrect))
print('loss: {}; accuracy: {}'.format(test_loss, test_acc))