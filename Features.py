#!/usr/bin/python3

import time
import sched
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import sounddevice as sd
import scipy.io.wavfile as wav
import pydub 
from python_speech_features import mfcc

#%% Reading


#Sample 1
#(rate, data) = wav.read("Hello-SoundBible.com-218208532.wav")

#sample 2
(rate, data) = wav.read("Hello-SoundBible.com-1812488315.wav")

#data2 = pydub.AudioSegment.from_mp3("Hello-SoundBible.com-1812488315.mp3")

#data2 = np.array( data2.get_array_of_samples() )


#singleChanelData = np.zeros(len(data), dtype=np.int16)

data = data[:, 0] #*.5 + data[:, 1] *.5 

sprectrum = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(sprectrum))

sd.play(data)

fig = plt.figure(figsize=(5,8))
plt.subplots_adjust(hspace=.6)

plt.subplot(2,1,1)
plt.title("Time Domain")
line, =  plt.plot(data)
plt.ylabel('Amplitude')
plt.xlabel('Time(sec/frames)')

plt.subplot(2,1,2)
plt.title("Frequency Domain")
plt.plot(frequencies, sprectrum)
plt.ylabel('F(x)')
plt.xlabel('Frequency(Hz)')

plt.show()

#plt.ion()

segmentTime = 100 #ms

lenSegment = rate * segmentTime / 1000 #10ms segment
startSegment = 0
endSegment = lenSegment;


figCount = 0

sizeList = []

while(endSegment < len(data)):
    
    figCount += 1
    
    plt.figure(figCount)
    #ax = fig.add_subplot(211)
    #ax2 = fig.add_subplot(212)
    plt.title('MFCC Features (frame: %s - %s)' % (startSegment, endSegment) )


    mfcc_features = mfcc(data[startSegment:endSegment], rate, nfft=1500)
    plt.imshow(mfcc_features, aspect='auto', origin='lower')
    
    
    cbar = plt.colorbar()
    #ax.plot_wireframe(range(len(mfcc_features)), range(len(mfcc_features[0])), mfcc_features)
    #plt.pause(.5)
    
    sizeList.append(np.shape(mfcc_features))
    
    startSegment = endSegment + 1
    endSegment = startSegment + lenSegment #10ms segment
    
    plt.savefig('./MFCC_Features/Sample2/%d.png' % figCount)