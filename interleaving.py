# interleaving encoding

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


# Merge with sync vector 

