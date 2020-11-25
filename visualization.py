import networkx as nx
import graphviz
import json

f = open('list_AST.json', 'r')
for line in f.readlines():
    dics = json.loads(line)
    dot = graphviz.Graph(name="MyPicture", format="png")
    node_list = []
    edge_list = []
    for i in range(len(dics)):
        if 'value' in dics[i].keys():
            name = '%s\n[%s]' % (dics[i]['type'], dics[i]['value'])
            node_list.append(name)
        else:
            name = dics[i]['type']
            node_list.append(name)

        if 'children' in dics[i].keys():
            for j in dics[i]['children']:
                edge_list.append((i,j))

    for i in node_list:
        dot.node(i)
    for i in edge_list:
        m,n  = i
        dot.edge(node_list[m],node_list[n])
    dot.view(filename='MyPicture')
