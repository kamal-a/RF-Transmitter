# From lib/python3.7/string.

#def main():
msg = input("enter the message:")
print(msg)
data = bytes(msg, "ascii")
print(list(data))
print(data[0])
N = 0
for i in range(0, 9):
    N = N * 38 + data[i]
    print(N)


 
