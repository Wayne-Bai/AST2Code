import json
import js2py

escodegen = js2py.require('escodegen')

def convertAST(node):
    seq_dic = {}
    if node['type'] == 'Program':
        # node_dic['type'] = "Program"
        # node_dic['sourceType'] = "script"
        # node_dic['body'] = []
        # whole_AST = node_dic

        seq_dic['type'] = "Program"
        seq_dic['sourceType'] = "script"
        seq_dic['body'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == "VariableDeclaration":
        seq_dic['type'] = "VariableDeclaration"
        seq_dic['kind'] = node['value']
        seq_dic['declarations'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == "VariableDeclarator":
        seq_dic['type'] = "VariableDeclarator"
        seq_dic['id'] = {}
        seq_dic['init'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == "Identifier":
        seq_dic['type'] = "Identifier"
        seq_dic['name'] = node['value']
        seq_dic['seqN'] = node['id']

    elif node['type'] == "Literal":
        seq_dic['type'] = "Literal"
        seq_dic['value'] = node['value']
        seq_dic['raw'] = node['value']
        seq_dic['seqN'] = node['id']

    return seq_dic



def mergeAST(dic1,dic2,idx):
    for k, v in dic1.items():
        if k == 'seqN':
            if idx == v:
                if dic1['type'] == 'Program':
                    dic1['body'].append(dic2)
                elif dic1['type'] == 'VariableDeclaration':
                    dic1['declarations'].append(dic2)
                elif dic1['type'] == 'VariableDeclarator':
                    if dic2['type'] == 'Identifier':
                        dic1['id'] = dic2
                    elif dic2['type'] == 'Literal':
                        dic1['init'] = dic2
        elif type(v) is dict and v!={}:
                mergeAST(v, dic2, idx)
        elif type(v) is list and v!=[]:
            for i in range(len(v)):
                mergeAST(v[i],dic2,idx)



f = open('list_AST.json', 'r')

for line in f.readlines():
    dics = json.loads(line)
    whole_AST = {}
    seq_list = []
    for i in range(len(dics)):
        seq_AST = {}
        node_id = dics[i]['id']
        if node_id != 0:
            for j in range(i):
                if 'children' in dics[j].keys() and node_id in dics[j]['children']:
                    seq_AST = convertAST(dics[i])
                    mergeAST(whole_AST,seq_AST,j)

        else:
            first_AST = convertAST(dics[i])
            whole_AST = first_AST
    # print(whole_AST)
    print(escodegen.generate(whole_AST))