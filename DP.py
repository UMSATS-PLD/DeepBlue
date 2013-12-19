# Detector Range: 200-1100 nm
# 2048 pixels
# 15um x 200um pixel size

import sys
import matplotlib.pyplot as plt
import numpy

#
# Data Smoothing function
#

def smooth(x,window_len=11,window='hanning'):
    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."
    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."
    if window_len<3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

    s=numpy.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]

    if window == 'flat': #moving average
        w=numpy.ones(window_len,'d')
    else:
        w=eval('numpy.'+window+'(window_len)')

    y=numpy.convolve(w/w.sum(),s,mode='valid')
    return y

#
# Main
#

filepath = sys.argv[1]
content = open(filepath, 'r')
split = content.read().split()

i = 19    # Magic number to skip the header
data = []

# Read in the data
while (i < len(split) - 5):                       #Ignore the final 4 bytes (bad word and 0xFFFD)
  number = (int(split[i]) << 8) + int(split[i+1]) #Ex: '1 1' becomes 100000001_2 = 257 
  data.append(number) 
  i += 2

# Smooth it out
npdata = numpy.asarray(data)
npdata = smooth(npdata)

# Guess at the wavelengths by way of: 
# (Range of wavelengths the USB2000 detects) / (pixels)
x = [200.0]
len_data = len(npdata)
offset = (float) ((1100.0 - 200.0) / len_data);
for k in range(1,len_data):
  x.append(x[k-1] + offset)

# matplotlib plots the data for us
plt.plot(x, npdata)
plt.ylabel('Intensity')
plt.xlabel('Lambda')
plt.show()	
