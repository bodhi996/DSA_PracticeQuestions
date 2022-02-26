def addallpath(WList,u, d, visited, path,allpath):
  	visited[u]= True
  	path.append(u)
  	if u == d:
         L = path.copy()
         allpath.append(L)
  	else:
         for i in WList[u]:
             if visited[i[0]]== False:
                 addallpath(WList, i[0], d, visited, path, allpath)      	
  	path.pop()
  	visited[u]= False

def findallpath(WList,s,d):
    visited = {}
    allpath = []
    for v in WList.keys():
        visited[v] = False
    path = []
    addallpath(WList,s, d, visited, path,allpath)
    return(allpath)
def cost(L,l):
    c=0
    a=1
    for i in range(len(l)-1):
        for j in L[l[i]]:
            if j[0]==l[i+1]:
                c+=j[1]
                a+=1
    l.append(a)
    l.append(c)
def best_fare(L,s,d,k):
    t=findallpath(L,s,d)
    for i in t:
        cost(L,i)
    min=[]
    m=9999999
    k+=2
    for i in t:
        if(i[-2]<=k):
            if i[-1]<m:
                min=i
                m=i[-1]
                
    if min==[]:
        return "Not found"
    else:
        return (min[-1],min[0:-2])

size = int(input())
edges = eval(input())
s = int(input()) 
d = int(input())
k = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
print(best_fare(WL,s,d,k))
