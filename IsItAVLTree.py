def counter(c):
    global c=0    
def height(node):
    if node==None:
        return 0
    lh=height(node.left)+1
    rh=height(node.right)+1
    return max(lh,rh)
def Vheight(node,b):
    if node==None:
        return 
    if abs(height(node.left) - height(node.right)) > 1:
        b=False
        Vheight(node,b)
        print(b) 
    Vheight(node.left,b)
    Vheight(node.right,b)
def IsTreeBalanced(node):
    print(c)
    Vheight(node,b)
    print(b)
