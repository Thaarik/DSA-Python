class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node  # yield returns the function or value of node without breaking the local variable
            node = node.next

    # insertion function
    def insertSLL(self, value, location):
        # create a node to insert the value in the linkedlist
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #if the insertion is in head
                newNode.next = self.head
                self.head = newNode
            elif location == -1:#if the insertion is in tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:      #if the insertion is in between head and tail
                prevNode = self.head
                index = 0
                while index < location-1:
                    prevNode = prevNode.next
                    index += 1
                nextNode = prevNode.next
                prevNode.next = newNode
                newNode.next = nextNode
                if prevNode == self.tail: #if the linkedlist contains only single node which acts as both head and tail
                    self.tail = newNode

singleLinkedList = SLinkedList();
singleLinkedList.insertSLL(1,1)
singleLinkedList.insertSLL(4,0)


print([node.value for node in singleLinkedList])
