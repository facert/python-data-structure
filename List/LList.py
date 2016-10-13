# coding: utf-8

from LNode import LNode
from Exceptions import LinkedListUnderflow


class LList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return not self._head

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if not self._head:
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if not self._head:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if not self._head:  # 空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head

        if not p.next:  # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print p.elem
            p = p.next

    def elements(self):
        p = self._head
        while p:
            yield p.elem
            p = p.next

    # def insert(self, i, elem):
    #     if i < 0:
    #         raise LinkedListUnderflow('in insert')
    #     p = self._head
    #     q = LNode(elem)
    #     if not p:
    #         # 如果是空表
    #         self._head = q
    #         return

    #     if i == 0:
    #         q.next = p.next
    #         p = q
    #         return

    #     while p and i > 0:
    #         i -= 1
    #         print p
    #         p = p.next
    #     print p

    #     q.next = p.next
    #     p.next = q

    def clear(self):
        self._head = None


if __name__ == '__main__':
    llist = LList()
    if llist.is_empty():
        print 'llist is empty'
    llist.prepend(1)
    # print llist.pop()

    llist.append(2)
    # print llist.pop_last()

    llist.append(3)
    print llist.find(lambda a: a == 3)
    llist.pop()

    for i in xrange(10):
        llist.append(i)
    for i in xrange(10):
        llist.prepend(i)
    # llist.printall()

    for x in llist.elements():
        print x

    llist.clear()

    llist.insert(0, 99)
    llist.printall()

    llist.insert(1, 100)

    llist.printall()
