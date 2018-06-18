class Node(object):

    def __init__(self, value=None, next=None): # Узел

        self.value = value
        self.next = next

class LinkedList(object):

    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.lenght = 0
        self.counter = -1

        for a in args:
            self.add(a)

    def __str__(self):
        if self.head != None:
            current = self.head
            out = 'LinkedList(' +str(current.value)
            while current.next != None:
                current = current.next
                out += ', ' + str(current.value)
            return out + ')'
        return 'LinkedList()'

    def add(self, value):
        self.lenght += 1
        if self.head == None:
            self.tail = self.head = Node(value, None)
        else:
            self.tail.next = self.tail = Node(value, None)

    def insert(self, index, value):
        counter = 0
        pointer = self.head

        if index >= self.lenght:
            self.add(value)
            return

        if index == 0:
            self.lenght += 1
            if self.head == None:
                self.head = Node(value, None)
                self.tail = self.head
                return
            else:
                self.head = Node(value, self.head)
                return

        while pointer != None:
            counter += 1
            if counter  == index:
                self.lenght += 1
                pointer.next = Node(value, pointer.next)
                if pointer.next.next is None:
                    self.last = pointer.next
                    self.lenght += 1
                return
            pointer = pointer.next
        return

    def get(self, index):
        if index >= self.lenght:
            raise IndexError
        counter = 0
        pointer = self.head

        while pointer != None:
            if counter == index:
                return pointer.value
            counter += 1
            pointer = pointer.next


    def remove(self, value):
        pointer = self.head
        while pointer != None:

            if pointer.value == value:
                if pointer.next == None:
                    self.remove_at(self.lenght - 1)
                    return

                pointer.value = pointer.next.value
                pointer.next = pointer.next.next
                self.lenght -= 1
                return
            pointer = pointer.next


    def remove_at(self, index):
        pointer = self.head
        counter = -1


        if self.lenght <= index:
            raise IndexError

        if index == 0:
            cache = self.head.value
            self.lenght -= 1
            self.head = pointer.next
            return cache

        while pointer:
            counter += 1
            if counter + 1 == index:
                cache = pointer.next.value
                pointer.next = pointer.next.next
                self.lenght -= 1
                return cache
            pointer = pointer.next

    def clear(self):
        while self.lenght != 0:
            self.remove_at(0)

    def contains(self, value):
        pointer = self.head
        counter = 0
        while pointer:
            if pointer.value == value:
                return True
            pointer = pointer.next
            counter += 1
        return False

    def len(self):
        return self.lenght

    def is_empty(self):
        if self.lenght == 0:
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < self.lenght:
            return self.get(self.counter)
        else:
            raise StopIteration


#ll = LinkedList(1, 2, 3, 4)
#ll.add('Hello')
#print(ll.contains(2))
#print(ll.len())
#print(ll.is_empty())
#ll.insert(2, 'k')
#ll.insert(100, 99)
#print(ll)
#ll.remove(2)
#print(ll.get(3))
#print(ll)
#ll.remove_at(3)
#print(ll)
#ll.clear()
#print(ll.is_empty())
#ll2 = LinkedList('item1', 'item2', 'item3')
#for item in ll2:
#    print(item)
