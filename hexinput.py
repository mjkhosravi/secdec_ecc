import math
# Function to check 
# Log base 2 
def Log2(x): 
    return (math.log10(x) / 
            math.log10(2)); 
  
# Function to check 
# if x is power of 2 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));


user_input = input("Enter a hex number: ")
scale = 16
try:
	hexval = int(user_input, scale)
except:
	print('That is an invalid hex value.')
# Code to convert hex to binary 
res = bin(int(user_input, scale))[2:].zfill(4)
#Calculation of the number of redundant bits
r=1
while(2**r<len(res)+r+1):
	r=r+1		
outputsize=len(res)+r
numberofr=0
positionr=[]
output = []
#Positioning the redundant bits and copy the input bits	
for i in range(1,outputsize+1):
	if(isPowerOfTwo(i)):
		numberofr=numberofr+1
		positionr.append(i)
		output.append(0)
	else:
		output.append(int(res[len(res)-i+len(positionr)]))
		#print (res[len(res)-i+len(positionr)])
#output with redundant bits=0 and inutbits
#print (output)
#Calculating the values of each redundant bit
for i in range(0,len(positionr)):
	x=2**i
	for j in range(1,outputsize+1):
		if (((j >> i) & 1) == 1):
			if (x != j):								
				output[x-1] = output[x-1] ^ output[j-1]
#output with redundant bits and inutbits
#print (output)
bitoutput="";
for i in range(0,len(positionr)):
	x=2**i;
	bitoutput=str(output[x-1])+bitoutput
print("Redundant bits")
print(bitoutput)
print("Redundant bits in Hex")
print(hex(int(bitoutput, 2)))

