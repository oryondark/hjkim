class BitArray:
    
    def createBitArray(self):
        self.BitArray = [False]*2
        #print(bin(self.BitArray[0]))
        self.MASK = 0b1

    def set_bit(self,num):
        idx = (num - 1) // 32 # get array idx
        print("get num " + str(num) +" array index :" + str(idx))
        locate = num - (32*idx) -1 # get bit position
        #print(locate)
        """
        >>> format(mask<<5, '#032b')
        '0b000000000000000000000000100000'
        """

        self.BitArray[idx] |= self.MASK << locate
        #print(format(self.BitArray[idx], "#032b"))
        #print(self.BitArray)

    def toggle(self,num):
        idx = (num - 1) // 32 # get array idx
        print("get num " + str(num) +" array index :" + str(idx))
        locate = num - (32*idx) -1 # get bit position

        self.BitArray[idx] ^= self.MASK << locate

    def clear(self):
        array_size = len(self.BitArray)
        i = 0
        while i < array_size:
            self.BitArray[i] >>= 32
            i += 1

        print("clear array :" + str(self.BitArray))
            

    #test print#
    def read_bit(self):
        array_size = len(self.BitArray)
        i = 0
        while i < array_size:                
            print("array index :" + str(i)
                  + ": " + format(self.BitArray[i], "#032b"))
            i += 1


if __name__ == "__main__":
    bitvector = BitArray()
    bitvector.createBitArray() #초기 생성에서는 Bool 

    print("-------------set bit-------------")
    bitvector.set_bit(5)
    bitvector.set_bit(32)
    bitvector.set_bit(22)
    bitvector.set_bit(9)
    bitvector.set_bit(12)
    bitvector.set_bit(35)
    bitvector.set_bit(33)
    bitvector.set_bit(5)
    bitvector.read_bit()


    print("-------------toggle bit-------------")
    bitvector.toggle(5)
    bitvector.read_bit()

    print("-------------clear bit-------------")
    bitvector.clear()
    bitvector.read_bit()
    
"""
PS D:\> python.exe .\Bitvector.py
-------------set bit-------------
get num 5 array index :0
get num 32 array index :0
get num 22 array index :0
get num 9 array index :0
get num 12 array index :0
get num 35 array index :1
get num 33 array index :1
get num 5 array index :0
array index :0: 0b10000000001000000000100100010000
array index :1: 0b000000000000000000000000000101
-------------toggle bit-------------
get num 5 array index :0
array index :0: 0b10000000001000000000100100000000
array index :1: 0b000000000000000000000000000101
-------------clear bit-------------
clear array :[0, 0]
array index :0: 0b000000000000000000000000000000
array index :1: 0b000000000000000000000000000000

format 함수에서 맨 뒷부분 "0000" = "00"으로 단축됨
"""
