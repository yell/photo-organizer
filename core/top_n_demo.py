#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import plac
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from nlp import identify_class, get_labels
from repository import Repository


def main(imgs_path='../data/test/', csv_path='data.csv', n=5, img_index='None'):
	n = int(n)
	img_index = (None if img_index == 'None' else int(img_index))
	repo = Repository(csv_path)
	plt.ion()
	m = repo.count()
	labels = get_labels()
	for index, (img_path, probs, _) in enumerate(repo):
		if img_index:
			if index != img_index:
				continue
			img_path = os.path.join(imgs_path, img_path)
			print "Image '{0}':".format(img_path)
			print '-' * 40
			probs = zip(probs, labels)
			probs.sort()
			for prob, fname in probs[::-1][:n]:
				print "{0:.4f}\t{1}".format(prob, fname)

			plt.figure(figsize=(12, 8))
			img = mpimg.imread(img_path)
			imgplot = plt.imshow(img)
			plt.axis('off')
			plt.tight_layout()
			plt.draw()
			print "\n\nPress ENTER to exit.\n"
			s = raw_input()
			plt.close('all')
			
		else:
			img_path = os.path.join(imgs_path, img_path)
			print "Image '{0}' ({1} out of {2}):".format(img_path, index + 1, m)
			print '-' * 40
			probs = zip(probs, labels)
			probs.sort()
			for prob, fname in probs[::-1][:n]:
				print "{0:.4f}\t{1}".format(prob, fname)
			print "\n\nPress ENTER to continue and any other key to exit.\n"
		
			img = mpimg.imread(img_path)
			imgplot = plt.imshow(img)
			plt.axis('off')
			plt.tight_layout()
			plt.draw()

			s = raw_input()
			if s:
				break
			if index > 0 and index % 15 == 0:
				plt.close('all')


if __name__ == '__main__':
	plac.call(main)