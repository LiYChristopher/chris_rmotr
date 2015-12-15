"""
A Linked List (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure.
You can think of it as an implementation of a regular Python List.

Using Object Oriented programming, build a simple Linked List that
shares the same interface with Python Lists:

    l = LinkedList()

    l.append(2)
    l.count()  # Should return 1

    l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
    l += [3, 4]   # Should return None and append [3, 4] to the original list

    l.pop(0)       # Should remove and return the first element.

    # Important. This should be True:
    LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])

To ease your task, a LinkedList is constructed using different Nodes.
Each node has a reference to other Node, what makes it
a recursive class, it'll point to itself.

"""
from copy import copy, deepcopy


class Node(object):

    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

    def __eq__(self, other):
        return (self.elem, self.next == other.elem, self.next)


class LinkedList(object):

    def __init__(self, values=None):
        self.start = None
        self.end = None
        if values is not None:
            self.start = Node()
            self.link(self.start, values)

    def __str__(self):
        if type(self.start) is Node:
            start = self.start.elem
        else:
            start = None
        if type(self.end) is Node:
            end = self.end.elem
        else:
            end = None
        return "LinkedList-Start {0}, End {1}, Length {2}".format(start, end, self.count())

    def __add__(self, values):
        print values.display_chain()
        if self.start is None:
            self.start = values.start
            self.end = self.start
        elif self.start.next is None:
            self.start.next = values.start
            self.end = self.start.next
        elif self.end.next is None:
            self.end.next = values.start
        return self.display_chain()

    def __iadd__(self, values):
        return self

    def __getitem__(self, index):
        if index < 0:
            index = self.count() + index
        current_node = self.start
        for i in xrange(0, index + 1):
            if i == index:
                return current_node
            current_node = current_node.next

    def link(self, current_node, values):
        if len(values) == 0:
            self.start = None
        elif len(values) == 1:
            if self.start.elem is None:
                self.start = Node(values[0])
            else:
                self.end = Node(values[0])
        else:
            current_node.elem, next_elem = values[0], values[1]
            current_node.next = Node(next_elem)
            return self.link(current_node.next, values[values.index(next_elem):])
        return

    def display_chain(self):
        chain = []
        cur_elem = self.start
        if cur_elem is None:
            return chain
        chain.append(cur_elem.elem)
        while cur_elem != self.end:
            if cur_elem.next is None:
                return chain
            cur_elem = cur_elem.next
            chain.append(cur_elem.elem)
        return chain

    def count(self):
        if self.start is None:
            return 0
        count = 1
        cur_elem = self.start
        while cur_elem != self.end:
            if cur_elem.next is None:
                return count
            cur_elem = cur_elem.next
            count += 1
        return count

    def append(self, value):
        if self.start is None:
            self.start = Node(value)
            self.end = self.start
        elif self.start.next is None:
            self.start.next = Node(value)
            self.end = self.start.next
        elif self.end.next is None:
            #print 'Running .. (sen is None)'
            current_end = self.__getitem__(-1)
            print 'current end', current_end.elem
            current_end.next = Node(value)
            print 'new end', self.__getitem__(-1).elem
            self.end = current_end.next
        return

    def __eq__(self, other):
        return (self.display_chain() == other.display_chain())

    def pop(self, index=-1):
        # raise errors
        if self.count() == 0:
            raise IndexError('No elements to pop.')
        elif index >= self.count():
            raise IndexError('Index out-of-range')

        # operations
        if index == 0:
            popped = self.start.elem
            self.start = self[(index + 1)]
        elif 0 < index < self.count() - 1:
            popped = self[(index)].elem
            self[(index - 1)].next = self[(index + 1)]
        else:
            popped = self[(index)].elem
            if self.count() == 1:
                self.start = None
            else:
                self[(index - 1)].next = None
        return popped


m = LinkedList([1])
l = LinkedList([2, 3])
print 'add', m + l
print 'm -', m.display_chain()
print 'l -', l.display_chain()


if __name__ == '__main__':

    import unittest

    class LinkedListTestCase(unittest.TestCase):
        ListImplementationClass = LinkedList

        def test_creation_and_equal(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            self.assertTrue(l1.start is not None)
            self.assertEqual(l1.start.elem, 1)

            self.assertTrue(l1.end is not None)
            self.assertEqual(l1.end.elem, 3)

            self.assertTrue(l1.start.next is not None)
            self.assertEqual(l1.start.next.elem, 2)

            self.assertTrue(l1.start.next.next is not None)
            self.assertEqual(l1.start.next.next.elem, 3)


        def test_append(self):
            my_list = self.ListImplementationClass()

            my_list.append(1)
            self.assertEqual(my_list.start.elem, 1)
            self.assertEqual(my_list.start.next, None)
            self.assertEqual(my_list, self.ListImplementationClass([1]))

            my_list.append(2)
            self.assertEqual(my_list.start.elem, 1)
            self.assertEqual(my_list.start.next, Node(2))
            self.assertEqual(my_list.start.next.elem, 2)
            self.assertEqual(my_list.start.next.next, None)

            self.assertEqual(my_list.count(), 2)

        def test_count(self):
            self.assertEqual(self.ListImplementationClass([1, 2, 3]).count(), 3)

        def test_pop_removes_last_item_by_default(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop()
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([1, 2]))

        def test_pop_removes_first_item(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop(0)
            self.assertEqual(elem, 1)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([2, 3]))

        def test_pop_removes_last_item(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop(2)
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([1, 2]))

        def test_pop_removes_item_in_the_middle_of_the_list(self):
            l1 = self.ListImplementationClass([1, 2, 3, 4, 5])

            elem = l1.pop(2)
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 4)
            self.assertEqual(l1, self.ListImplementationClass([1, 2, 4, 5]))

            elem = l1.pop(1)
            self.assertEqual(elem, 2)
            self.assertEqual(l1.count(), 3)
            self.assertEqual(l1, self.ListImplementationClass([1, 4, 5]))

        def test_pop_with_a_single_element_list(self):
            # Default index
            l1 = self.ListImplementationClass([9])

            elem = l1.pop()
            self.assertEqual(elem, 9)
            self.assertEqual(l1.count(), 0)
            self.assertEqual(l1, self.ListImplementationClass([]))

            # index == 0
            l1 = self.ListImplementationClass([9])

            elem = l1.pop(0)
            self.assertEqual(elem, 9)
            self.assertEqual(l1.count(), 0)
            self.assertEqual(l1, self.ListImplementationClass([]))

        def test_pop_raises_an_exception_with_empty_list(self):
            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop()

            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop(0)

            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop(3)

        def test_pop_raises_an_exception_with_invalid_index(self):
            with self.assertRaises(IndexError):
                self.ListImplementationClass([1]).pop(1)

            with self.assertRaises(IndexError):
                self.ListImplementationClass([1, 2, 3]).pop(3)

        def test_equals(self):
            self.assertEqual(
                self.ListImplementationClass([1, 2, 3]),
                self.ListImplementationClass([1, 2, 3]))

            self.assertEqual(
                self.ListImplementationClass([]),
                self.ListImplementationClass([]))

            self.assertEqual(
                self.ListImplementationClass([1]),
                self.ListImplementationClass([1]))

            self.assertNotEqual(
                self.ListImplementationClass([1, 2]),
                self.ListImplementationClass([1, 2, 3]))

            self.assertNotEqual(
                self.ListImplementationClass([1]),
                self.ListImplementationClass([]))

    #unittest.main()
