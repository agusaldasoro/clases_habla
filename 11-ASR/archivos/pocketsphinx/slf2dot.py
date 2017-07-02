#!/usr/bin/env python
# coding: utf-8
# Converts an HTK standard lattice format (SLF) to DOT format.
# AG - 06/2017 - Universidad de Buenos Aires

import sys
import re

filestem=sys.argv[1]

# Read SLF file.
f = open(filestem+".slf", "r")
nodes = []
edges = []
for line in f:
    if line[0]=="I":
        m = re.match("I=([0-9]+)\tt=([0-9.]+)\t.*W=(.+)\tv=1", line)
        node_index, node_time, node_word = m.group(1), m.group(2), m.group(3)
        assert(len(nodes)==int(node_index))
        nodes.append(node_word +'/'+ node_time)
    if line[0]=="J":
        m = re.match("J=.*\tS=([0-9]+)\tE=([0-9]+)\t.*a=(.+)\tp=.*", line)
        edges.append((int(m.group(1)), int(m.group(2)), m.group(3)))

# Write DOT file.
w = open(filestem+".dot", "w")
w.write('digraph lattice {\n')
w.write('\trankdir=LR;\n')
w.write('\t\tnode [shape=circle];')

nodesR = nodes[:]
nodesR.reverse()

for i in range(0,len(nodesR)-1):
    w.write('"'+nodesR[i]+'"')
w.write(';\n')

w.write('\tnode [shape=doublecircle]; "'+nodesR[-1]+'";\n\n')

for edge in edges:
    s,e,a = edge[0],edge[1],edge[2]
    w.write('\t"'+nodes[s]+'" -> "'+nodes[e]+'" [label="'+a+'"];\n')

w.write('}')
w.close()

