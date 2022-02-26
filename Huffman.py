class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff=''
def printHuff(d,node, val=''):
    n=val+str(node.huff)
    if(node.left):
        printHuff(d,node.left,n)
    if(node.right):
        printHuff(d,node.right,n)
    if not node.right and not node.left:
        #print(node.symbol,n)
        d.append((node.symbol,n))
def Huffman(s):
    d={i:0 for i in s}
    for i in range(len(s)):
        d[s[i]]+=1
    l=[]
    for i in d.keys():
        l.append(Node(d[i],i))
    while(len(l) >1):
        l=sorted(l, key=lambda x: x.frequency)
        left=l[0]
        right=l[1]
        if left.frequency==right.frequency:
            if left.symbol> right.symbol:
                temp=left
                left=right
                right=temp
        left.huff='0'
        right.huff='1'
        newNode=Node(left.frequency+right.frequency,left.symbol+right.symbol,left,right)
        l.remove(left)
        l.remove(right)
        l.append(newNode)
    d=[]    
    printHuff(d,l[0])
    dic={}
    for i in d:
        #print(i[1])
        dic[i[0]]=i[1]
    return(dic)
s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])
