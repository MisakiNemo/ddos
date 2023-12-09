##模拟区块链的p2p网络节点
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.link_node = []
        self.virtual_node = []
        self.payload = 0
        self.flow = 0
        self.link = []

    # 添加连接节点
    def add_link_node(self, node):
        self.link_node.append(node)

    # 删除连接节点
    def remove_link_node(self, node):
        self.link_node.remove(node)

    # 添加连接
    def add_link(self, link):
        self.link.append(link)

    def remove_link(self, link):
        self.link.remove(link)

    def get_link_node(self):
        return self.link_node

    def get_link(self):
        return self.link

    def get_payload(self):
        return self.payload

    # 添加虚拟节点
    def add_virtual_node(self, virtual_node):
        self.virtual_node.append(virtual_node)

    # 删除虚拟节点
    def remove_virtual_node(self, virtual_node):
        self.virtual_node.remove(virtual_node)

    # 获取虚拟节点
    def get_virtual_node(self):
        return self.virtual_node

    # 添加流量
    def add_flow(self, flow):
        self.flow += flow

    # 减少流量
    def reduce_flow(self, flow):
        self.flow -= flow
