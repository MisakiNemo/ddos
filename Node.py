##模拟区块链的p2p网络节点
class Node:
    def __init__(self, node_id, ip_address=None):
        self.node_id = node_id
        self.link_node = []
        self.virtual_node = []
        self.payload = 0
        self.flow = 0
        self.ip_address = ip_address

    # 添加连接节点
    def add_link_node(self, node):
        self.link_node.append(node)

    # 删除连接节点
    def remove_link_node(self, node):
        self.link_node.remove(node)

    # 判断是否相连
    def is_link_node(self, node) -> bool:
        if not self.link_node:
            return False
        for link_node in self.link_node:
            if link_node == node:
                return True
        return False

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
    def add_flow(self, flow: int) -> bool:
        if self.flow + flow > self.payload:
            print(self.node_id + "节点流量溢出")
            return False
        self.flow += flow
        return True

    # 减少流量
    def reduce_flow(self, flow: int) -> bool:
        if self.flow - flow < 0:
            print(self.node_id + "节点流量溢出")
            return False
        self.flow -= flow
        return True

    # 打印节点信息
