

# source encoding using pi4 symbols


PI4symbols = 146
PI4MaxInfoLength = 8

PI4char = {
    '0' : '0', '1' : '1', '2' : '2',
    '3' : '3', '4' : '4', '5' : '5',
    '6' : '6', '7' : '7', '8' : '8',
    '9' : '9', 'A' : '10', 'B' : '11',
    'C' : '12', 'D' : '13', 'E' : '14',
    'F' : '15', 'G' : '16', 'H' : '17',
    'I' : '18', 'J' : '19', 'K' : '20',
    'L' : '21', 'M' : '22', 'N' : '23',
    'O' : '24', 'P' : '25', 'Q' : '26',
    'R' : '27', 'S' : '28', 'T' : '29',
    'U' : '30', 'V' : '31', 'W' : '32',
    'X' : '33', 'Y' : '34', 'Z' : '35',
    ' ' : '36', '/' : '37'
    }

PI4Vector = [0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,
            1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,
            0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,
            1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,
            0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1]

msg = input("enter your message:")
print("length of the input msg", len(msg))
s = 8 - len(msg)
print("number of spaces required:", s)
x = ' ' 

PI4char = msg+s*x
if len(msg) <= 8:

    print (msg+s*x)
    print("length of the modified input:", len(PI4char))
    #data = bytes(a, "ascii")
    data = PI4char
    print(list(data))
    print(data[0])
    SourceEnc = 0
    for i in range(0, 8):
        SourceEnc = SourceEnc * 38 + data[i]
        print(SourceEnc)
else:
    print("message is not valid")

