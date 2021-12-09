# Stack Data Structure
# LIFO
# Push, Pop, and Peek Methods
# Prevents Overflow and Underflow

from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    