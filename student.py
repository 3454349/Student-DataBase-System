from demo import *
from LinkList import LinkList
class Node:
    def __init__(self, xm, xb,xh ,sr , img, next):
        self.xm = xm
        self.xb = xb
        self.xh = xh
        self.sr = sr
        self.img = img
        self.next = next

    # ⾃定义异常类，继承Exception
class ShortInputError(Exception):
    def __str__(self):
        return '位置不合法'

class Student:
    def __init__(self):
        self.N = 0
        self.head = Node( None, None,None ,None ,None , None)

    # 清空链表
    def clear(self):
        self.head.next = None
        self.N = 0

    # 判断链表是否为空
    def isEmpty(self):
        return self.N == 0

    # 获取链表中元素的个数
    def length(self):
        return self.N

    # # 获取指定位置的元素
    # def get(self, i):
    #     if i < 0 | i > self.N:
    #         raise ShortInputError()
    #     n = self.head
    #     index = 0
    #     while index < i:
    #         n = n.next
    #         index = index + 1
    #     n = n.next
    #     return n.item

    # 往链表中添加第一个元素
    # def insert(self, xm, xb, xh, sr):
    #     n = self.head
    #     while n.next != None:
    #         n = n.next
    #     newNode = Node(xm, xb, xh ,sr , None)
    #     n.next = newNode
    #     self.N = self.N + 1

    # 向指定位置处添加元素
    def insert(self, i, xm, xb, xh, sr, img):
        i = int(i)
        if i < 0 or i > self.N:
            raise ShortInputError()
        # 寻找i位置之前的节点
        pre = self.head
        index = 0
        while index < i:
            pre = pre.next
            index = index + 1
        curr = pre.next
        newNode = Node( xm, xb,xh ,sr , img, curr)
        pre.next = newNode
        self.N = self.N + 1

    # 删除并返回链表中第i个数据元素
    def remove(self, i):
        if i < 0 | i > self.N:
            raise ShortInputError()
        index = 0
        pre = self.head
        while index < i - 1:
            pre = pre.next
            index = index + 1
        curr = pre.next
        pre.next = curr.next
        self.N = self.N - 1

    # 查找元素t在链表中第一次出现的位置
    def indexOf(self, xm):
        n = self.head.next
        i = 0
        if n.xm == xm:
            return [n.xm, n.xh, n.sr, n.xb , n.img]
        while n.xm != xm:
            n = n.next

            if n.xm == xm:
                return [n.xm, n.xh, n.sr, n.xb ,n.img]
            i = i + 1
        return -1





