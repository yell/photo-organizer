#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plac

from nlp import identify_class, get_labels
from repository import Repository


def main(img_path, n=5, csv_path='data.csv'):
	n = int(n)
	repo = Repository(csv_path)
	print "Image '{0}':".format(img_path)
	print '-' * 40
	probs, _ = repo[img_path]
	probs = zip(probs, get_labels())
	probs.sort()
	for prob, fname in probs[::-1][:n]:
		print "{0:.4f}\t{1}".format(prob, fname)


if __name__ == '__main__':
	plac.call(main)