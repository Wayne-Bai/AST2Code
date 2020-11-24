import js2py
# import esprima
import json

esprima = js2py.require('esprima')
escodegen = js2py.require('escodegen')

w1 = open('list_AST.json', 'a')
w2 = open('dict_AST.json', 'a')

def extractAST(dic, dic_list, flag):
    new_dic = {}
    new_key_list = []
    new_value_list = []

    if type(dic) == dict:

        for key,value in dic.items():
            new_key_list.append(key)
            if type(value) == list or type(value) == dict:
                new_value_list.append(value)
        # print(new_list)

    if new_value_list != []:

        for key, value in dic.items():
            if key == 'type':
                new_dic['id'] = flag
                new_dic['type'] = value
                flag += 1
            if key == 'raw' or key == 'name' or key == 'kind':
                new_dic['value'] = value

        children = []

        for child in new_value_list:
            if type(child) == dict:
                if 'type' in child.keys():
                    child_dic, dic_list, flag = extractAST(child, dic_list, flag)
                    children.append(child_dic['id'])
            if type(child) == list:
                for i in range(len(child)):
                    if type(child[i]) == dict and 'type' in child[i].keys():
                        child_dic, dic_list, flag = extractAST(child[i], dic_list, flag)
                        children.append(child_dic['id'])
        new_dic['children'] = children
        dic_list.append(new_dic)

        return new_dic, dic_list, flag

    else:
        key_list = []
        for key in dic.keys():
            key_list.append(key)
        # print(key_list)
        for key,value in dic.items():
            if key == 'type':
                new_dic['id'] = flag
                new_dic['type'] = value
                flag += 1
            if key == 'raw' or key == 'name' or key == 'kind':
                new_dic['value'] = value
        dic_list.append(new_dic)
        return new_dic, dic_list, flag


f = open('example.js')

src = f.read()

tree = esprima.parse(src)
print(tree)
tree_dict = tree.to_dict()
AST_dict_Json = json.dumps(tree_dict)
w2.write(AST_dict_Json)
w2.write('\n')
w2.close()
# print(type(tree_dict))
# print(escodegen.generate(tree_dict))

ast_dic = []
flag = 0
dic, final_list, flag = extractAST(tree_dict, ast_dic, flag)
AST_list = sorted(final_list, key=lambda e: e.__getitem__('id'), reverse=False)
print(AST_list)
AST_list_Json = json.dumps(AST_list)
w1.write(AST_list_Json)
w1.write('\n')
w1.close()