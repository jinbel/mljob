#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# begin of matxManipulation.py

__author__ = 'Jinbel Ju'

def readMatrix(filename):
    #print filename
    data = []
    tokens = []
    category = []
    try:
        fd = open(filename, 'r')
        headline = fd.readline()
        rowsline = fd.readline()
        dSize = int(rowsline.split(' ')[0])
        vSize = int(rowsline.split(' ')[1])
        tokensline = fd.readline()
        tokens = tokensline.split(' ')[0:-1]

        #for line in fd.readlines():
        for line in fd.readlines():
            wordsNums = [0] * vSize
            words = line.split(' ')
            category.append(int(words[0]))
            wordAscs = words[1:-2:2]
            wordNums = words[2:-1:2]
            curSum = 0
            for i in range(len(wordAscs)):
                curSum += int(wordAscs[i])
                wordsNums[curSum] += int(wordNums[i])
            data.append(wordsNums);
    finally:
        if (fd):
            fd.close()

    return data, tokens, category

if __name__ == '__main__':
    print 'module matxManipulation'

# end of matxManipulation.py