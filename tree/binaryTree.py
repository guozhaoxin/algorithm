#encoding:utf8
__author__ = 'gold'

class BTNode(object):
    '''
    正常情况下一个二叉树的节点
    '''
    def __init__(self,value,left = None,right = None):
        self.val = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

class BDRTnode(BTNode):
    '''
    二叉树的节点是双向节点，即节点包含父节点的索引
    '''
    def __init__(self,val,parent = None,left = None,right = None):
        super(BDRTnode,self).__init__(left,right)
        self.parent = parent

'''
二叉树类
'''
class BTree(object):
    def __init__(self):
        '''
        二叉树的构造方法
        :param rootnode:BTnode类，表示二叉树的根节点
        '''
        self.root = None #二叉树类的根节点，需要将其设置为私有

    def find(self,val):
        '''
        二叉树的查找方法，
        :param val:要查找的值
        :return:如果找到就返回节点对象BTnode类或者其子类，否则返回None
        '''
        stack = [self.root] #因为是二叉树而不是二叉查找树，所以只能用stack的方法对节点一个个过滤
        index = 0
        while index < len(stack):
            curNode = stack[index]
            if curNode.val == val:
                return curNode
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
            index += 1


    def reset(self,root,brute = False):
        '''
        重新设置一棵树的根节点
        :param root:新设立的根节点
                burte：boolean，主要是当根节点已经存在时是否要强制性重设根节点
        :return: boolean，表示重新设置根节点是否成功
        '''
        if not self.root:
            self.root = root
            return True
        if brute:
            self.root = root
            return True
        else:
            return False


    def emptyBTree(self):
        '''
        判断一棵树是否为空树
        :return: boolean
        '''
        return self.root is None

    def height(self):
        def dfs(node):
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            return max(leftHeight,rightHeight) + 1

        return dfs(self.root)

    @classmethod
    def preOrder(cls,root):
        '''
        递归前序遍历二叉树
        :param root:
        :return: []，由所有节点的值组成的list
        '''
        results = []
        def dfs(node):
            if not node:
                return
            results.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return results

    @classmethod
    def midOrder(cls,root):
        '''
        递归中序遍历二叉树
        :param root:
        :return: []，由所有节点组成的list
        '''
        results = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            results.append(node.val)
            dfs(node.right)
        dfs(root)
        return results

    @classmethod
    def postOrder(cls,root):
        results = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            results.append(node.val)
        dfs(root)
        return results

    @classmethod
    def preOrderGenerator(cls,node):
        stack = [] #存储所有遍历过的节点
        curNode = node
        while curNode or stack:
            while curNode:
                yield curNode.val
                stack.append(curNode)
                curNode = curNode.left
            if stack:
                top = stack.pop()
                curNode = top.right

    @classmethod
    def midOrderGenerator(cls,node):
        stack = []
        curNode = node
        while curNode or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            if stack:
                top = stack.pop()
                yield top.val
                curNode = top.right

    @classmethod
    def postOrderGenerator(cls,node):
        class TempNode:
            def __init__(self,bTreeNode):
                self.bTreeNode = bTreeNode
                self.count = 1

        stack = []
        curNode = node
        while curNode or stack:
            while curNode:
                stack.append(TempNode(curNode))
                curNode = curNode.left
            if stack:
                top = stack[-1]
                if top.count == 1:
                    top.count = 2
                    curNode = top.bTreeNode.right
                else:
                    yield top.bTreeNode.val
                    stack.pop()

    def treeNodeCount(self):
        '''
        统计一棵二叉树上总的节点数量
        :return: int，表示树节点的总数量
        '''
        if not self.root:
            return 0
        stack = [self.root]
        index = 0
        while index < len(stack):
            node = stack[index]
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            index += 1
        return index


    def totalBinTree(self):
        '''
        判断树是否是完全二叉树
        :return:boolean，若为真则返回True，否则False
        '''
        if not self.root:
            return True
        parentStack = [self.root]
        childStack = []
        index = 0
        while index < len(parentStack):
            if parentStack[index] is None:
                if len(childStack) != 0:
                    return False
                while index < len(parentStack):
                    if parentStack[index] is not None:
                        return False
                    index += 1
                return True
            childStack.append(parentStack[index].left)
            childStack.append(parentStack[index].right)
            if index == len(parentStack) - 1:
                parentStack = childStack
                childStack = []
                index = 0
            else:
                index += 1

    def fullBinTree(self):
        '''
        判断一棵二叉树是否是满二叉树
        :return: boolean，你懂得
        '''
        height = self.height()
        nodeCount = self.treeNodeCount()
        return nodeCount == 2 ** height - 1

class FINDBTree(BTree):
    '''
    二叉查找树类
    '''
    def __init__(self):
        super(FINDBTree,self).__init__()

    def find(self,val):
        '''
        在二叉树中查找是否有对应值的节点已经在其中
        :param val:
        :return:
        '''
        curNode = self.root
        while curNode:
            if curNode.val == val:
                return curNode
            if curNode.val < val:
                curNode = curNode.right
            else:
                curNode = curNode.left
        return None

    def insert(self,val):
        '''
        二叉查找树的插入节点方法
        :param val: 要插入的值，至少是可比较的数值
        :return: boolean，True表示插入成功，False表示插入失败，很郁闷，要不要返回个list；算了失败就失败吧
        '''
        node = self.root
        if not node:
            self.root = BTNode(val)
            return True
        while node:
            if node.val == val:
                return False
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = BTNode(val)
                    return True
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BTNode(val)
                    return True

    def delete(self,val):
        '''
        删除二叉查找树中的指定节点，
        :param val: 要删除的节点的值
        :return: boolean，成功则为True，失败则为False
        '''
        parent = None
        curNode = self.root
        while curNode:
            if curNode.val < val:
                parent = curNode
                curNode = curNode.right
            elif curNode.val > val:
                parent = curNode
                curNode = curNode.left
            else:
                if not curNode.left and not curNode.right:
                    if not parent:
                        self.root = None
                    else:
                        if curNode is parent.left:
                            parent.left = None
                        else:
                            parent.right = None
                elif not curNode.right:
                    if not parent:
                        self.root = curNode.left
                    else:
                        if curNode is parent.left:
                            parent.left = curNode.left
                        else:
                            parent.right = curNode.left
                else:
                    tempParent = curNode
                    temp = tempParent.right
                    while temp.left:
                        tempParent = temp
                        temp = temp.left
                    if tempParent is not curNode:
                        tempParent.left = temp.right
                        temp.left = curNode.left
                        temp.right = curNode.right
                    if not parent:
                        self.root = temp
                    else:
                        if curNode is parent.left:
                            parent.left = curNode
                        else:
                            parent.right = curNode

                return True
        return False


class AVLTreeNode(BTNode):
    def __init__(self,val,height = 1,left = None,right = None):
        super(AVLTreeNode,self).__init__(val,left,right)
        self.height = height #AVL树中节点的高度，最底层为1

'''AVL查找二叉树'''
class AVLTree(FINDBTree):
    def __init__(self):
        super(AVLTree,self).__init__()

    def insert(self,val):
        '''
        向AVL中插入节点，但是要禁止其随便设置左右子节点防止出问题
        :param val: 要插入的几点的值
        :return: boolean
        '''
        if not self.root:
            root = AVLTreeNode(val,1)
            self.root = root
            return True
        def dfs(node):
            if node.val == val:
                return node
            if node.val < val:
                pass


    def leftleft(self,grand,parent,child):
        childright = child.right
        grand.left = child
        child.right = parent
        parent.left = childright
        parent.height = max(self.nodeHeight(parent.left),self.nodeHeight(parent.right)) + 1
        child.height = max(self.nodeHeight(child.left),self.nodeHeight(child.right)) + 1


    def leftright(self,grand,parent,child):
        pass

    def rightleft(self):
        pass

    def rightright(self,grand,parent,child):
        childleft = child.left
        grand.right = child
        child.left = parent
        parent.right = childleft
        parent.height = max(self.nodeHeight(parent.left),self.nodeHeight(parent.right)) + 1
        child.height = max(self.nodeHeight(child.left),self.nodeHeight(child.right)) + 1

    def nodeHeight(self,node):
        if not node:
            return 0
        return node.height

if __name__ == '__main__':
    tree = FINDBTree()
    root = BTNode(5)
    tree.reset(root)
    left = BTNode(3)
    right = BTNode(7)
    root.left = left
    root.right = right
    leftleft = BTNode(4)
    leftright = BTNode(2)
    left.left = leftleft
    left.right = leftright
    rightleft = BTNode(9)
    rightright = BTNode(10)
    # right.left = rightleft
    right.right = rightright
    print(tree.emptyBTree())
    print(tree.fullBinTree())
    print(tree.totalBinTree())