# -*- coding: utf-8 -*-
from avl import *
from range_node import *

class RangeTree(AVL):
  """BST with support for range queries."""

  def __init__(self, node_class = RangeNode):
    """Creates an empty AVL tree.
    
    Args:
      node_class (optional): the class of nodes in the tree, defaults to AVLNode
    """
    AVL.__init__(self, node_class)
    
  def rank(self, key):
    """Number of keys <= the given key in the tree."""
    if self.root is not None:
      return self.root.rank(key)
    return 0

  def lca(self, low_key, high_key):
    """Lowest-common ancestor node of nodes with low_key and high_key.
    
    If low_key and/or high_key are not in the tree, this returns the LCA of the
    nodes that would be created by inserting the keys in the tree.
    
    Returns a RangeNode instance, or None if low_key and high_key are not in the
    tree, and there is no key in the tree such that low_key < key < high_key.
    """
    return self.root and self.root.lca(low_key, high_key)

  def list(self, low_key, high_key):
    """A list containing the nodes with keys between low_key and high_key."""
    result = []
    lca = self.lca(low_key, high_key)
    if lca is not None:
      lca.list(low_key, high_key, result)
    return result