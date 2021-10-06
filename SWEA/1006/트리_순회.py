def preorder(nodes, v):
    print(v, end=' ')
    if nodes[v] != 0 and len(nodes[v]) >= 1:
        if nodes[v][0] < V:
            preorder(nodes, nodes[v][0])
        else:
            print(nodes[v][0], end=' ')
    if nodes[v] != 0 and len(nodes[v]) == 2:
        if nodes[v][1] < V:
            preorder(nodes, nodes[v][1])
        else:
            print(nodes[v][1], end=' ')


def inorder(nodes, v):
    if nodes[v] != 0 and len(nodes[v]) >= 1:
        if nodes[v][0] < V:
            preorder(nodes, nodes[v][0])
        else:
            print(nodes[v][0], end=' ')
    print(v, end=' ')
    if nodes[v] != 0 and len(nodes[v]) == 2:
        if nodes[v][1] < V:
            preorder(nodes, nodes[v][1])
        else:
            print(nodes[v][1], end=' ')


def postorder(nodes, v):
    if nodes[v] != 0 and len(nodes[v]) >= 1:
        if nodes[v][0] < V:
            preorder(nodes, nodes[v][0])
        else:
            print(nodes[v][0], end=' ')
    if nodes[v] != 0 and len(nodes[v]) == 2:
        if nodes[v][1] < V:
            preorder(nodes, nodes[v][1])
        else:
            print(nodes[v][1], end=' ')
    print(v, end=' ')


V = int(input())
nodes = [0]*V
v_list = list(map(int, input().split()))
for i in range(0, 2*V, 2):
    if nodes[v_list[i]] == 0:
        nodes[v_list[i]] = []
    nodes[v_list[i]].append(v_list[i+1])
print(nodes)

preorder(nodes, 1)
print()
inorder(nodes, 1)
print()
postorder(nodes, 1)