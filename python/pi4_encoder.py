import numpy as np
from gnuradio import gr

import pmt 

textboxvalue = ""

class pi4_encoder(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(self,
            name='PI4 Beacon Encoder ',   # will show up in GRC
            in_sig = None,
            out_sig = [np.byte])
           
        self.message_port_register_in(pmt.intern('msg_in'))
        self.message_port_register_out(pmt.intern('clear_input'))
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg)

    def handle_msg(self, msg):
        global textboxvalue
        textboxvalue = pmt.symbol_to_string (msg)
    #    # print textboxvalue      
    
    def parity(self, value):     
        even = 0     
        for bitNo in range (0, 32):         
            if (((value >> bitNo) & 0x01) != 0):             
               even = 1 - even     
        return even

    def work(self, input_items, output_items):
        global textboxvalue 
         
        if len(textboxvalue) ==0:
            return 0
        
       
        PI4Vectors = [0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,          
                      1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,  
                      0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,   
                      0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1]  

        pichar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ /'   #this is line assigns a value to each 
        
        mes = ""
        mes = textboxvalue
       
        print("length of mes is ", len(mes))
        # Check message length
        if len(mes) > 8:
            print("message is not available")
        elif len(mes) <= 8:
            space = 8 - len(mes)
            print("how many spaces we need", space)
            string_length = len(mes) + space
            string_revised = mes.ljust(string_length)
            print("new message length", len(string_revised))
        
            o = pichar.find(string_revised[0]) #
            z = pichar.find(string_revised[1])
            x = pichar.find(string_revised[2])
            i = pichar.find(string_revised[3]) 
            g = pichar.find(string_revised[4]) 
            y = pichar.find(string_revised[5]) 
            s = pichar.find(string_revised[6]) 
            h = pichar.find(string_revised[7])
         
 
            SourceEnc = o                           #This is the method used to generate t he  SourceEnc = SourceEnc
            SourceEnc = SourceEnc*38 + z            #Source encoding of the bits SourceEnc = SourceEnc*38 + x   
            SourceEnc = SourceEnc*38 + x 
            SourceEnc = SourceEnc*38 + i  
            SourceEnc = SourceEnc*38 + g 
            SourceEnc = SourceEnc*38 + y 
            SourceEnc = SourceEnc*38 + s
            SourceEnc = SourceEnc*38 + h 

        #print(s) print(SourceEnc)                        
            hexa = hex(SourceEnc) 
        #print("hex decimal equivlant is:", hexa)

        #convolutional encoding

            Poly1 = 0xF2D05351               #generating two registers named poly1 and pol y2 
            Poly2 = 0xE4613C47 
            N = 0 
            I = 0 
            ConvEnc = [] 
        #print("empty list is", ConvEnc)

            for j in range(0, 73):  
                N = N << 1                               #encoding was achieved     
                if (SourceEnc & 0x20000000000) != 0:   #100      
                    N = N | 1               
            
                SourceEnc <<= 1          
                ConvEnc.append(self.parity(N & Poly1))          
                ConvEnc.append(self.parity(N & Poly2)) 
         #print("ConvEnc is:", ConvEnc, end=" ")#this lines prints out theconvolutional           
        #return (ConvEnc)

            P = 0                          #initialising a counter P (108)
            R = 0                          #initialising a counter R 
            PI4symbols = 146 
            R_array = [ ]
            R_array_other = [ ] 
  
            for I in range (0, 256):                      #line 84-97 demonstrates how to achieve 
                for BitNo in range (0, 8):                #the interleaving encoding
                    if (((I >> BitNo) & 0x01) == 0x01):
                        R |= 1 << (7 - BitNo)
                    else:
                        R = R & ~(1 << (7 - BitNo))
             
                R_other = int('{:08b}'.format(I)[::-1], 2)  
                assert(R == R_other, "Rs do not match ")
            #if ((P < PI4symbols) and (R < PI4symbols)):
                if R < 146:
                    R_array.append(R)
                if R_other < 146:
                    R_array_other.append(R_other)

         
         #print("The equivlent R array is:", R_array)
         #print("R_other is ", R_array_other)


            incrementing = 0
            interleaved = [0]*PI4symbols             #defining an array for the interleaved data
            for index in R_array:
                interleaved[index] = ConvEnc[incrementing]
                incrementing += 1

            merge_sync = [ ] 
            for i in range(0, len(interleaved)): 
                merge_sync.append(interleaved[i] * 2 + PI4Vectors[i])
        
            for x in range(len(merge_sync)):
                output_items[0][x] = merge_sync[x]
            print (merge_sync)
            self.message_port_pub(pmt.intern('clear_input'), pmt.intern(''))
            textboxvalue = ""
        
            
 
           
            return (len(merge_sync))

         #print("data symbols is:", merge_sync ) 
         

