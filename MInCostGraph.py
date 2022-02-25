class XYZ_Courier:
    def __init__(self,WL):
        self.WL=WL
    def route(self,s,dest):
        L=self.WL
        dist={}
        p={}
        vis={}
        for i in L.keys():
            (dist[i],p[i],vis[i])=(99999,-1,False)
        dist[s]=0
        for i in L.keys():
            for u in L.keys():
                for (v,d) in L[u]:
                    if dist[v]>dist[u]+d:
                        dist[v]=dist[u]+d
                        p[v]=u
        l=[]
        l.append(dest)
        while(True):
            l=[p[l[0]]]+l
            if l[0]==s:
                break;
        return l
    def cost(self,s,d):
        L=self.WL
        l=self.route(s,d)
        c=0
        for i in range(len(l)-1):
            #print(c)
            for j in L[l[i]]:
                #print(j)
                if(j[0]==l[i+1]):
                    c+=j[1]
        return c*5
size = int(input())
edges = eval(input())
s=int(input())
d=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))
