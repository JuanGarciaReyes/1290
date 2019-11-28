# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:09:02 2019

@author: Eng
"""

def countSubstrings (s):

        res = 0
        dp = [[0]*(len(s)) for i in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                if dp[i][j]:
                    res+=1
        return res 