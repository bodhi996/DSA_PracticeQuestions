def printHuff(d,node, val=''):
    n=val
    if(node.left):
        printHuff(d,node.left,n+'0')
    if(node.right):
        printHuff(d,node.right,n+'1')
    if not node.right and not node.left:
        
        d.append((node.symbol,n))
def decode(root, cipher):
    d=[]
    printHuff(d,root)
    dic={}
    s=""
    wd=""
    for i in d:
        dic[i[1]]=i[0]
    for i in range(len(cipher)):
        wd+=cipher[i]
        if wd in dic.keys():
            s+=dic[wd]
            wd=""
    return(s)
