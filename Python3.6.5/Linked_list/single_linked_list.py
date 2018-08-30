# 单链表逆置
"""

https://github.com/taizilongxu/interview_python#21-%E5%8D%95%E9%93%BE%E8%A1%A8%E9%80%86%E7%BD%AE
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


node_1st = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))


def rev(link):
    """ 单链表逆置
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
    """
    pre = link  # 1
    cur = link.next  # 2
    pre.next = None  # 断开链接: 1,  2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
    while cur:
        tmp = cur.next  # 第一次循环为3
        cur.next = pre  # 第一次循环，2的next指向1，即 2 -> 1, 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
        pre = cur       # 第一次循环，替换pre为2，cur为3
        cur = tmp
    return pre


if __name__ == '__main__':
    root = rev(node_1st)
    while root:
        print(root.data)
        root = root.next
