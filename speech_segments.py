#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:23:05 2017

@author: dsi
"""

def getSegments(audioSegment, silenceThreshold = 2000):
    
    silenceLength = max(audioSegment) * .1

    
    sentenceStarted = False
    sentenceList = []
    starting = 0
    
    lowAmplitudeFound = False
    lowAmplitudeCount = 0
    
    for i in range(0, len(audioSegment)):
        if(abs(audioSegment[i]) >= silenceThreshold and not sentenceStarted):
            sentenceStarted = True
            starting = i
        
        if(abs(audioSegment[i]) < silenceThreshold):
            lowAmplitudeFound = True
            lowAmplitudeCount += 1
        else:
            lowAmplitudeFound = False
            lowAmplitudeCount = 0
            
        if(lowAmplitudeCount >= silenceLength and sentenceStarted):
            sentenceStarted = False
            sentenceList.append((starting, i))
            
    return sentenceList

