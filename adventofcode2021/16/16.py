import sys
"""
LITERAL PACKET STRUCTURE
- 3 bits: packet version
- 3 bits: typeID
- rest: packets of 1+<4bits>, 1+<4bits>, ..., 0+<4bits>
--> normal 3bit numbers

OPERATOR PACKET STRUCTURE
- 3 bits: packet version
- 3 bits: typeID
- 1 bit: length type ID

literal ID INTERPRETATIONS
4: literal value (packet encodes single binary number)

length type ID INTERPRETATIONS
0: next 15 bits number to indiacte total length in bits of subpackets
1: next 11 bits number to indicate number of subpackets contained
"""

VERSION_SUM = 0

class Literal():
    def __init__(self, version, typeid, content):
        self.version = int(version, 2)
        global VERSION_SUM
        VERSION_SUM += self.version
        self.typeid = typeid
        self.content = content

    def getValue(self):
        return self.content

class Operator():
    def __init__(self, version, typeid, lentypeid, content):
        self.version = int(version,2)
        global VERSION_SUM
        VERSION_SUM += self.version
        self.typeid = int(typeid, 2)
        self.lentypeid = lentypeid
        self.content = content
    
    def getValue(self):
        if self.typeid == 0:
            changed = False
            r = 0
            for child in self.content:
                r += child.getValue()
                changed = True
            if not changed: print("oh no")
        elif self.typeid == 1:
            changed = False
            r = 1
            for child in self.content:
                r *= child.getValue()
                changed = True
            if not changed: print("oh no")
        elif self.typeid == 2:
            changed = False
            r = sys.maxsize
            for child in self.content:
                r = min(r,child.getValue())
                changed = True
            if not changed: print("oh no")
        elif self.typeid == 3:
            changed = False
            for child in self.content:
                r = -10
                r = max(r,child.getValue())
                changed = True
            if not changed: print("oh no")
        elif self.typeid == 5:
            assert(len(self.content) == 2)
            r = 1 if self.content[0].getValue() > self.content[1].getValue() else 0

        elif self.typeid == 6:
            assert(len(self.content) == 2)
            r = 1 if self.content[0].getValue() < self.content[1].getValue() else 0
        elif self.typeid == 7:
            assert(len(self.content) == 2)
            r = 1 if self.content[0].getValue() == self.content[1].getValue() else 0
        else:
            print("fuuuuuuuuuuuu")
        return r




        
        



#110100101111111000101000
#VVVTTTAAAAABBBBBCCCCC
def parseLiteral(b_data, END, i):
    version = b_data[i: i+3]
    i += 3
    typ = b_data[i: i+3]
    i += 3
    nums = []
    while(b_data[i] != '0'): #if it is zero it is the end of the number
        i+=1
        nums.append(b_data[i:i+4]) # read 4 bin vals
        i += 4
    i += 1
    nums.append(b_data[i:i+4])
    i+=4
    num = int("".join(nums), 2)
    lit = Literal(version, typ, num)
    return i, lit


def containsOnlyZeros(s):
    for c in s:
        if c != '0': return False
    return True

#11101110000000001101010000001100100000100011000001100000
#VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC^51
def parseOperator(b_data, END, i):
    version = b_data[i: i+3]
    i += 3
    typ = b_data[i: i+3]
    i += 3
    ltypeid = b_data[i]
    i+=1
    content = []
    if ltypeid == '0':
        l = int(b_data[i:i+15], 2)
        i += 15
        i, object = parseBdata(b_data, i + l, i)
        content = object
    elif ltypeid == '1':
        l = b_data[i:i+11]
        i += 11
        n = int(l, 2)
        for _ in range(n):
            i, object = parseBDataSingleStride(b_data, END, i)
            content.append(object)
    O = Operator(version, typ, ltypeid, content)
    return i, O


def parseBDataSingleStride(b_data, END, i):
    i += 3 #skip version
    typ = b_data[i:i+3]
    if int(typ, 2) == 4:
        i -= 3 # move i back
        i, object = parseLiteral(b_data, END, i)
        return i, object
    else:
        i -= 3 # move i back
        i, object = parseOperator(b_data, END, i)
        return i, object


#00111000000000000110111101000101001010010001001000000000
def parseBdata(b_data, END, i):
    objects = []
    if containsOnlyZeros(b_data[i:END]): return i, objects
    while (i < END):
        if containsOnlyZeros(b_data[i:END]): return i, objects
        i += 3 #skip version
        typ = b_data[i:i+3]
        if int(typ, 2) == 4:
            i -= 3 # move i back
            i, o = parseLiteral(b_data, END, i)
            objects.append(o)
        else:
            i -= 3 # move i back
            i, o = parseOperator(b_data, END, i)
            objects.append(o)
    return i, objects




if __name__ == "__main__":
    fname = "16/input.txt"
    f = open(fname, 'r')
    data = [l for l in f][0]



    #data = "D2FE28" # one literal
    #data = "38006F45291200" # operator(15) with two literal packets
    #data = "A0016C880162017C3686B18A3D4780" # operator(11) with two literal packets
    #data = "A0016C880162017C3686B18A3D4780"
    # first parse to binary
    integer = int(data, 16)
    w = len(data) * 4
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=w, type='b')
    b_data = format(integer, spec)
    END = len(b_data) - 1
    _, stuff = parseBdata(b_data, END, 0)
    print(stuff[0])
    print(stuff[0].getValue())













#10637009915279



