#PIsymbols = {
#    '0' : '0', '1' : '1', '2' : '2',
#    '3' : '3', '4' : '4', '5' : '5',
#    '6' : '6', '7' : '7', '8' : '8',
#    '9' : '9', 'A' : '10', 'B' : '11',
#    'C' : '12', 'D' : '13', 'E' : '14',
#    'F' : '15', 'G' : '16', 'H' : '17',
#    'I' : '18', 'J' : '19', 'K' : '20',
#    'L' : '21', 'M' : '22', 'N' : '23',
#    'O' : '24', 'P' : '25', 'Q' : '26',
#    'R' : '27', 'S' : '28', 'T' : '29',
#    'U' : '30', 'V' : '31', 'W' : '32',
#    'X' : '33', 'Y' : '34', 'Z' : '35',
#    ' ' : '36', '/' : '37'
#    }

#print(PIsymbols['O'])
#o = PIsymbols['O']
#z = PIsymbols['Z']
#x = PIsymbols['7']
#i = PIsymbols['I']
#g = PIsymbols['G']
#y = PIsymbols['Y']

pichar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ /'
#print(pichar.index('G is', 16))
o = pichar.find("O")
z = pichar.find("Z")
x = pichar.find("7")
i = pichar.find("I")
g = pichar.find("G")
y = pichar.find("Y")
s = pichar.find(" ")
 
n = o 
n = n*38 + z
n = n*38 + x
n = n*38 + i 
n = n*38 + g
n = n*38 + y
n = n*38 + s
n = n*38 + s
print(s)
print(n)






#print(i)


#print(h)



#n = 0
#for i in range(0, 9):
#    n = n * 38 + msg[i]
#    print(n)

#print(z)
#x = PIsymbols['A'] + PIsymbols['E']
#print("x is equal to", x)

#PIchars = '0123ABCD'
#print(PIchars[6])


