class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return 'Node{!r}'.format(self.data)

class LinkedList(object):
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
        
    def delete(self, item):
        node = self.head
        prev_node = None
        found = False

        while not found and node is not None:
            if node.data == item:
                found = True
            else:
                prev_node = node
                node = node.next
                
        if found:
            if node is not self.head and node is not self.tail:
                print("here")
                prev_node.next = node.next
                node.next = None
            if node is self.head:
                self.head = node.next
                node.next = None
            if node is self.tail:
                if prev_node is not None:
                    prev_node.next = None
                self.tail = prev_node
            self.size -= 1
        else:
            raise ValueError(f"oops didn't seem to find the item: {item}")


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(8)
    ll.append(3)
    ll.append(4)
    ll.append(6)
    print(ll)
    ll.delete(3)
    print(ll)