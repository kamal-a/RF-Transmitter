#pivectors[146] =[0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,
 #               1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,
 #               0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,
 #               1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,
 #               0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1]
 
pichar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ /'
#print(pichar.index('G is', 16))
o = pichar.find("O")
z = pichar.find("Z")
x = pichar.find("7")
i = pichar.find("I")
g = pichar.find("G")
y = pichar.find("Y")
s = pichar.find(" ")
 
SourceEnc = o 
SourceEnc = SourceEnc*38 + z
SourceEnc = SourceEnc*38 + x
SourceEnc = SourceEnc*38 + i 
SourceEnc = SourceEnc*38 + g
SourceEnc = SourceEnc*38 + y
SourceEnc = SourceEnc*38 + s
SourceEnc = SourceEnc*38 + s
print(s)
print(SourceEnc)
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
    print('%s' % title)     #(4*30 + 26)\n
    print(" ")

    count = len(title) + 9
    for i in range (0, count):
        print("-", end=" ")
    print("\n", end = " ")

    for i in range (0, 145):
        print(dat, end=" ")
        #if ((i+1)%30 == 0):
            #print("/n")
    print("\n\n")
        
Poly1=0xF2D05351
Poly2=0xE4613C47
N = 0
I = 0
    
ConvEnc = []
print("empty list is", ConvEnc)


for j in range(0, 74):
    N = N << 1
    if (SourceEnc & 0x20000000000) != 0:
        N = N | 1
        
    SourceEnc <<= 1
    
    ConvEnc.append(parity(N & Poly1))
    print("ConvEnc1 :", ConvEnc)

    ConvEnc.append(parity(N & Poly2))
    print("ConvEnc2 is:", ConvEnc)
 
print("ConvEnc is:", ConvEnc, end=" ")
   
#print("N is:", N)
#print("new source encoding is:", SourceEnc)
#print("np1 is:", np1)
#print("np2 is:", np2)

#n = [0,1,2,3,4]
#for i in range (0, 6):
#x[i] = 5
#print(x)

#printdata("Convolutional encoded data:", ConvEnc)

#asciisymbols = 146       
#SourceEnc = 0
#ConvEnc = [0] * 146

input = [0, 1, 2 ,3]
print(input)

output = [ ]

interleaved = [3, 2, 1, 0]

for index in interleaved:
    output.append(input(index)
