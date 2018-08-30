# 遍历二叉树
"""

给定一个数组，构建二叉树，并且按层次打印这个二叉树
"""


class Node(object):
    """ 二叉树节点 """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree():
    """
             1           1
            / \         / \
           3   2       3   2
          /\  /\      /\  /\
         7 6 5 4     7 6 5 4
        /           / / \
       0           0 -1 -2
    :return:
    """
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    return tree


# TODO 需要全部验证是否正确
def lookup(root):
    """ 层次遍历
    
    [1]  [3, 2]  [7, 6, 5, 4]  [0]
    按层遍历 """
    row = [root]
    while row:
        print([item.data for item in row])
        row = [kid for item in row for kid in (item.left, item.right) if kid]


def deep(root):
    """ 深度遍历

     [1, 3, 7, 0]  [6]  [2, 5]  [4]
     """
    if not root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)


def inorder_travelsal(root):
    """ 中序遍历
    
    [0, 7, 3]  [6]  [1]  [5, 2]  [4]
     遍历左子树,访问当前节点,遍历右子树 """
    if root.left is not None:
        inorder_travelsal(root.left)
        # 访问当前节点
    print(root.data)
    if root.right is not None:
        inorder_travelsal(root.right)


def preorder_travelsal(root):
    """ 前序遍历
    1, 3, 7, 0, 6, 2, 5,4
    前序遍历方式为： 访问当前节点 -> 遍历左子树 -> 遍历右子树
    """
    print(root.data)
    if root.left is not None:
        preorder_travelsal(root.left)
    if root.right is not None:
        preorder_travelsal(root.right)


def postorder_trvelsal(root):
    """ 后序遍历
    0, 7, 6, 3, 5, 4, 2, 1
    后序遍历方式为： 遍历左子树 -> 遍历右子树 -> 访问当前节点
    """
    if root.left is not None:
        postorder_trvelsal(root.left)
    if root.right is not None:
        postorder_trvelsal(root.right)
    print(root.data)


def maxDepth(root):
    """ 求最大树深 """
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def isSameTree(p, q):
    """ 求2颗树是否相同 """
    if p is None and q is None:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False


def rebuild(pre, center):
    """ 前序中序求后序
     https://blog.csdn.net/hinyunsin/article/details/6315502
     
    前序遍历方式为：根节点->左子树->右子树
    中序遍历方式为：左子树->根节点->右子树
    后序遍历方式为：左子树->右子树->根节点

从这里可以看出，前序遍历的第一个值就是根节点，然后再中序遍历中找到这个值，那么这个值的左边部分即为当前二叉树的左子树部分前序遍历结果，
这个值的右边部分即为当前二叉树的右子树部分前序遍历结果。
     """
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur


if __name__ == '__main__':
    # lookup(tree())
    
    # deep(tree())
    """
             1
            / \
           3   2
          /\  /\
         7 6 5 4
        / / \
       0 -1 -2
    """
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6, Node(-1), Node(-2))), Node(2, Node(5), Node(4)))
    inorder_travelsal(tree)  # 0,7,3,-1,6,-2,1,5,2,4

    preorder_travelsal(tree)  # 1,3,7,0,6-1-2,2,5,4
    
    postorder_trvelsal(tree)  # 0,7,-1,-2,6,3,5,4,2,1

