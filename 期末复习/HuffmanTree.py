# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:29:07 2020

@author: ThinkPad
"""

from PrioQueue import PrioQueue
from BiTree1 import BiTNode

class HTNode(BiTNode):    
    def __lt__(self, othernode):        
        return self.data < othernode.data
    
class HuffmanPrioQ(PrioQueue):    
    def number(self): 
        return self.num 

def HuffmanTree(weights):    
    trees = HuffmanPrioQ()    
    for w in weights:        
        trees.enqueue(HTNode(w, None, None))    
    while trees.number() > 1:        
        t1 = trees.dequeue()        
        t2 = trees.dequeue()        
        x = t1.data + t2.data        
        trees.enqueue(HTNode(x, t1, t2))    
    return trees.dequeue()





