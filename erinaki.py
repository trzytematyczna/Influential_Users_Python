__author__ = 'moni'

# ProfileRank= w_e + f( w_p * Pi , w_a * Ai)
# Pi = w1 * p1 + ... +wn * pn
# Ai = wn+1 * a1 + ... + wn+m * am

wpf = 0.05 # number of friends
wpg = 0.05 # communities

wap = 0.03 # number of posts

w_e = 1
w_p = 1
w_a = 1

for NI in GR.Nodes():
    ProfileRank = ProfileRank + ( w_e + w_p * (wpf * GetInDeg() + wpg * circles[GR])  )
