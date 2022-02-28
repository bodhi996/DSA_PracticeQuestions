def STF(task):
    task.sort(key=lambda x:x[2])
    #print(task)
    t=0
    l=[]
    c=len(task)
    while(True):
        if len(l)==c:
            break
        for i in task:
            if i[1]<=t:
                l.append(i[0])
                task.remove(i)
                t+=i[2]
                break;
    return(l)
task = eval(input())
print(STF(task))
