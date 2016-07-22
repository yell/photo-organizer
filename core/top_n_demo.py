#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import plac
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from nlp import identify_class, get_labels
from repository import Repository


def main(imgs_path='./', csv_path='data.csv', n=5):
	n = int(n)
	repo = Repository(csv_path)
	plt.ion()
	m = repo.count()
	for index, (img_path, probs, _) in enumerate(repo):
		img_path = os.path.join(imgs_path, img_path)
		print "Image '{0}' ({1} out of {2}):".format(img_path, index, m)
		print '-' * 40
		probs = zip(probs, get_labels())
		probs.sort()
		for prob, fname in probs[::-1][:n]:
			print "{0:.4f}\t{1}".format(prob, fname)
		print "\n\nPress ENTER to continue and any other key to exit.\n"
	
		img = mpimg.imread(img_path)
		imgplot = plt.imshow(img)
		plt.draw()

		s = raw_input()
		if index > 0 and index % 15 == 0:
			plt.close('all')
		if s:
			break


if __name__ == '__main__':
	plac.call(main)