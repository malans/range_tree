class BSTNode(object):
  """A node in a BST tree."""
  
  def __init__(self, key):
    """Creates a binary search tree node.
    
    Should be inserted into a tree by calling BST.insert()
    
    Args:
      key: the key associated with the node
    """
    self.key = key
    self.parent = None
    self.left = None
    self.right = None
      
  def find(self, key):
    """The node with the given key in the subtree rooted at this node.
    
    Args:
      key: the key of the node to be returned
    
    Returns a BSTNode instance with the given key, or None if the key was not
    found.
    """
    if key < self.key:
      return self.left and self.left.find(key)
    elif key > self.key:
      return self.right and self.right.find(key)
    return self
  
  def min(self):
    """The node with the minimum key in the subtree rooted at this node.
    
    Returns a BSTNode instance with the minimum key.
    """
    if self.left is None:
      return self
    return self.left.min()
     
  def successor(self):
    """The node with the next larger key (the successor) in the BST.
    
    Returns a BSTNode instance, or None if this node has no successor.
    """
    if self.right is not None:
      return self.right.min()
    current = self
    while current.parent is not None and current is current.parent.right:
      current = current.parent
    return current.parent

  def insert(self, node):
    """Inserts a node into the subtree rooted at this node.
    
    Args:
      node: the node to be inserted
      
    Returns the node argument, if the node was inserted in the tree. If a node
    with the same key was found, that node is returned instead.
    """
    if node.key < self.key:
      if self.left is not None:
        return self.left.insert(node)
      node.parent = self
      self.left = node
      return node
    elif node.key > self.key:
      if self.right is not None:
        return self.right.insert(node)
      node.parent = self
      self.right = node
      return node
    return self

  def delete(self):
    """Deletes this node from the BST.
    
    Returns the deleted BSTNode instance. The instance might be different from
    this node, but will have this node's key. The deleted node's fields will
    still be set, despite the fact that it does not belong to the tree anymore.
    """
    if self.left is None or self.right is None:
      if self is self.parent.left:
        self.parent.left = self.left or self.right
        if self.parent.left is not None:
          self.parent.left.parent = self.parent
      else:
        self.parent.right = self.left or self.right
        if self.parent.right is not None:
          self.parent.right.parent = self.parent
      return self
    else:
      s = self.successor()
      deleted_node = s.delete()
      self.key, s.key = s.key, self.key
      return deleted_node


