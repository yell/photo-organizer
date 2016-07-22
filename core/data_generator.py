#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import plac

from repository import Repository
from extractor import probs_feats


def main(imgs_path, deploy_path, weights_path, blob_name="pool5/7x7_s1"):
	repo = Repository()
	if imgs_path[-1] != '/': imgs_path += '/'
	for directory, dirnames, filenames in os.walk(imgs_path):
		for fname in filenames:
			fpath = imgs_path + fname
			probs, feats = probs_feats(fpath, deploy_path, weights_path, blob_name)
			repo.store(fpath, probs, feats)

if __name__ == '__main__':
	plac.call(main)