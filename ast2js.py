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
        # seq_dic['sourceType'] = "module"
        seq_dic['body'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == "ArrayPattern":
        seq_dic['type'] = "ArrayPattern"
        seq_dic['elements'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == "RestElement":
        seq_dic['type'] = "RestElement"
        seq_dic['argument'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'AssignmentPattern':
        seq_dic['type'] = "AssignmentPattern"
        seq_dic['left'] = {}
        seq_dic['right'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ObjectPattern':
        seq_dic['type'] = "ObjectPattern"
        seq_dic['properties'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ThisExpression':
        seq_dic['type'] = "ThisExpression"
        seq_dic['seqN'] = node['id']

    elif node['type'] == "Identifier":
        seq_dic['type'] = "Identifier"
        seq_dic['name'] = node['name']
        seq_dic['seqN'] = node['id']

    elif node['type'] == "Literal":
        seq_dic['type'] = "Literal"
        seq_dic['value'] = node['value']
        seq_dic['raw'] = node['raw']
        seq_dic['seqN'] = node['id']
        if 'regex' in node.keys():
            seq_dic['regex'] = node['regex']

    elif node['type'] == 'ArrayExpression':
        seq_dic['type'] = 'ArrayExpression'
        seq_dic['elements'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ObjectExpression':
        seq_dic['type'] = "ObjectExpression"
        seq_dic['properties'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'Property':
        seq_dic['type'] = 'Property'
        seq_dic['key'] = {}
        seq_dic['computed'] = node['computed']
        seq_dic['value'] = {}
        seq_dic['kind'] = node['kind']
        seq_dic['method'] = node['method']
        seq_dic['shorthand'] = node['shorthand']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'FunctionExpression':
        seq_dic['type'] = "FunctionExpression"
        seq_dic['id'] = {}
        seq_dic['params'] = []
        seq_dic['body'] = {}
        seq_dic['generator'] = node['generator']
        seq_dic['async'] = node['async']
        seq_dic['expression'] = node['expression']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ArrowFunctionExpression':
        seq_dic['type'] = "ArrowFunctionExpression"
        seq_dic['id'] = {}
        seq_dic['params'] = []
        seq_dic['body'] = {}
        seq_dic['generator'] = node['generator']
        seq_dic['async'] = node['async']
        seq_dic['expression'] = node['expression']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ClassExpression':
        seq_dic['type'] = "ClassExpression"
        seq_dic['id'] = {}
        seq_dic['superClass'] = {}
        seq_dic['body'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ClassBody':
        seq_dic['type'] = "ClassBody"
        seq_dic['body'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'MethodDefintion':
        seq_dic['type'] = 'MethodDefinition'
        seq_dic['key'] = {}
        seq_dic['computed'] = node['computed']
        seq_dic['value'] = {}
        seq_dic['kind'] = node['kind']
        seq_dic['static'] = node['static']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'TaggedTemplateExpression':
        seq_dic['type'] = "TaggedTemplateExpression"
        seq_dic['readonly tag'] = {}
        seq_dic['readonly quasi'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'TemplateElement':
        seq_dic['type'] = 'TemplateElement'
        seq_dic['value'] = node['value']
        seq_dic['tail'] = node['value']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'TemplateLiteral':
        seq_dic['type'] = 'TemplateLiteral'
        seq_dic['quasis'] = []
        seq_dic['expressions'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'MemberExpression':
        seq_dic['type'] = 'MemberExpression'
        seq_dic['computed'] = node['computed']
        seq_dic['object'] = {}
        seq_dic['property'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'Super':
        seq_dic['type'] = 'Super'
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'MetaProperty':
        seq_dic['type'] = 'MetaProperty'
        seq_dic['meta'] = {}
        seq_dic['property'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'CallExpression':
        seq_dic['type'] = 'CallExpression'
        seq_dic['callee'] = {}
        seq_dic['argument'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'NewExpression':
        seq_dic['type'] = 'NewExpression'
        seq_dic['callee'] = {}
        seq_dic['argument'] = []
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'Import':
        seq_dic['type'] = 'Import'
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'SpreadElement':
        seq_dic['type'] = 'SpreadElement'
        seq_dic['argument'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'UpdateExpression':
        seq_dic['type'] = "UpdateExpression"
        seq_dic['operator'] = node['operator']
        seq_dic['argument'] = {}
        seq_dic['prefix'] = node['prefix']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'AwaitExpression':
        seq_dic['type'] = 'AwaiteExpression'
        seq_dic['argument'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'UnaryExpression':
        seq_dic['type'] = 'UnaryExpression'
        seq_dic['operator'] = node['operator']
        seq_dic['argument'] = {}
        seq_dic['prefix'] = node['prefix']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'BinaryExpression':
        seq_dic['type'] = 'BinaryExpression'
        seq_dic['operator'] = node['operator']
        seq_dic['left'] = {}
        seq_dic['right'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'LogicalExpression':
        seq_dic['type'] = 'LogicalExpression'
        seq_dic['operator'] = node['operator']
        seq_dic['left'] = {}
        seq_dic['right'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'ConditionalExpression':
        seq_dic['type'] = 'ConditionalExpression'
        seq_dic['test'] = {}
        seq_dic['consequent'] = {}
        seq_dic['alternate'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'YieldExpression':
        seq_dic['type'] = 'YieldExpression'
        seq_dic['argument'] = {}
        seq_dic['delegate'] = node['delegate']
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'AssignmentExpression':
        seq_dic['type'] = 'AssignmentExpression'
        seq_dic['operator'] = node['operator']
        seq_dic['left'] = {}
        seq_dic['right'] = {}
        seq_dic['seqN'] = node['id']

    elif node['type'] == 'SequenceExpression':
        seq_dic['type'] = 'SequenceExpression'
        seq_dic['expressions'] = {}
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





    return seq_dic



def mergeAST(dic1,dic2,idx):
    Expression_List = ['Identifier', 'Literal', 'Super', 'MetaProperty']
    for k, v in dic1.items():
        if k == 'seqN':
            if idx == v:
                if dic1['type'] == 'Program':
                    dic1['body'].append(dic2)

                elif dic1['type'] == 'ArrayPattern':
                    if dic2['type'] == 'AssignmentPattern' or dic2['type'] == 'Identifier' or dic2['type'] == 'BindingPattern' \
                            or dic2['type'] == 'RestElement':
                        dic1['elements'].append(dic2)

                elif dic1['type'] == 'RestElement':
                    if dic2['type'] == 'Identifier' or dic2['type'] == 'BindingPattern':
                        dic1['argument'] = dic2

                elif dic1['type'] == 'AssignmentPattern':
                    if dic2['type'] == 'Identifier' or dic2['type'] == 'BindingPattern' and not dic1['left']:
                        dic1['left'] = dic2
                    elif 'Expression' in dic2['type'] or dic2['type'] == 'Identifier' or dic2['type'] == 'Literal' and dic1['left']:
                        dic1['right'] = dic2

                elif dic1['type'] == 'ObjectPattern':
                    if dic2[type] == 'Property':
                        dic1['properties'].append(dic2)

                elif dic1['type'] == 'ArrayExpression':
                    if 'Expression' in dic2['type'] or dic2['type'] in Expression_List or dic2['type'] == 'SpreadElement':
                        dic1['elements'].append(dic2)

                elif dic1['type'] == 'ObjectExpression':
                    if dic2['type'] == 'Property':
                        dic1['properties'].append(dic2)

                elif dic1['type'] == 'Property':
                    if not dic1['key'] and ('Expression' in dic2['type'] or dic2['type'] in Expression_List):
                        dic1['key'] = dic2
                    elif dic1['key'] and ('Expression' in dic2['type'] or dic2['type'] in Expression_List):
                        dic1['value'] = dic2

                elif dic1['type'] == 'FunctionExpression':
                    if dic2['type'] == 'Identifier' and not dic1['id']:
                        dic1['id'] = dic2
                    elif dic2['type'] == 'Identifier' or dic2['type'] == 'AssignmentPattern' or dic2['type'] == 'BindingPattern':
                        dic1['params'].append(dic2)
                    elif dic2['type'] == 'BlockStatement':
                        dic1['body'] = dic2

                elif dic1['type'] == 'ArrowFunctionExpression':
                    if dic2['type'] == 'Identifier' and not dic1['id']:
                        dic1['id'] = dic2
                    elif dic2['type'] == 'Identifier' or dic2['type'] == 'AssignmentPattern' or dic2['type'] == 'BindingPattern':
                        dic1['params'].append(dic2)
                    elif dic2['type'] == 'BlockStatement' or 'Expression' in dic2['type']:
                        dic1['body'] = dic2

                elif dic1['type'] == 'ClassExpression':
                    if dic2['type'] == 'Identifier' and not dic1['id']:
                        dic1['id'] = dic2
                    elif dic2['type'] == 'Identifier':
                        dic1['superClass'] = dic2
                    elif dic2['type'] == 'Classbody':
                        dic1['body'] = dic2

                elif dic1['type'] == 'ClassBody':
                    if dic2['type'] == 'MethodDefinition':
                        dic1['body'].append(dic2)

                elif dic1['type'] == 'MethodDefinition':
                    if 'Expression' in dic2['type'] or dic2['type'] in Expression_List and not dic1['key']:
                        dic1['key'] = dic2
                    elif dic2['type'] == 'FunctionExpression':
                        dic1['value'] = dic2

                elif dic1['type'] == 'TaggedTemplateExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type']:
                        dic1['readonly tag'] = dic2
                    elif dic2['type'] == "TemplateLiteral":
                        dic1['readonly quasi'] = dic2

                elif dic1['type'] == 'TemplateLiteral':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type']:
                        dic1['epressions'].append(dic2)
                    elif dic2['type'] == "TemplateElement":
                        dic1['quasi'].append(dic2)

                elif dic1['type'] == 'MemberExpression':
                    if (dic2['type'] in Expression_List or 'Expression' in dic2['type']) and not dic1['object']:
                        dic1['object'] = dic2
                    elif (dic2['type'] in Expression_List or 'Expression' in dic2['type']) and dic1['object']:
                        dic1['property'] = dic2

                elif dic1['type'] == 'MetaProperty':
                    if dic2['type'] == "Identifier" and not dic1['meta']:
                        dic1['meta'] = dic2
                    elif dic2['type'] == "Identifier" and dic1['meta']:
                        dic1['property'] = dic2

                elif dic1['type'] == 'CallExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type'] or dic2['type'] == 'Import' and not dic1['callee']:
                        dic1['callee'] = dic2
                    elif dic2['type'] in Expression_List or 'Expression' in dic2['type'] or dic2['type'] == 'SpreadElement' and dic1['called']:
                        dic1['arguments'].append(dic2)

                elif dic1['type'] == 'NewExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type'] and not dic1['callee']:
                        dic1['callee'] = dic2
                    elif dic2['type'] in Expression_List or 'Expression' in dic2['type'] or dic2['type'] == 'SpreadElement' and dic1['called']:
                        dic1['arguments'].append(dic2)

                elif dic1['type'] == 'SpreadElement' or dic1['type'] == 'UpdateExpression' or dic1['type'] == 'AwaitExpression'\
                        or dic1['type'] == 'UnaryExpression' or dic1['type'] == 'YieldExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type']:
                        dic1['argument'] = dic2

                elif dic1['type'] == 'BinaryExpression' or dic1['type'] ==  'LogicalExpression' or dic1['type'] == 'AssignmentExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type'] and not dic1['left']:
                        dic1['left'] = dic2
                    elif dic2['type'] in Expression_List or 'Expression' in dic2['type'] and dic1['left']:
                        dic1['right'] = dic2

                elif dic1['type'] == 'ConditionalExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type'] and not dic1['test']:
                        dic1['test'] = dic2
                    elif dic2['type'] in Expression_List or 'Expression' in dic2['type'] and dic1['test'] and not dic1['consequent']:
                        dic1['consequent'] = dic2
                    elif dic2['type'] in Expression_List or 'Expression' in dic2['type'] and dic1['test'] and dic1['consequent']\
                            and not dic1['alternate']:
                        dic1['alternate'] = dic2

                elif dic1['type'] == 'SequenceExpression':
                    if dic2['type'] in Expression_List or 'Expression' in dic2['type']:
                        dic1['expressions'].append(dic2)














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