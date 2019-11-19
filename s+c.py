#source code
#source coding
pivectors[146] =[0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,
                1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,
                0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,
                1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,
                0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1]
 
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


#convolutional encoding

def parity(value):
        even = 0
        for bitNo in range (0, 31):
            if (((value >> bitNo) & 0X01) != 0):
                even = 1 - even
        return even 


def printdata(title, dat):
    print("%s (4*30 + 26)\n", title)
    print(" ")

    count = len(title) + 9
    for i in range (0, count):
        print("-")
        print("\n")

    for i in range (0, 145):
        print("%d", dat[i])
        if ((i+1)%30 == 0):
            print("/n")
        print("\n\n")
        



Poly1=0xF2D05351
Poly2=0xE4613C47
N = 0
I = 0
    
asciisymbols = 146       
SourceEnc = 0
ConvEnc = [None] * 146

for j in range(0, 73):
    N <<= 1
    if (SourceEnc and 0x20000000000) != 0:
        N |= 1
    SourceEnc <<= 1
    
    ConvEnc[I] = parity(N and Poly1)
    ConvEnc[I] = parity(N and Poly2)
    I = I + 1

printdata("Convolutional encoded data:", ConvEnc)

# interleaved encoding


P = 0 
R = 0
PI4symbols = 146 
for I in range (0, 255):
    for BitNo in range (0, 7):
        if (((I >> BitNo) and 0x01) == 0x01):
            R |= 1 << (7 - BitNo)
        else:
            R = R and (1 << (7 - BitNo))

if ((P < PI4symbols) and (R < PI4symbols)):
    interleaved[R] = ConvEnc[P]
    P +=1 

printdata("interleaved data:", interleaved)

# Merge with sync vectors

def symbols():
    for I in range (0, 145):
        symbols[I] = pivectors[I] or (interleaved[I] << 1)
        printdata("symbols", symbols)

symbols()




