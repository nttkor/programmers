class Tree:
    def __init__(self, i, l=-1, r=-1):
        self.index = i
        self.left = None
        self.right = None

    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        if self.index == i:
            self.left = Tree(l) if l != -1 else None
            self.right = Tree(r) if r != -1 else None
            return True
        else:
            added = False
            if self.left:
                added = self.left.addNode(i, l, r)
            if not added and self.right:
                added = self.right.addNode(i, l, r)
            return added

    def preorder(self):
        result = [self.index]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.index)
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.index)
        return result

def main():
    n = int(input())
    tree = Tree(1)

    for _ in range(n):
        i, l, r = map(int, input().split())
        tree.addNode(i, l, r)

    print(' '.join(map(str, tree.preorder())))
    print(' '.join(map(str, tree.inorder())))
    print(' '.join(map(str, tree.postorder())))

def text():
    ex = [
    [5],
    [1, 2 ,3],
    [2, 4, 5],
    [3, -1, -1],
    [4, -1, -1],
    [5, -1, -1],
    ]
    n = ex[0][0]
    tree = Tree(1)

    for _ in ex[1:]:
        i, l, r = _[0], _[1], _[2]
        tree.addNode(i, l, r)

    print(' '.join(map(str, tree.preorder())))
    print(' '.join(map(str, tree.inorder())))
    print(' '.join(map(str, tree.postorder())))
    

if __name__ == "__main__":
    # main()
    text()