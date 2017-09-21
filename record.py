#!/usr/bin/python3

import time
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#%% Recording

duration = 3 # Seconds
sd.default.samplerate = fs = 48000
sd.default.channels = 1


# Recording User 1
print('Recording for user 1 within 5 Seconds')

for i in range(4):
    print('... in %d Seconds' % (3 - i))
    if(i != 3 ):
        time.sleep(1)

print("Recording User 1 ....")
myrecording1 = sd.rec(duration * fs)
sd.wait()

# Recording User 2
'''
print('Recording for user 2 within 5 Seconds')

for i in range(5):
    print('... in %d Seconds' % (5 - i))
    if(i != 5 ):
        time.sleep(1)

print("Recording User 2 ....")
myrecording2 = sd.rec(duration * fs)
sd.wait()
'''


#%% Playing

# Playing User 1
print("Playing User 1 ...")
sd.play(myrecording1)
sd.stop()

# Playing User 2
print("Playing User 2 ...")
sd.play(myrecording2)

#%% Display Recording

# Displaying User 1
spectrum = np.fft.fft(myrecording1)
frequencies = np.fft.fftfreq(len(spectrum))

plt.figure(dpi=80)
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.subplot(2,1,1)
plt.suptitle('Recorded Frequency')
plt.plot(myrecording1)

plt.subplot(2,1,2)
plt.suptitle('Fourier Transform')

plt.plot(frequencies, spectrum)


# Display User 2
'''
spectrum = numpy.fft.fft(myrecording2)
frequencies = numpy.fft.fftfreq(len(spectrum))
pylab. plot(frequencies,spectrum)
print('User 2 Plot')
pylab.show()
'''