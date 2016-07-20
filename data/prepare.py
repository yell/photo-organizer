import os
import sys
import csv
import json


def dot():
	sys.stdout.write('.'); sys.stdout.flush()

def safe_mkdir(dirpath):
	try:
	    os.stat(dirpath)
	except:
	    os.mkdir(dirpath)

def split(csvfilepath='actions.csv', train_ratio=0.9):
	safe_mkdir('index/')
	safe_mkdir('train/')
	safe_mkdir('test/')

	with open(csvfilepath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='\'')
		reader = list(reader)
		m = len(reader)

		for index, row in enumerate(reader):
			if index == 0: continue # skip header

			if row[1]:
				target_folder = 'train/' if index < m * train_ratio else 'test/'
			else:
				target_folder = 'index/'

			try:
				os.rename('images/' + row[0], target_folder + row[0])
			except:
				pass

			if index % 100 == 0: dot()
		print
	os.rmdir('images/')

def labels(csvfilepath='actions.csv'):
	labels = []
	with open(csvfilepath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='\'')
		for index, row in enumerate(reader):
			if index == 0: continue # skip header
			if row[1]:
				label = row[1].replace(' ', '_')
				if not label in labels:
					labels.append(label)
	labels.sort()
	with open('labels.txt', 'w') as f:
		for index, label in enumerate(labels):
			f.write("{0} {1}\n".format(index, label))

	train_labels = []
	test_labels = []
	with open(csvfilepath, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='\'')
		for index, row in enumerate(reader):
			if index == 0: continue # skip header
			if row[1]:
				index = labels.index(row[1].replace(' ', '_'))
				if os.path.isfile('train/{0}'.format(row[0])):
					train_labels.append((row[0], index))
				elif os.path.isfile('test/{0}'.format(row[0])):
					test_labels.append((row[0], index))
	
	with open('train_labels.txt', 'w') as f:
		for fname, index in train_labels:
			f.write("{0} {1}\n".format(fname, index))
	with open('test_labels.txt', 'w') as f:
		for fname, index in test_labels:
			f.write("{0} {1}\n".format(fname, index))
	

def main():
	# split()
	labels()

if __name__ == '__main__':
	main()