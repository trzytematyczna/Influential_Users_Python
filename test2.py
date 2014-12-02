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
#            with open(feat_file) as f:
#                feat = f.read().split()
#                  j= 0
#                for i in feat:
#                        if(j <=0):
#                            feat_similarity2[str(node_id)]={feat[0]: sum([int(i) for i, j in zip(zm, feat) if i == j])}
#                            j=1
#                        if(j>0):
#                            feat_similarity2[str(node_id)].update({feat[0]: sum([int(i) for i, j in zip(zm, feat) if i == j])})
#            f.close()
    print circles[18996905]
    print hashtags_count[18996905]

    #print GR.GetInDeg();
    #print  feat_similarity[18996905]


# ProfileRank= w_e + f( w_p * Pi , w_a * Ai)
# Pi = w1 * p1 + ... +wn * pn
# Ai = wn+1 * a1 + ... + wn+m * am

    wpf = 0.05 # number of friends
    wpg = 0.05 # communities

    wap = 0.03 # number of posts

    w_e = 1
    w_p = 1
    w_a = 1

    ProfileRank = {}
    file =   "C:\\Users\\moni\\Documents\\agh\\IXsem\mgr\\erinaki_dane\\results.txt"
    for NI in GR.Nodes():
        circles_file = path + str(NI.GetId()) + ".circles"
        if os.path.exists(circles_file):
            #print "bla2"
            ProfileRank[NI.GetId()] = ( w_e + w_p * (wpf * NI.GetInDeg() + wpg * circles[NI.GetId()]) + w_a * (wap * hashtags_count[NI.GetId()] ) )
            #with open(file, 'r+') as f:


    #ProfileRank[18996905]

    from operator import itemgetter
    asd = sorted(ProfileRank.items(), key=itemgetter(1))

    print asd
    print asd[-10:]

    with open(file, 'r+') as f:
        f.write(str(asd[-10:]))
        f.write(str(ProfileRank))
        #f.write(ProfileRank)


if __name__ == '__main__':
    intro()