#source code

def main():
    message = input("enter the message:")  #the input message
    def msg(n):
        n == 8
    return msg
    
  
    message = msg
    if n != 8:
        print("message is nit valid")
    else:    
        data = bytes(message, "ascii")     #converting the letters into the equivlant ascii symbols
        print(list(data))
        print(data[0])
        N = 0      # 
        for i in range(0, 8):
            N = N * 38 + data[i]
            print(N)
    

      
     

main()