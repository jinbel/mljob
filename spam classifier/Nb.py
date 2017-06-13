#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# begin of Nb.py

from __future__ import division
import math
import sys, os

class Nb(object):
    def fit(self, data, tokens, category):
        vSize = len(tokens)
        dSize = len(data)
        trainMatrixs = [[], []]

        for i in range(dSize):
            trainMatrixs[category[i]].append(data[i])

        self.pos_log_prior = math.log(len(trainMatrixs[1]) / dSize)
        self.neg_log_prior = math.log(len(trainMatrixs[0]) / dSize)
        print self.pos_log_prior, self.neg_log_prior
        neg_phi = [1] * vSize
        pos_phi = [1] * vSize

        for k in range(vSize):
            neg_words = 0;
            pos_words = 0;
            for i in range(len(trainMatrixs[0])):
                neg_phi[k] += trainMatrixs[0][i][k]
                neg_words += sum(trainMatrixs[0][i])
            for i in range(len(trainMatrixs[1])):
                pos_phi[k] += trainMatrixs[1][i][k]
                pos_words += sum(trainMatrixs[1][i])
            neg_phi[k] /= neg_words + vSize
            pos_phi[k] /= pos_words + vSize

        self.neg_phi = neg_phi
        self.pos_phi = pos_phi

    def test(self, data, tokens, category):
        vSize = len(tokens)
        dSize = len(data)
        neg_log_phi = []
        pos_log_phi = []
        output = [0] * dSize
        for phiI in self.neg_phi:
            neg_log_phi.append(math.log(phiI))
        for phiI in self.pos_phi:
            pos_log_phi.append(math.log(phiI))
        
        for i in range(dSize):
            neg_log_posterior = self.neg_log_prior
            pos_log_posterior = self.pos_log_prior

            for k in range(vSize):
                neg_log_posterior += neg_log_phi[k] * data[i][k]
                pos_log_posterior += pos_log_phi[k] * data[i][k]

            #print neg_log_posterior, pos_log_posterior
            if (neg_log_posterior > pos_log_posterior):
                output[i] = 0
            else:
                output[i] = 1

        error = 0;
        for i in range(dSize):
            error += output[i] != category[i]

        return error / dSize




# end of Nb.py
