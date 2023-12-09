class Link:
    def __init__(self,link_id,node1,node2):
        self.link_id = link_id
        self.node1 = node1
        self.node2 = node2
        self.flow = 0

    def get_link_id(self):
        return self.link_id

    def