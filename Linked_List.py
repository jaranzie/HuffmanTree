class Linked_List:

    class __Node:
    
        def __init__(self, val):
            self.next = None
            self.prev = None
            self.__char = val
            if val is not None:
                self.charCode = ord(val)
            self.__freq = 1
        
        def increase_freq(self):
            self.__freq = self.__freq + 1
        
        def get_char(self):
            return self.__char

        def get_freq(self):
            return self.__freq

        def get_char_code(self):
            return self.__charCode

        def __gt__(self, other):
            if self.freq > other.freq: return True
            return False

        def __lt__(self, other):
            if self.freq < other.freq: return True
            return False

    def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__length = 0

    def pop(self):
        return self.remove_element_at(0)

    def __len__(self):
        return self.__length

    def insert_element(self, val):
        if self.__length == 0:
            self.append_element(val)
        else:
            temp = self.__header.next
            while temp is not self.__trailer:
                if val == temp.get_char():
                    temp.increase_freq()
                    return
                elif val < temp.get_char():
                    self.__length = self.__length + 1
                    newNode = Linked_List.__Node(val)
                    temp.prev.next = newNode
                    newNode.prev = temp.prev
                    newNode.next = temp
                    temp.prev = newNode
                    return
                temp = temp.next
            self.append_element(val)



    def append_element(self, val):
        self.__length = self.__length + 1
        newNode = Linked_List.__Node(val)
        newNode.next = self.__trailer
        newNode.prev = self.__trailer.prev
        self.__trailer.prev.next = newNode
        self.__trailer.prev = newNode

    def insert_element_at(self, val, index):
        if index >= self.__length or index < 0: raise IndexError
        self.__length = self.__length + 1
        newNode = Linked_List.__Node(val)
        if index <= self.__length / 2:
            temp = self.__header
            for i in range(index):
                temp = temp.next
            temp.next.prev = newNode
            newNode.next = temp.next
            newNode.prev = temp
            temp.next = newNode
        else:
            temp = self.__trailer
            for i in range(self.__length - index - 1):
                temp = temp.prev
            temp.prev.next = newNode
            newNode.prev = temp.prev
            newNode.next = temp
            temp.prev = newNode

    def remove_element_at(self, index):
        if index >= self.__length or index < 0: raise IndexError
        self.__length = self.__length - 1
        if index <= self.__length / 2:
            temp = self.__header
            for i in range(index):
                temp = temp.next
            temp2 = temp.next
            temp.next.prev = None
            temp.next = temp.next.next
            temp.next.prev.next = None
            temp.next.prev = temp
        else:
            temp = self.__trailer
            for i in range(self.__length - index):
                temp = temp.prev
            temp2 = temp.prev
            temp.prev.next = None
            temp.prev = temp.prev.prev
            temp.prev.next.prev = None
            temp.prev.next = temp
        return temp2
        
    def get_element_at(self, index):
        if index >= self.__length or index < 0: raise IndexError
        elif index <= self.__length / 2:
            temp = self.__header.next
            for i in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.__trailer.prev
            for i in range(self.__length - index):
                temp = temp.prev
            return temp

    def __str__(self):
        if self.__length == 0: return '[ ]'
        tempArr = [None] * self.__length
        tempNode = self.__header
        for i in range(self.__length):
            tempNode = tempNode.next
            tempArr[i] = str(tempNode.get_char()) + str(tempNode.get_freq())
        return '[ ' + ', '.join(tempArr) + ' ]'
        

    def __iter__(self):
        self.__tempIter = self.__header
        return self

    def __next__(self):
        self.__tempIter = self.__tempIter.next
        if self.__tempIter is self.__trailer: raise StopIteration
        else: return self.__tempIter.value        