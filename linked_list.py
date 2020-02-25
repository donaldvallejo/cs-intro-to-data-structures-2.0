class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node{!r}'.format(self.data)

class linked_list(object):
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'linkedList{!r}'.format(self.items())

    def items(self):
        items = []
        node = self.head

        while node is not None: 
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size

    def append(self, item):
        """ creates from item, check if empty if so add to head and tail if not we add to the linked list """
        node = Node(item)
        self.size += 1
        
        if self.is_empty():
            self.head = node
            self.tail = node
            return

        tail_node = self.tail
        tail_node.next = node
        self.tail = node

    def prepend(self, item):
        node = Node(item)
        self.size += 1
        
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            current_node = self.head
            self.head = node
            node.next = current_node

    def find(self, quality):
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None
        