#input = [0, 1, 2 ,3]
#print(input)

#output = [ ]

#interleaved = [1, 2, 3, 0]

#for index in interleaved:
#    output.append(input[index])
#print(output)

pichar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ /'   #this is line assigns a value to each 
        
       
textboxvalue = 'OZ7IGY  '
        
o = pichar.find(textboxvalue[0]) #
z = pichar.find(textboxvalue[1])
x = pichar.find(textboxvalue[2])
i = pichar.find(textboxvalue[3]) 
g = pichar.find(textboxvalue[4]) 
y = pichar.find(textboxvalue[5]) 
s = pichar.find(textboxvalue[6]) 
h = pichar.find(textboxvalue[7])
         
 
SourceEnc = o                           #This is the method used to generate t he  SourceEnc = SourceEnc
SourceEnc = SourceEnc*38 + z            #Source encoding of the bits SourceEnc = SourceEnc*38 + x   
SourceEnc = SourceEnc*38 + x 
SourceEnc = SourceEnc*38 + i  
SourceEnc = SourceEnc*38 + g 
SourceEnc = SourceEnc*38 + y 
SourceEnc = SourceEnc*38 + s
SourceEnc = SourceEnc*38 + h 

print(s) 
print(SourceEnc)                        
hexa = hex(SourceEnc) 
print("hex decimal equivlant is:", hexa)

