from Linked_List import Linked_List
from Heap import Heap
from Tree import Tree

class Huffman_Tree:

    class Encoded_Chr:

        def __init__(self, char, code):
            self.__char = char
            self.__code = code
        
        def __str__(self):
            return self.__char + ' ' + self.__code

        def get_char(self):
            return self.__char

        def get_code(self):
            return self.__code

    def __init__(self, string):
        charList = Linked_List()
        self.__char_arr = list(string)
        for i in range(len(self.__char_arr)):
            charList.insert_element(self.__char_arr[i])
        self.__heap = Heap(len(charList))
        self.__encoded_array = [None] * len(charList)
        while len(charList) != 0:
            self.__heap.insert(Tree.from_linked_list_node(charList.pop()))
        
        while self.__heap.get_back() > 1:
            tree1 = self.__heap.pop()
            tree2 = self.__heap.pop()
            self.__heap.insert(Tree.join_trees(tree1, tree2))
        tree1 = self.__heap.pop()
        tree2 = self.__heap.pop()
        self.__tree = Tree.join_trees(tree1, tree2)
        self.__count = 0
        self.__str = ''
        self.__rec_encode(self.__tree, self.__encoded_array)

        self.__encoded_string = self.encode_string()
        

    def remove_last_char(self):
        arr = list(self.__str)
        tempArr = [None] * (len(arr) - 1)
        for i in range((len(arr) - 1)):
            tempArr[i] = arr[i]
        self.__str = ''.join(tempArr)

    def __rec_encode(self, head, arr):
        if head.left_child is None and head.right_child is None:
            arr[self.__count] = Huffman_Tree.Encoded_Chr(head.get_char(), self.__str)
            self.__count = self.__count + 1
            self.remove_last_char()
        elif head.right_child is not None and head.left_child is not None:
            self.__str = self.__str + '0'
            self.__rec_encode(head.left_child, arr)
            self.__str = self.__str + '1'
            self.__rec_encode(head.right_child, arr)
            self.remove_last_char()
        elif head.left_child is not None:
            self.__str = self.__str + '1'
            self.__rec_encode(head.right_child, arr)
        elif head.right_child is not None:
            self.__str = self.__str + '0'
            self.__rec_encode(head.left_child, arr)
        

    def get_array(self):
        return self.__encoded_array

    
    def get_char_code(self, char):
        for val in self.__encoded_array:
            if val.get_char() == char:
                return val.get_code()

    def encode_string(self):
        encoded_arr = [None] * len(self.__char_arr)
        for i in range(len(self.__char_arr)):
            encoded_arr[i] = self.get_char_code(self.__char_arr[i])
        return ''.join(encoded_arr)

    def get_encoded_string(self):
        return self.__encoded_string

    def get_decoded_string(self):
        str = input('Enter a binary string you\'d like to decode: ')
        i = 2
        decode_str = ''
        while len(str) > 1:
            subString = str[0:i]
            for val in self.__encoded_array:
                if subString == val.get_code():
                    str = str[i:]
                    i = 0
                    decode_str = decode_str + val.get_char()
            i = i + 1
        return decode_str
        
if __name__ == '__main__':
    str = input('Enter the string you\'d like to encode: ')
    tree = Huffman_Tree(str)
    print(tree.get_encoded_string())
    print(tree.get_decoded_string())


    


        
