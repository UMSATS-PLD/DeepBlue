import sys
import matplotlib.pyplot as plt

filepath = 'C:\Users\NRichard\Documents\Programs\umsats\Deep Blue 120.txt'
content = open(filepath, 'r')
split =  content.read().split()

i = 0
data = []

while (i < len(split) - 1):
	number = (int(split[i]) << 8) + int(split[i+1])
	data.append(number) 
	i += 2

print len(data)

plt.plot(data)
plt.ylabel('Intensity')
plt.xlabel('array position')
plt.show()	
