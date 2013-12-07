# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:05:18 2013

@author: james
"""

import sys

def FindMiniLength(edgelist):
    foo=edgelist[0][2]
    
    minilist=edgelist[0]
    for i in range(1,len(edgelist)):
        if foo>edgelist[i][2]:
            foo=edgelist[i][2]
            minilist=edgelist[i]
    return minilist


txtfile=open(sys.argv[1])

N=8
root={}
edgelist=[]
ClusterNode={}
NodeCluster={}

def findRoot(a,NodeCluster):
    while NodeCluster[a] !=a:
        a=NodeCluster[a]
    return a

for line in txtfile:
    line=line.split()
    line=map(int,line)
    edgelist.append(line)
    
for count in range(1,N+1):
    ClusterNode[count]=[count]
    NodeCluster[count]=count

while len(ClusterNode.keys())>4:
    MiniLen=FindMiniLength(edgelist)
    a=MiniLen[0]
    b=MiniLen[1]
    edgelist.remove(MiniLen)
    Root=findRoot(a,NodeCluster)
    foo=findRoot(MiniLen[1],NodeCluster)
    if NodeCluster[foo]!=Root:
        ClusterNode[Root]+=ClusterNode[foo]
        del ClusterNode[foo]
        NodeCluster[foo]=Root

for items in edgelist:
    if findRoot(items[0],NodeCluster)==findRoot(items[1],NodeCluster):
	edgelist.remove(items)

print min(edgelist, key= lambda l:l[2])
