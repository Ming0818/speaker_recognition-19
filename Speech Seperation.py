#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:25:37 2017

@author: dsi
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import sounddevice as sd
import pydub
from python_speech_features import mfcc

import speech_segments

file = pydub.AudioSegment.from_mp3('./Data/01 - Ielts Practice Tests Plus 1. CD1 - Extract 1.mp3')
#data = np.  (file.export())
rawLeft = file.split_to_mono()[0]
rawRight = file.split_to_mono()[1]

monoLeft = pydub.AudioSegment.from_mono_audiosegments(rawLeft)
monoRigt = pydub.AudioSegment.from_mono_audiosegments(rawRight)

mono = monoLeft.overlay(monoRigt)
data = np.array( mono.get_array_of_samples() )

#n = 30  # the larger n is, the smoother curve will be
#b = [1.0 / n] * n
#a = 1
#yy = lfilter(b,a,data)

#segments = pydub.silence.split_on_silence(mono, min_silence_len=1000, silence_thresh=-18)
'''
silenceThreshold = 2000
silenceLength = np.max(data) * .1


sentenceStarted = False
sentenceList = []
starting = 0

lowPick = 0
highPick = 0
pickEnd = False

lowAmplitudeFound = False
lowAmplitudeCount = 0

for i in range(0, len(data)):
    if(abs(data[i]) >= silenceThreshold and not sentenceStarted):
        sentenceStarted = True
        starting = i
    
    if(abs(data[i]) < silenceThreshold):
        lowAmplitudeFound = True
        lowAmplitudeCount += 1
    else:
        lowAmplitudeFound = False
        lowAmplitudeCount = 0
        
    if(lowAmplitudeCount >= silenceLength and sentenceStarted):
        sentenceStarted = False
        sentenceList.append((starting, i))
    
plt.plot(data)
#plt.plot(yy)
plt.show()
'''

sentenceList = speech_segments.getSegments(data)

#%%
mfccFeatures = []
sample_max = 0
for i in sentenceList:
    mfccFeature = mfcc(data[i[0]:i[1]], mono.frame_rate, nfft=1500)
    mfccFeatures.append(mfccFeature)
    
    if sample_max < len(mfccFeature):
        sample_max = len(mfccFeature)
        
#%%

fig = plt.figure(figsize=(5, 80))
plt.subplots_adjust(hspace=.5)

for i in range(len(mfccFeatures)):
    plt.subplot(len(mfccFeatures), 1, i + 1)
    plt.title('Segment: %d' % i)
    img = plt.imshow(mfccFeatures[i], aspect='auto', origin='lower', vmin=0, vmax=sample_max)

#fig.colorbar(img)
plt.show()


#%%

'''
for i in range(len(sentenceList)):
    print ('Playing %d -----------------------' % i)
    plt.plot(data[sentenceList[i][0]:sentenceList[i][1]])
    plt.show()
    sd.play(data[sentenceList[i][0]:sentenceList[i][1]])
    sd.wait()
'''