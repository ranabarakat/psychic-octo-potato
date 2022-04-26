# psychic-octo-potato
Performance of red black trees implemented in python.

Most of BST operations (e.g: insert, search, delete) take O(h) time where h is the height of the tree. If the BST is skewed (e.g: inserting an array of sorted numbers one at a time) then the time complexity becomes O(n) where n is the number of elements. If we can find a way to keep it balanced, then we can ensure that the time complexity is kept at O(lgn).

A red black tree is a balanced BST where time complexity of all operations doesn't exceed O(lgn).

Applied on a dictionary, it is used to insert new words more efficiently than ordinary BSTs due to its properties that keep it balanced.
After each insertion, the height and size of the modified RB tree are asserted.
