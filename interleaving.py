#pivectors[146] =[0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,
    #           1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,
   #             0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,
 ##               1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,
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
        



Poly1 = 0xF2D05351
Poly2 = 0xE4613C47
N = 0
I = 0
    
#asciisymbols = 146       
#SourceEnc = 0
#ConvEnc = [0] * 146
ConvEnc = []
print("empty list is", ConvEnc)
#np1 = N & Poly1
#np2 = N & Poly2


for j in range(0, 73):
    N = N << 1
    if (SourceEnc & 0x20000000000) != 0:
        N = N | 1
        
    SourceEnc <<= 1
    #j += 1
    
    #ConvEnc = parity(N & Poly1)
    #CE1 = ConvEnc
    ConvEnc.append(parity(N & Poly1))
    #print("ConvEnc1 :", ConvEnc)

    #ConvEnc = parity(N & Poly2)
    #CE2 = ConvEnc
    ConvEnc.append(parity(N & Poly2))
    #print("ConvEnc2 is:", ConvEnc)

    #ConvEnc = CE1 + CE2
 
print("ConvEnc is:", ConvEnc, end=" ")

# interleaving encoding
import array
def parity2(value2):
    for bitno in range (0, 8):
        if (((i >> bitno) & 0x01) == 0x01):
            value2 |= 1 << (7 - bitno)
        else:
            value2 &= ~(1 << (7 - bitno))
    return value2

P = 0 
R = 0
PI4symbols = 146 
interleaved = [ ]

for I in range (0, 145):
    for BitNo in range (0, 8):



        if (((I >> BitNo) & 0x01) == 0x01):
            R |= 1 << (7 - BitNo)
        else:
            R = R & ~(1 << (7 - BitNo))
    
   
    #ConvEnc.append(R)
        
    #printdata("interleaved is:", ConvEnc)
       
        #interleaved[:: R]
        #if ((P < PI4symbols) and (R < PI4symbols)):
    #if(3

        #interleaved[R] = ConvEnc
        #interleaved.append(interleaved)
    #interleaved = ConvEnc
        
    interleaved.append(R)
        #interleaved = sorted(ConvEnc, key = R, reverse= False)
        

       
    # interleaved.append(R)
    print("interleaved data:", interleaved)
    
    #print("binary equivlant is:", bin(interleaved))
print("extra:", ConvEnc[32])
print("I is:", I)
print("R is:", R)
#print("interleaved is:", interleaved)


    #interleaved = ConvEnc
    #P +=1 



# Merge with sync vector 

