#source coding
msg = input("enter your message:")
print("length of the input msg", len(msg))
s = 8 - len(msg)
print("number of spaces required:", s)
x = ' ' 

a = msg+s*x
if len(msg) <= 8:

    print (msg+s*x)
    print("length of the modified input:", len(a))
    data = bytes(a, "ascii")
    print(list(data))
    print(data[0])
    N = 0
    for i in range(0, 8):
        N = N * 38 + data[i]
        print(N)
else:
    print("message is not valid")

# convolutional encoding 





