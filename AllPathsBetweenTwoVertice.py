def dfs(l,j,d,dvis,L0,A):
    dvis[j]=1
    L0.append(j)
    if(j==d):
        A.append("".join(L0)) 
    else:
        for i in l[j]:
            if(dvis[i]==0):
                dfs(l,i, d, dvis,L0,A)
    
    dvis[j]=0
    L0.pop()


    
def findAllPaths(v,l,s, d):
    L=[]
    dvis=dict.fromkeys(v, 0)
    L0=[]
    A=[]
    dfs(l,s, d, dvis,L0,A)
    #print(dvis)
    return(A)
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))
