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

    def insertBeforeIndex(self, i, elem):
        if i < 0:
            raise LinkedListUnderflow('in insert before index')
        # if not self._head:
        #     self._head = LNode(elem)
        #     return
        p = self._head
        if i == 0:
            self._head = LNode(elem, self._head)
            return

        currentIndex = 0
        while p:
            if (currentIndex + 1) == i:
                p.next = LNode(elem, p.next)
                return
            currentIndex += 1
            p = p.next

    def insertAfterIndex(self, i, elem):
        if i < 0:
            raise LinkedListUnderflow('in insert after index')
        if i == 0:
            self._head = LNode(elem, self._head)
            return
        p = self._head
        currentIndex = 0
        while p:
            if currentIndex == i:
                p.next = LNode(elem, p.next)
                return
            p = p.next
            currentIndex += 1

    def deleteData(self, data):
        p = self._head
        if self._head.elem == data:
            self._head = self._head.next
            p.next = None
            print p.elem
            return
        while p.next:
            if p.next.elem == data:
                print p.next.elem
                p.next = p.next.next
                return
            p = p.next

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
    # print llist.find(lambda a: a == 3)
    llist.pop()

    for i in xrange(10):
        llist.append(i)
    for i in xrange(10):
        llist.prepend(i)
    # llist.printall()

    # for x in llist.elements():
    #     print x

    llist.clear()

    llist.insertBeforeIndex(0, 99)
    # llist.printall()

    llist.insertBeforeIndex(0, 100)

    # llist.printall()

    llist.clear()
    llist.insertAfterIndex(0, 2)
    llist.insertAfterIndex(0, 3)
    llist.insertAfterIndex(1, 4)
    llist.printall()
    llist.deleteData(3)
    llist.printall()
