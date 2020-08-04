#!/usr/bin/env python3
#
# Copyright 2015   David Snyder
# Apache 2.0.
#
# Copied from egs/sre10/v1/local/prepare_for_eer.py (commit 9cb4c4c2fb0223ee90c38d98af11305074eb7ef8)
#
# Given a trials and scores file, this script
# prepares input for the binary compute-eer.
# 将socres文件和trials文件，抽取成 score target/nontarget 形式，后续输入到compute-eer中

import sys
trials = open(sys.argv[1], 'r').readlines()
scores = open(sys.argv[2], 'r').readlines()
spkrutt2target = {}
for line in trials:
  spkr, utt, target = line.strip().split()
  spkrutt2target[spkr+utt]=target
for line in scores:
  spkr, utt, score = line.strip().split()
  print("{} {}".format(score, spkrutt2target[spkr+utt]))
