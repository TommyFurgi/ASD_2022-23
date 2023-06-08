# Huffman coding
class Huffman:
    def __init__(self,char,f):
        self.code=''
        self.char=char
        self.frequency=f
        self.parent=self
        self.left=None
        self.right=None



def huffman(chars,frequency):
    n=len(chars)

    for i in range(n-1): # sort
        index=i
        for j in range(i+1,n):
            if frequency[j]>frequency[index]:
                index=j

        frequency[index],frequency[i]=frequency[i],frequency[index]
        chars[index],chars[i]=chars[i],chars[index]

    P=[]
    for i in range(n):
        a=Huffman(chars[i],frequency[i])
        P.append(a)


    while len(P)>1:
        a=P.pop()
        b=P.pop()
        sum=a.frequency+b.frequency 
        new=Huffman('',sum)
        new.left=b
        new.right=a
        a.parent=new
        b.parent=new
        P.append(new)
        if len(P)==1:
            continue
            
        for i in range(len(P)-1,0,-1):
            if P[i].frequency>P[i-1].frequency:
                P[i],P[i-1]=P[i-1],P[i]

            else:
                break
        
        
    root=P[0]

    write_code(root)
    print(res)


def write_code(point):
    if point.left!=None:
        point.left.code=point.code+'0'
        write_code(point.left)

    if point.right!=None:
        point.right.code=point.code+'1'
        write_code(point.right)

    if point.char!='':
        res.append((point.char,point.code))

res=[]
chars=['a','b','c','d','e']
frequency=[700,200,120,300,10]
huffman(chars,frequency)

# res=[]
# f=[50,5,60,65,20]
# huffman(chars,f)
