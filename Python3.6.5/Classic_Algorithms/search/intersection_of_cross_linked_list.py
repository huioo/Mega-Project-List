#  交叉链表求交点

"""
其实思想可以按照从尾开始比较两个链表，如果相交，则从尾开始必然一致，
只要从尾开始比较，直至不一致的地方即为交叉点，如图所示

https://github.com/taizilongxu/interview_python#8-%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E5%88%97%E8%A1%A8
"""


def func1():
    # 使用a,b两个list来模拟链表，可以看出交叉点是 7这个节点
    a = [1, 2, 3, 7, 9, 1, 5]
    b = [4, 5, 7, 9, 1, 5]
    
    for i in range(1, min(len(a), len(b))):
        if i == 1 and (a[-1] != b[-1]):
            print("No")
            break
        else:
            if a[-i] != b[-i]:
                print("交叉节点：", a[-i + 1])
                break
            else:
                pass


# 另外一种比较正规的方法，构造链表类
class ListNode:
    # TODO: 完善__iter__()、__next__()
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __len__(self):
        length = 1
        current_node = self
        while current_node.next:
            current_node = current_node.next
            length += 1
        return length


def gen_linked_list_nodes(l):
    result = []
    length = len(l)
    for _ in range(length):
        node = ListNode(l[_])
        if _ > 0:
            result[_-1].next = node
        result.append(node)
    return result


def gen_cross_linked_list(iter1, iter2):
    """ 2个列表的最后几个元素相同 """
    iter1.reverse()
    iter2.reverse()
    result1, result2 = [], []
    length = min(len(iter1), len(iter2))
    for i in range(length):
        if iter1[i] == iter2[i]:
            node1 = node2 = ListNode(iter1[i])
        else:
            node1 = ListNode(iter1[i])
            node2 = ListNode(iter2[i])
        
        if i > 0:
            node1.next = result1[i - 1]
            node2.next = result2[i - 1]
        
        result1.append(node1)
        result2.append(node2)
    
    if len(iter1) != length:
        for i in range(length, len(iter1)):
            node1 = ListNode(iter1[i])
            node1.next = result1[i - 1]
            result1.append(node1)
    if len(iter2) != length:
        for i in range(length, len(iter2)):
            node2 = ListNode(iter2[i])
            node2.next = result2[i - 1]
            result2.append(node1)

    return result1, result2


def intersecting_node(l1, l2):
    # 求两个链表长度
    length1, length2 = len(l1), len(l2)
    # 求链表结点列表
    l1_nodes, l2_nodes = gen_cross_linked_list(l1, l2)
    l1_node = l1_nodes[-1]
    l2_node = l2_nodes[-1]
    # 长的链表先走
    if length1 > length2:
        for _ in range(length1 - length2):
            l1_node = l1_node.next
    else:
        for _ in range(length2 - length1):
            l2_node = l2_node.next
    while l1_node and l2_node:
        print(l1_node.val, l2_node.val)

        if l1_node.next == l2_node.next:
            return l1_node.next
        else:
            l1_node = l1_node.next
            l2_node = l2_node.next


def test_gen_cross_linked_list(l1, l2):
    a = gen_cross_linked_list(l1, l2)[0]
    print(a.val)
    while a.next:
        print(a.next.val)
        a = a.next


if __name__ == '__main__':
    l1 = [1, 2, 3, 7, 9, 1, 5]
    l2 = [   4, 5, 7, 9, 1, 5]

    print(intersecting_node(l1, l2))
    
    
    


