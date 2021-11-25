class Tree:

  def __init__(self, char, freq):
    self.__char = char
    self.__freq = freq
    self.left_child = None
    self.right_child = None

  def get_char(self):
    return self.__char

  def get_freq(self):
    return self.__freq

  @classmethod
  def from_linked_list_node(cls, node):
    return cls(node.get_char(), node.get_freq())

  def __eq__(self,other):
    if self.__freq == other.__freq:
      return True
    return False

  def __gt__(self, other):
    if self.__freq > other.__freq: return True
    return False

  def __lt__(self, other):
    if self.__freq < other.__freq: return True
    return False

  @staticmethod
  def join_trees(tree1, tree2):
    newTree = Tree(None, tree1.__freq + tree2.__freq)
    newTree.left_child = tree1
    newTree.right_child = tree2
    return newTree
  
  def in_order(self):
    return '[ ' + Tree.__rec_in_order(self) + ' ]'
  
  @staticmethod
  def __rec_in_order(head):
    if head.left_child is None and head.right_child is None:
      return str(head)
    if head.left_child is None:
      return str(head) + ', ' + Tree.__rec_in_order(head.right_child)
    if head.right_child is None:
      return Tree.__rec_in_order(head.left_child) + ', ' + str(head)
    return Tree.__rec_in_order(head.left_child)  + ', ' + str(head) + ', ' + Tree.__rec_in_order(head.right_child)
