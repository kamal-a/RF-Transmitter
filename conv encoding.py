#convolutional encoding

def parity(value):
        even = 0
        for bitNo in range (0, 31):
            if (((value >> bitNo) & 0X01) != 0):
                even = 1 - even
        return even 



Poly1=0xF2D05351
Poly2=0xE4613C47
N = 0
I = 0
    
asciisymbols = 174        
SourceEnc = 0
ConvEnc = [None] * 174

for j in range(0, 87):
    N <<= 1
    if (SourceEnc and 0X7837222C7BB800) != 0:
        N |= 1
    SourceEnc <<= 1
    
    ConvEnc[I] = parity(N and Poly1)
    I = I + 1
    
