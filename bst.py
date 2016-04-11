# -*- coding: utf-8 -*-
from bst_node import *

class BST(object):
  """A binary search tree."""

  def __init__(self, node_class = BSTNode):
    """Creates an empty BST.

    Args:
      node_class (optional): the class of nodes in the tree, defaults to BSTNode
    """
    self.node_class = node_class
    self.root = None

  def find(self, key):
    """The node with the given key in this BST.

    Args:
      key: the key of the node to be returned

    Returns a BSTNode instance with the given key, or None if the key was not
    found.
    """
    return self.root and self.root.find(key)

  def min(self):
    """The node with the minimum key in this BST."""
    if self.root is None:
      return None
    else:
      return self.root.min()

  def insert(self, key):
    """Inserts a node into the subtree rooted at this node.

    Args:
      key: the key of the node to be inserted

    Returns a BSTNode with the given key that belongs to this tree.
    """
    node = self.node_class(key)
    if self.root is None:
      self.root = node
      return node
    return self.root.insert(node)

  def delete(self, key):
    """Removes the node with the given key from this BST.

    Args:
      key: the key of the node to be deleted

    Returns a BSTNode instance with the given key, which was removed from the
    tree. If this tree does not contain the given key, returns None. The deleted
    node's fields will still be set, despite the fact that it does not belong to
    the tree anymore.
    """
    node = self.find(key)
    if node is None:
      return None
    if node is self.root:
      pseudo_root = self.node_class(None)
      pseudo_root.left = self.root
      self.root.parent = pseudo_root
      deleted_node = self.root.delete()
      self.root = pseudo_root.left
      if self.root is not None:
        self.root.parent = None
      return deleted_node
    else:
      return node.delete()

  def successor(self, key):
    """Returns the node that contains the next larger (the successor) key in
    the BST in relation to the node with key k.

    Args:
      key: the key of the node whose successor will be returned

    Returns a BSTNode instance whose key is the successor of the given key, or
    None if the given key doesn't exist in the tree, or if is the maximum key,
    so the corresponding node has no successor.
    """
    node = self.find(key)
    return node and node.successor()