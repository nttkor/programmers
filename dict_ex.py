def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''


    width = dict()
    def dfs(tree,level):
        if tree == None:
            return 0
        if level in width:
            width[level].append(tree.index)
        else:
            width[level] = [tree.index]
        level = dfs(tree.left,level+1)
        level = dfs(tree.right,level+1)
        return 
    dfs(myTree,1)
    max_idx = sorted( [(i,len(v)) for i,v in width.items()] ,lambda x:x[1], reverse=True)[0][1]
    return (0, 0)