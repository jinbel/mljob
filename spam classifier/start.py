#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# begin of start.py

__author__ = 'Jinbel Ju'

import sys, os
from Nb import Nb
from lib import matxManipulation
"""
data = [[0] * 10, [1] * 10, [0] * 10, [1] * 10, [1] * 10, [1] * 10, [0] * 10, [1] * 10,
    [1] * 10, [1] * 10, [0] * 10]
tokens = ['ss'] * 10
category = [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
nb = Nb();
nb.fit(data, tokens, category)
print nb.test(data, tokens, category)
"""
trainSetUrl = sys.path[0] + '/spam_data/MATRIX.TRAIN'
testSetUrl = sys.path[0] + '/spam_data/MATRIX.TEST'
data, tokens, category = matxManipulation.readMatrix(trainSetUrl);

nb = Nb();
nb.fit(data, tokens, category)

data, tokens, category = matxManipulation.readMatrix(testSetUrl);

print nb.test(data, tokens, category)


# end of start.py
