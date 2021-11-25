class Heap:

    def __init__(self, entries):
        self.__heap = [None] * entries
        self.__back = None

    def __str__(self):
        arr = [None] * len(self.__heap)
        for i in range(len(self.__heap)):
            arr[i] = str(self.__heap[i])
        return ', '.join(arr)

    def get_array(self):
        return self.__heap
        
    
    def insert(self, val):
        if self.__back is None:
            self.__heap[0] = val
            self.__back = 0
        else:
            self.__back = self.__back + 1
            self.__heap[self.__back] = val
        if self.__heap[(self.__back - 1) // 2] is not None and self.__heap[self.__back] < self.__heap[(self.__back - 1) // 2]:
            self.swap_up()

    def pop(self):
        if self.__back == 0:
            self.__back = None
            return self.__heap[0]
        self.__back = self.__back - 1
        returnVal = self.__heap[0]
        self.__heap[0] = self.__heap[self.__back + 1]
        self.__heap[self.__back + 1] = None
        self.swap_down(0)
        return returnVal

    def get_back(self):
        return self.__back

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child(self, index):
        if (index * 2 + 1) > self.__back:
            return None
        return self.__heap[index * 2 + 1]

    def get_right_child(self, index):
        if (index * 2 + 2) > self.__back:
            return None
        return self.__heap[index * 2 + 2]

    def get_right_child_index(self, index):
        return index * 2 + 2

    def get_left_child_index(self, index):
        return index * 2 + 1

    def swap_left_child(self, index):
        temp = self.__heap[index]
        self.__heap[index] = self.__heap[index * 2 + 1]
        self.__heap[index * 2 + 1] = temp

    def swap_right_child(self, index):
        temp = self.__heap[index]
        self.__heap[index] = self.__heap[index * 2 + 2]
        self.__heap[index * 2 + 2] = temp
    
    def get_val(self, index):
        return self.__heap[index]

    def swap_parent(self, index):
      temp = self.__heap[index]
      self.__heap[index] = self.__heap[(index - 1) // 2]
      self.__heap[(index - 1) // 2] = temp

    def swap_up(self):
        index = self.__back
        while index != 0 and self.__heap[index] < self.__heap[(index - 1) // 2]:
            self.swap_parent(index)
            index = self.get_parent_index(index)
    
    def swap_down(self, index):
        if self.get_right_child(index) is None and self.get_left_child(index) is None:
            return
        elif self.get_right_child(index) is not None and self.get_left_child(index) is not None and self.get_left_child(index) == self.get_right_child(index) and self.get_left_child(index) < self.get_val(index):
            self.swap_left_child(index)
            self.swap_down(self.get_left_child_index(index))
        elif self.get_right_child(index) is None and self.get_left_child(index) is not None  and self.get_left_child(index) < self.get_val(index):
            self.swap_left_child(index)
            self.swap_down(self.get_left_child_index(index))
        elif self.get_right_child(index) is not None and self.get_left_child(index) is None  and self.get_right_child(index) < self.get_val(index):
            self.swap_right_child(index)
            self.swap_down(self.get_right_child_index(index))
        elif self.get_right_child(index) is not None and self.get_left_child(index) is not None and self.get_left_child(index) < self.get_right_child(index) and self.get_left_child(index) < self.get_val(index):
            self.swap_left_child(index)
            self.swap_down(self.get_left_child_index(index))
        elif self.get_right_child(index) is not None and self.get_left_child(index) is not None and self.get_left_child(index) > self.get_right_child(index) and self.get_right_child(index) < self.get_val(index):
            self.swap_right_child(index)
            self.swap_down(self.get_right_child_index(index))



        



