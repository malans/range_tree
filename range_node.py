# -*- coding: utf-8 -*-
from avl_node import *

class RangeNode(AVLNode):
  """A node in a range tree."""

  def __init__(self, key):
    """Creates a node that will be inserted in a range index tree.
  
    See __init__ in BSTNode."""
    AVLNode.__init__(self, key)
    self.tree_size = 1

  def update_subtree_info(self):
    """Updates pre-computed fields such as the node's subtree height."""
    AVLNode.update_subtree_info(self)
    self.tree_size = self._uncached_tree_size()

  def _uncached_tree_size(self):
    """Re-computes the node's subtree size based on the children's heights."""
    return 1 + (((self.left and self.left.tree_size) or 0) +
                ((self.right and self.right.tree_size) or 0))
    
  def check_ri(self):
    """Checks the AVL representation invariant around this node.
    
    Raises an exception if the RI is violated.
    """
    if self.tree_size != self._uncached_tree_size():
      raise RuntimeError("RangeTree RI violated by node subtree size")
    AVLNode.check_ri(self)

  def rank(self, key):
    """Number of keys <= the given key in the subtree rooted at this node."""
    if key < self.key:
      if self.left is not None:
        return self.left.rank(key)
      else:
        return 0
    if self.left:
      lrank = 1 + self.left.tree_size
    else:
      lrank = 1
    if key > self.key and self.right is not None:
      return lrank + self.right.rank(key)
    return lrank

  def lca(self, low_key, high_key):
    """Lowest-common ancestor node of nodes with low_key and high_key.
    
    If low_key and/or high_key are not in the tree, this returns the LCA of the
    nodes that would be created by inserting the keys in the tree.
    
    Returns a RangeNode instance, or None if low_key and high_key are not in the
    node's subtree, and there is no key in the tree such that
    low_key < key < high_key.
    """
    if low_key <= self.key <= high_key:
      return self
    if low_key < self.key:
      return self.left and self.left.lca(low_key, high_key)
    else:
      return self.right and self.right.lca(low_key, high_key)

  def list(self, low_key, high_key, result):
    """Lists nodes with keys between low_key and high_key in this node's subtree.
    
    Extends result with a list of RangeNode instances for the nodes in the
    subtree rooted at this node, such that each node's key is between low_key
    and high_key."""
    if low_key <= self.key <= high_key:
      result.append(self)
    if self.left is not None and low_key <= self.key:
      self.left.list(low_key, high_key, result)
    if self.right is not None and self.key <= high_key:
      self.right.list(low_key, high_key, result)