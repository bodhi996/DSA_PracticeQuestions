def IsCodeValid(d0,m0):
    d = {v: k for k, v in d0.items()}
    m=str(m0)
    wd=''
    for i in range(len(m)):
        wd+=m[i]
        if(len(wd)>4):
            return False
        if wd in d.keys():
            wd=''
    if not wd=='':
        return False
    return True
hfcode = eval(input())
message = input()
print(IsCodeValid(hfcode,message)) 
