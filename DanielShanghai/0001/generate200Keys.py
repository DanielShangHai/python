#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DanielSong'

import uuid
import random
#from random import random

def codeGenerator_byRandom(codelength = 8):
    chars = 'abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPGRSTUVWXYZ1234567890'
    resultstr = ''
    for i in range(1,codelength+1):
    	index = random.randint(1,len(chars))
    	resultstr = resultstr + chars[index-1]
    return resultstr

def codeGenerator_byUUID():
    resultstr = str(uuid.uuid1())    
    return resultstr



if __name__ == '__main__':
    resultFile = open('result.txt', 'w')
    for i in range(1,201):
        codeStr = codeGenerator_byRandom()
        print ("%d: "%i + codeStr)
        resultFile.write(codeStr+'\r\n')
    for i in range(200):
        codeStr = codeGenerator_byUUID()
        print ("%d: "%i + codeStr + "\r\n")
        resultFile.write(codeStr+'\r\n')
