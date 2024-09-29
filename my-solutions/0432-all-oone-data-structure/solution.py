class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()  # Store keys with this count
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        # Maps keys to their counts
        self.key_count = {}
        # Maps counts to their nodes in the doubly linked list
        self.count_node = {}
        # Sentinel head and tail nodes for the doubly linked list
        self.head = Node(float('-inf'))  # Sentinel head
        self.tail = Node(float('inf'))    # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        # Remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def _add_node_after(self, new_node, prev_node):
        # Add a new node after prev_node in the doubly linked list
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.count_node[new_node.count] = new_node

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        count = self.key_count.get(key, 0)
        new_count = count + 1
        self.key_count[key] = new_count
        
        # Update linked list
        if count > 0:
            # Remove key from the current count node
            current_node = self.count_node[count]
            current_node.keys.remove(key)
            if not current_node.keys:  # If no keys left, remove the node
                self._remove_node(current_node)

        # Add key to the new count node
        if new_count not in self.count_node:
            # Create new node for the new count
            new_node = Node(new_count)
            # Insert it into the linked list
            prev_node = self.head
            while prev_node.next.count < new_count:
                prev_node = prev_node.next
            self._add_node_after(new_node, prev_node)
        
        self.count_node[new_count].keys.add(key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        count = self.key_count[key]
        new_count = count - 1
        
        # Remove key from the current count node
        current_node = self.count_node[count]
        current_node.keys.remove(key)
        
        if not current_node.keys:  # If no keys left, remove the node
            self._remove_node(current_node)
        
        if new_count > 0:
            self.key_count[key] = new_count
            # Add key to the new count node
            if new_count not in self.count_node:
                new_node = Node(new_count)
                # Insert it into the linked list
                prev_node = self.head
                while prev_node.next.count < new_count:
                    prev_node = prev_node.next
                self._add_node_after(new_node, prev_node)
            self.count_node[new_count].keys.add(key)
        else:
            del self.key_count[key]

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

