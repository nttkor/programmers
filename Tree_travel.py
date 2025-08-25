'''
preorder, inorder, postorder 함수를 구현하세요.
'''

def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    def dfs(node):
        if node is None:
            return
        result.append(node.index)
        dfs(node.left)
        dfs(node.right)
    dfs(tree)
    return result


def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result=[]
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.index)
        dfs(node.right)
    dfs(tree)
    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.index)
    dfs(tree)
    return result