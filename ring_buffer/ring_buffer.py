from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.length = 0

    def append(self, item):
        # Increment length

        # If full, overwrite oldest value and add new value to head
        if self.length == self.capacity:

            if self.current.next is not None:
                self.current.value = item
                self.current = self.current.next

            elif self.current.next is None:
                self.storage.tail.value = item
                self.current = self.storage.head

            
        # If not full, add value in 
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            self.length += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.length == 0:
            return []

        else:
            current = self.storage.head
            while current:
                list_buffer_contents.append(current.value)
                current = current.next
        # Append current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
