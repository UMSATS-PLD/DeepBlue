import sys
import matplotlib.pyplot as plt

filepath = sys.argv[1]
content = open(filepath, 'r')
split = content.read().split()

i = 19    #Temporary magic number to skip the header
data = []

while (i < len(split) - 5):                       #Ignore the final 4 bytes (bad word and 0xFFFD)
  number = (int(split[i]) << 8) + int(split[i+1]) #Ex: '1 1' becomes 100000001_2 = 257 
  data.append(number) 
  i += 2

# matplotlib plots the data for us
plt.plot(data)
plt.ylabel('Intensity')
plt.xlabel('array position')
plt.show()	
