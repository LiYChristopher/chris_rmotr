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


class Node(object):

    def __init__(self, elem, link=None):
        self.elem = elem
        self.next = None

    def connect(self, elem):
        self.next = Node(elem)
        return


class LinkedList(object):

    def __init__(self, values=None):
        self.values = []
        if values is not None:
            self.__iadd__(values)
        self.start = self.values[0] if self.values else None
        self.end = self.values[-1] if self.values else None

    def update_start(self):
        self.start = self.values[0] if self.values else None
        return

    def update_end(self):
        self.end = self.values[-1] if self.values else None
        return

    def __str__(self):
        return str(self.values)

    def __add__(self, values):
        current_values = self.values[:]
        if len(values) < 2:
            current_values.append(Node(values[0]))
            self.update_start()
            self.update_end()
            return current_values
        else:
            pass
        return

    def __iadd__(self, values):
        if len(values) < 2:
            self.values.append(Node(values[0]))
        else:
            for val in values:
                if len(self.values) < 1:
                    print 'add first element', val
                    self.values.append(Node(val))
                    continue
                end_node = self.values[-1]
                end_node.connect(val)
                self.values.append(end_node.next)
                #self.values.append(cur_node.conn)
        self.update_start()
        self.update_end()
        return self

    def append(self, value):
        if not self.values:
            self.values.append(Node(value))
        else:
            end_node = self.values[-1]
            end_node.connect(value)
            self.values += end_node.next
        self.update_start()
        self.update_end()
        return self

    def pop(self):
        pass


l = LinkedList()
l.append(1)
m = LinkedList([1])
print l.start.elem
print l.start.next
print m.start.elem
print m.start.next
print l, m
#assert l == LinkedList([1])


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


    unittest.main()
