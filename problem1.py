# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:08:29 2019

@author: Eng
"""

def stoneGame(game):
    if len(game) < 1 and len(game)%2 != 0:
        return -1
    dp =[[0]*len(game) for _ in range(len(game))] 
    for i in range(len(game)-1,-1,-1):
        for j in range(i+1,len(game),2): 
            if i+1==j:
                dp[i][j] = max(game[i],game[j])
            else:
                dp[i][j] = max(game[i] + min(dp[i+2][j],dp[i+1][j-1]), game[j] + min(dp[i+1][j-1],dp[i][j-2]))     
        if dp[0][-1] > sum(game) - dp[0][-1]:
            return True
        else:
            return False

gam = ['6','9','1','2','16','8']
print(stoneGame(gam))
