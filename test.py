# From lib/python3.7/string.
n = 8
def main():
    msg[n] = input("enter the message:")  #the input message
    data = bytes(msg[n], "ascii")     #converting the letters into the equivlant ascii symbols
    print(list(data))
    #print(data[0])
    N = 0      # 
    for i in range(0, 8):
        N = N * 38 + data[i]
        print(N)

main()