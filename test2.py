__author__ = 'moni'
import snap
from snap import *
import os.path
from collections import defaultdict
def intro():

    #building graph
    GR = TNGraph.New()

    content =[]
    graph_file = "C:\\Users\\moni\\Documents\\agh\\IXsem\mgr\\erinaki_dane\\snapy\\twitter_combined.txt"
    with open(graph_file) as f:
        content = f.read().split( )
    f.close

    v1 = int
    v2 = int
    i=0
    while i < content.__len__():
        v1=int(content[i])
        i=i+1
        v2=int(content[i])
        i=i+1
        if(not GR.IsNode(v1) ):
            GR.AddNode(v1)
        if(not GR.IsNode(v2)):
            GR.AddNode(v2)
        GR.AddEdge(v1,v2)

    print "G1: Nodes %d, Edges %d" % (GR.GetNodes(), GR.GetEdges())


    #properties of graph
    path = "C:\\Users\\moni\\Documents\\agh\\IXsem\mgr\\erinaki_dane\\snapy\\twitter\\"

    circles = {}
    hashtags_count = {}
    feat ={}
    single_similarity= {}
    feat_similarity2 = {}
    feat_similarity = defaultdict(dict)
    for NI in GR.Nodes():
        zm = {}
        hs_count = 0
        node_id = NI.GetId()
        circles_file = path + str(node_id) + ".circles"
        egofeat_file = path + str(node_id) + ".egofeat"
        feat_file = path + str(NI.GetId()) + ".feat"
        if os.path.exists(circles_file):
            with open(circles_file) as f:
                circles[node_id] = f.read().splitlines().__len__()
            f.close()
            with open(egofeat_file) as f:
                zm = f.read().split( )
                for i in zm:
                    if(int(i)== 1):
                        hs_count=hs_count+1
            f.close()
            hashtags_count[node_id] = hs_count
            a = [1, 2, 3, 4, 5]
            b = [9, 8, 2, 6, 5]
            #print
            with open(feat_file) as f:
                feat = f.read().split()
                j= 0
                for i in feat:
                #print feat[0]
                #print feat[0]
                #print set(zm) & set(feat)
                #shared.
                #d={"u1_1":{"u2_1": 134, "u2_2": 43}}
#                    if(not feat_similarity2):
                        #print i
                        if(j <=0):
                            #print node_id
                            #print feat[0]
                            feat_similarity2[str(node_id)]={feat[0]: sum([int(i) for i, j in zip(zm, feat) if i == j])}
                            j=1
                        if(j>0):
                            #print node_id
                            feat_similarity2[str(node_id)].update({feat[0]: sum([int(i) for i, j in zip(zm, feat) if i == j])})
                #print feat_similarity2
                #    feat_similarity[node_id][feat[0]] = sum([int(i) for i, j in zip(zm, feat) if i == j])
            f.close()
    print circles[18996905]
    print hashtags_count[18996905]
    print  feat_similarity[18996905]

if __name__ == '__main__':
    intro()