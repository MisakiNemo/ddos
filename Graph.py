from Node import Node

class Graph:

    def __init__(self):
        self.node=[]
        self.link=[]


    def add_node(self,node):
        self.node.append(node)

    def add_link(self,link):
        self.link.append(link)

    def get_node(self):
        return self.node

    def remove_node(self,node):
        self.node.remove(node)

    def get_link(self):
        return self.link

    def remove_link(self,link):
        self.link.remove(link)

    #根据node_id获取node
    def get_node_by_id(self,node_id:int)->Node:
        for node in self.node:
            if node.node_id==node_id:
                return node
        return None

