def replace_special_chars(str):
   str = str.replace('/','_')
   str = str.replace('.','_')
   str = str.replace('-','_')
   return str

file = open('../topology.txt')
text = file.read()
lines = text.split('\n')
lines.pop()



import pygraphviz as pgv
graph = pgv.AGraph()
graph.graph_attr['overlap'] = 'scale'
graph.graph_attr['ratio'] = 'fill'
graph.graph_attr['concentrate'] = 'true'

graph.node_attr['fontsize'] = '16'
#graph.graph_attr['splines'] = 'true'




for line in lines:
   vals = line.split('|')
   processed_vals = []

   for val in vals:
       val = val.replace(' ','')
       val = val.replace('GigabitEthernet','Gi')
       val = val.replace('FastEthernet','Fa')
       val = val.lower()
       processed_vals.append(val)

   left_dev, left_port, right_port, right_dev = processed_vals



   graph.add_node(replace_special_chars(left_dev), label=left_dev, shape='box')
   graph.add_node(replace_special_chars(left_dev + left_port), label=left_port)

   graph.add_edge(replace_special_chars(left_dev),replace_special_chars(left_dev + left_port), weight='10')


   graph.add_node(replace_special_chars(right_dev), label=right_dev,shape='box')
   graph.add_node(replace_special_chars(right_dev + right_port), label=right_port)

   graph.add_edge(replace_special_chars(right_dev), replace_special_chars(right_dev + right_port), weight='10')


   graph.add_edge(replace_special_chars(left_dev + left_port), replace_special_chars(right_dev + right_port), weight='2')

   #graph.add_edge(replace_special_chars(left_dev),replace_special_chars(right_dev))



#print graph.string()
graph.layout(prog='dot')
graph.draw('../out.pdf')
