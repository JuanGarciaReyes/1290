# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:56:01 2019

@author: Eng
"""

def findLongestChain(self, pairs):
        
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                        dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)