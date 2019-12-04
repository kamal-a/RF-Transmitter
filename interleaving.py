PI4Vectors = [0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1]
convenc_check = '1 1 0 1 1 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 0 1 1 0 0 0 1 0 1 1 1 0 1 0 0 0 1 0 1 0 1 0 1 1 1 1 1 1 1 0 1 0 1 1 0 0 0 1 1 1 1 0 1 0 0 1 0 0 1 0 1 1 1 1 1 0 0 1 0 1 0 0 1 1 1 1 0 1 0 0 0 1 0 1 0 1 0 0 1 0 0 0 0 0 0 1 1 1 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 0 0 0 0'
pichar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ /'   #this is line assigns a value to each 
                                                    #character within the array

message = "OZ7IGY  "
# Check message length

# Source Encoding

o = pichar.find("O")
z = pichar.find("Z")
x = pichar.find("7")
i = pichar.find("I")
g = pichar.find("G")
y = pichar.find("Y")
s = pichar.find(" ")
 
SourceEnc = o                           #This is the method used to generate the 
SourceEnc = SourceEnc*38 + z            #Source encoding of the bits
SourceEnc = SourceEnc*38 + x
SourceEnc = SourceEnc*38 + i 
SourceEnc = SourceEnc*38 + g
SourceEnc = SourceEnc*38 + y
SourceEnc = SourceEnc*38 + s
SourceEnc = SourceEnc*38 + s
print(s)
print(SourceEnc)                        #this line prints out the Source encoding
hexa = hex(SourceEnc)
print("hex decimal equivlant is:", hexa)





#convolutional encoding

def parity(value):
    even = 0
    for bitNo in range (0, 32):
        if (((value >> bitNo) & 0x01) != 0):
            even = 1 - even
    return even 

def printdata(title, dat):
    print('%s' % title)     
    print(" ")

    count = len(title) + 9
    for i in range (0, count):
        print("-", end=" ")
    print("\n", end = " ")

    for i in range (0, 145):
        print(dat, end=" ")
        
    print("\n\n")
        

Poly1 = 0xF2D05351               #generating two registers named poly1 and poly2
Poly2 = 0xE4613C47
N = 0
I = 0
ConvEnc = []
print("empty list is", ConvEnc)

for j in range(0, 73):                       #line 63-72 demostrates how the convolutional 
    N = N << 1                               #encoding was achieved
    if (SourceEnc & 0x20000000000) != 0:
        N = N | 1
        
    SourceEnc <<= 1
    
    ConvEnc.append(parity(N & Poly1))
    
    ConvEnc.append(parity(N & Poly2))
   
print("ConvEnc is:", ConvEnc)    #this lines prints out the convolutional 
                                           #encoding array
convenc_check = convenc_check.split()
convenc_check = [int(i) for i in convenc_check]
print("Conv check is", convenc_check)
assert(ConvEnc == convenc_check)


# interleaving encoding

P = 0                          #initialising a counter P
R = 0                          #initialising a counter R 
PI4symbols = 146 
R_array = [ ]
R_array_other = [ ]                  

for I in range (0, 256):                      #line 84-97 demonstrates how to achieve 
    for BitNo in range (0, 8):                #the interleaving encoding
        if (((I >> BitNo) & 0x01) == 0x01):
            R |= 1 << (7 - BitNo)
        else:
            R = R & ~(1 << (7 - BitNo))

    R_other = int('{:08b}'.format(I)[::-1], 2)  
    assert(R == R_other, "Rs do not match ")
    #if ((P < PI4symbols) and (R < PI4symbols)):
    if R < 146:
        R_array.append(R)
    if R_other < 146:
        R_array_other.append(R_other)
       
print("The equivlent R array is:", R_array)
print("R_other is ", R_array_other)
#print("R is", R)

incrementing = 0
interleaved = [0]*PI4symbols             #defining an array for the interleaved data
for index in R_array:
    interleaved[index] = ConvEnc[incrementing]
    incrementing += 1

print("Convolutional encoding data is:", ConvEnc)      #prints the CE array
print("interleaved data is", interleaved)              #prints out the interleaved array
print("length of conv encoding array:", len(ConvEnc))
print("length of interleaving data is:", len(interleaved))
print("I is:", I)
print("R is:", R)





#merge with sync

merge_sync = [ ] 
for i in range(0, len(interleaved)): 
    merge_sync.append(interleaved[i] * 2 + PI4Vectors[i])

print("data symbols is:", merge_sync ) 

# Merge with sync vector 

#def symbols():
#    for I in range (0, 145):
#        symbols[I] = PI4Vector[I] or (interleaved[I] << 1)
#        printdata("symbols", symbols)

#symbols()
