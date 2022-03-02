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
        Vheight.b='False' 
    Vheight(node.left,b)
    Vheight(node.right,b)
def IsTreeBalanced(node):
    b=True
    Vheight(node,b)
    if hasattr(Vheight,'b'):
        return False
    else:
        return True
