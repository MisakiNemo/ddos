class Link:
    def __init__(self, link_id, node1, node2):
        self.link_id = link_id
        self.node1 = node1
        self.node2 = node2
        self.flow = 0

    def get_link_id(self):
        return self.link_id

    # 添加流量
    def add_flow(self, flow: int) -> bool:
        self.flow += flow
        return True

    # 减少流量
    def reduce_flow(self, flow: int) -> bool:
        if self.flow - flow < 0:
            print(self.link_id + "节点流量溢出")
            return False
        self.flow -= flow
        return True

    def get_flow(self)->int:
        return self.flow

