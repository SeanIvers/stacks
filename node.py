# Codecademy Node Data Structure

# Nodes - Contain data and a link (or multiple links) to other nodes

# Basic single link node
# class Node:
#     def __init__(self, value, link_node):
#         self.value = value
#         self.link_node = link_node

#     # Method to get value
#     def get_value(self):
#         return self.value

#     # Method to get link
#     def get_link_node(self):
#         return self.link_node

#     # Method to set link node
#     def set_link_node(self, link_node):
#         self.link_node = link_node

# Node Class for other Data Structures
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value

