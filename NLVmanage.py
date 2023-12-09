from Node import Node
from Link import Link
from Virtual_Node import Virtual_Node


def number_generater():
    num = 0

    def generate_number():
        nonlocal num
        num = num + 1
        return num

    return generate_number


node_id_generater = number_generater()
link_id_generater = number_generater()
virtual_node_id_generater = number_generater()


# 创造n个节点
def create_node(n: int) -> list:
    node_list = []
    for i in range(n):
        node_list.append(Node(node_id_generater()))
    return node_list


# 判断两个节点是否连接
def is_link(node1: Node, node2: Node) -> bool|Link:
    if node1.is_link_node(node2) and node2.is_link_node(node1):
        return True
    return False


# 连接两个节点
def link_node(node1: Node, node2: Node) -> bool:
    if is_link(node1, node2):
        print("节点已连接,无需重复连接")
        return False
    node1.add_link_node(node2)
    node2.add_link_node(node1)
    return True


# 断开两个节点
def unlink_node(node1: Node, node2: Node) -> bool:
    if not is_link(node1, node2):
        print("节点未连接,无需断开")
        return False
    node1.remove_link_node(node2)
    node2.remove_link_node(node1)
    return True


# 给一个节点生成n个虚拟节点
def create_virtual_node(node: Node, n: int):
    for i in range(n):
        node.add_virtual_node(Virtual_Node(virtual_node_id_generater()))

