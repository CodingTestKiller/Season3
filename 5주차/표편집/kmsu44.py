class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def makelist(n: int):
    head = Node(0)
    pnode = head
    for i in range(1, n):
        node = Node(i, None, pnode)
        pnode.next = node
        pnode = node
    return (head, pnode)


def up(node: Node, x: int):
    for _ in range(x):
        node = node.prev
    return node


def down(node: Node, x: int):
    for _ in range(x):
        node = node.next
    return node


def delete(node: Node, delete: list):
    global tail
    global head
    delete.append(node)
    if node == tail:
        tail = node.prev
        node.prev.next = None
        return node.prev
    if node == head:
        head = node.next
        node.next.prev = None
        return node.next

    node.prev.next = node.next
    node.next.prev = node.prev
    return node.next


def ctrl_z(restore_node: Node):
    global tail
    global head
    if restore_node.data < head.data:
        restore_node.next.prev = restore_node
        head = restore_node
        return
    if restore_node.data > tail.data:
        restore_node.prev.next = restore_node
        tail = restore_node
        return

    prev = restore_node.prev
    next = restore_node.next
    prev.next = restore_node
    next.prev = restore_node


def solution(n, k, cmd):
    answer = []
    delete_list = []
    global tail
    global head

    head, tail = makelist(n)

    pnode = head
    for _ in range(k):
        pnode = pnode.next

    for command in cmd:
        c = list(command.split())
        if c[0] == 'U':
            pnode = up(pnode, int(c[1]))
        elif c[0] == 'D':
            pnode = down(pnode, int(c[1]))
        elif c[0] == 'C':
            pnode = delete(pnode, delete_list)
        else:
            ctrl_z(delete_list.pop())

    for _ in range(n):
        answer.append('O')

    for node in delete_list:
        answer[node.data] = 'X'

    answer = ''.join(answer)
    return answer
