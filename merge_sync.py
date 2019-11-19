# merge with sync vector 

def symbols():
    for I in range (0, 145):
        symbols[I] = PI4Vector[I] or (interleaved[I] << 1)
        printdata("symbols", symbols)

symbols()
