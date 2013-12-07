from random import choice
global integer
integer=[]
def most_common(g):
    objDict=dict([(x,g.count(x)) for x in set(g)])
    common=[x for x in objDict.keys() if objDict[x]==max(objDict.values())]
    return common[0]

def modify(g,v1,v2):
    for key in g.keys():
        for index in range(len(g[key])):
            if g[key][index]==v2:
                g[key][index]=v1
    return g
                

def karger(g):
    edge=choice(g.keys())
    v2=most_common(g[edge])
    #print g,edge,v2
    g[edge].extend(g[v2])
    del g[v2]
    modify(g,edge,v2)
    #print g,edge,v2
    #print g,edge
    g[edge]=filter(lambda x:x!=edge,g[edge])
    #print g,edge,v2
    if len(g.items())==2:
        cut=len(g[edge])
        integer.append(cut)
        return cut
    else:
        karger(g)
    



for i in range(10):
    file=open(r'C:\cygwin\home\hp\Python\StandfordAlgorithm\assignment3\kargerMinCut.txt')
    g={}
    for line in file:
        words=line.split()
        words=map(int,words)
        g[words[0]]=words[1:len(words)]
    karger(g)
print min(integer)
    
    
