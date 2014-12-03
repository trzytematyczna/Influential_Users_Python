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
    nodes = {}
    for NI in GR.Nodes():
        zm = {}
        hs_count = 0
        node_id = NI.GetId()
        circles_file = path + str(node_id) + ".circles"
        egofeat_file = path + str(node_id) + ".egofeat"
        feat_file = path + str(NI.GetId()) + ".feat"
        if os.path.exists(circles_file):
            nodes[node_id] = node_id
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

    ###
    #print circles[18996905]
    #print hashtags_count[18996905]

    #print GR.GetInDeg();
    #print  feat_similarity[18996905]
    ###


################### PROFILE RANK COUNT ###################

# ProfileRank= w_e + f( w_p * Pi , w_a * Ai)
# Pi = w1 * p1 + ... +wn * pn
# Ai = wn+1 * a1 + ... + wn+m * am

#Popularity

    wpf = 0.15 # number of friends
    wpg = 0.05 # communities
    wpc = 0.07 # comments on posts
    wpv = 0.06 # view on posts
    wpt = 0.085 # testimonials (likes)
    wpm = 0.06 # messages per friend
    wppv = 0.05 # profile views/period of time
    wpaf = 0.07 # active contacts
    ###
    wpa = 0.06 # app req
    wpur = 0.07 # user ratings
    wpq = 0.07 # quality of friendship
    wpr = 0.05 # responses to questions
    wppr = 0.07 # public vs private

#Activity

    wap = 0.05 # number of posts
    waq = 0.015 # number of questions posted
    wasu = 0.04 # number status updates
    ###
    waa = 0.015 # app installed
    war = 0.015 # app req sent
    wapu = 0.03 # profile updates
    wat = 0.04 # last login time

    w_e = 1
    w_p = 1
    w_a = 1

    ProfileRank = {}
    DegreeCentrality = {}
    for NI in GR.Nodes():
        #if os.path.exists(circles_file):
        node_id = NI.GetId()
        if nodes.__contains__(node_id):
            circles_file = path + str(NI.GetId()) + ".circles"
            ProfileRank[node_id] = ( w_e + w_p * (wpf * NI.GetOutDeg() + wpg * circles[node_id]) + w_a * (wap * hashtags_count[node_id] ) )
            DegreeCentrality[node_id] = NI.GetDeg()

    #Sorting
    from operator import itemgetter
    sorted_ProfileRank = sorted(ProfileRank.items(), key=itemgetter(1))
    sorted_DegreeCentrality = sorted(DegreeCentrality.items(), key=itemgetter(1))

    #print sorted_ProfileRank
    #print sorted_ProfileRank[-10:]

    top = 25
    results_file =   "C:\\Users\\moni\\Documents\\agh\\IXsem\mgr\\erinaki_dane\\results.txt"
    #with open(results_file, 'r+') as f:
#        f.write(str(ProfileRank.__len__()))
#        f.write(str("\n"))
    #    f.write(str(sorted_DegreeCentrality[-top:]))
    #    f.write(str("\n"))
    #    f.write(str(sorted_ProfileRank[-top:]))
#        f.write(str("\n"))
#        f.write(str(ProfileRank))
    with open(results_file, 'r+') as f:
        f.write("[")
        for i in range (sorted_ProfileRank.__len__()-1,  sorted_ProfileRank.__len__()-top-1, -1):
            f.write(str(sorted_ProfileRank[i]))
            f.write(";")
        f.write("]")
        f.write("\n")

        f.write("[")
        for i in range (sorted_DegreeCentrality.__len__()-1,  sorted_DegreeCentrality.__len__()-top-1,-1):
            f.write(str(sorted_DegreeCentrality[i]))
            f.write(";")
        f.write("]")
        a=sorted_DegreeCentrality[-top:]
        b=sorted_ProfileRank[-top:]
    f.close()

if __name__ == '__main__':
    intro()