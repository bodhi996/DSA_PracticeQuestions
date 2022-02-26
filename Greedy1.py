def MaxValueSelection(item,C):
    l=[]
    for i in item:
        l.append((item[i][1]/item[i][0],item[i][0]))
    l.sort()
    c=len(l)
    s=0
    while(c>0):
        #print(C,l[c-1][1])
        if l[c-1][1]<=C:
            C-=l[c-1][1]
            s+=l[c-1][1]*l[c-1][0]
            c-=1
        else:
            s+=C*l[c-1][0]
            break;
    #print(l)
    return(s)
items = eval(input())
C = int(input())
print(round(MaxValueSelection(items, C),2))
