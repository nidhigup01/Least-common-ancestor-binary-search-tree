# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:41:02 2018

@author: nidhi
"""

# A recursive python program to find LCA of two nodes
# n1 and n2
 
# A Binary tree node
class Node():
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
        

def lca(T, root, n1, n2):
    data = root.data
    print ('_root.key_', root.data)
    #Base Case
    num_rows = len(T)
    print ('num_rows', num_rows)
    num_columns = len(T[0])
    print ('num_columns', num_columns)
   
    def left_child(key):
        for child in range(0, num_columns):
            parent = Node(data)
            parent_num = parent.data
            print ('parent', parent)
            if T[parent_num][child] == 1 and  child <= parent_num:
                root.left.data = child
                
                print('keyleft', root.left)
                print ('root.left', root.left )
                return root.left
            elif T[parent_num][child] == 0:
                pass
            elif T[parent_num][child]==None:
                pass
    def right_child(key):  
        for child in range(0, num_columns):
            parent = Node(data)
            parent_num = parent.data
            print ('parent', parent)    
            if T[parent_num][child] == 1 and  child > parent_num:
                root.right.data = child
                print('key right', root.right)
                print ('root.right', root.right )
                return root.right
            elif T[parent][child] == 0:
                pass
            elif T[parent][child]==None:
                pass
     
    # Base Case
    if root is None or T == None or T == [[]]:
        return None
      
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root
 
# Driver program to test above function
 

root = Node(3) 
T = [[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]] ;n1 = 1 ; n2 = 4
     
t = lca(T, root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))
 
root = Node(3)
T = [[0, 1, 0, 0, 0,0],[0, 0, 0, 0, 0,0],[0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 1, 0],[0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0]] ;n1 = 2 ; n2 = 5
     
t = lca(T, root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)