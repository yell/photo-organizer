import os
import sys
import csv
from random import seed, shuffle
seed(1337)


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

def new_classes_map():
	mp = {}
	for k in [12, 17]:
		mp[k] = 0
	for k in [6, 8, 11, 13, 15, 16]:
		mp[k] = 1
	v = 2
	for k in xrange(20):
		if not k in mp:
			mp[k] = v
			v += 1
	return mp
	
def new_labels():
	return [
		"running/walking",
		"other",
		"bicycling",
		"conditioning_exercise",
		"dancing",
		"fishing_and_hunting",
		"home_activities",
		"home_repair",
		"lawn_and_garden",
		"music_playing",
		"occupation",
		"sports",
		"water_activities",
		"winter_activities",
	]

def resplit(csvfilepath='actions.csv', train_ratio=0.9):
	os.rename('train/', 'traintest/')
	for (dirpath, dirnames, filenames) in os.walk('test/'):
		for fname in filenames:
			os.rename('test/' + fname, 'traintest/' + fname)
	os.rmdir('test/')

	with open('labels.txt', 'w') as f:
		for index, label in enumerate(new_labels()):
			f.write("{0} {1}\n".format(index, label))

	fname_map = {}
	new_map = new_classes_map()
	with open('train_labels.txt') as f:
		for line in f:
			fname, index = line.strip().split(' ')
			fname_map[fname] = new_map[int(index)]
	with open('test_labels.txt') as f:
		for line in f:
			fname, index = line.strip().split(' ')
			fname_map[fname] = new_map[int(index)]

	index_map = dict([ (k, []) for k in xrange(14) ])
	for fname, index in fname_map.items():
		index_map[index].append(fname)
	
	train_labels = []
	test_labels = []
	for index in index_map:
		m_index = len(index_map[index])
		for fname_index, fname in enumerate(index_map[index]):
			if fname_index < train_ratio * m_index:
				train_labels.append((fname, index))
			else:
				test_labels.append((fname, index))

	shuffle(train_labels)
	shuffle(test_labels)

	with open('train_labels.txt', 'w') as f:
		for fname, index in train_labels:
			f.write("{0} {1}\n".format(fname, index))
	with open('test_labels.txt', 'w') as f:
		for fname, index in test_labels:
			f.write("{0} {1}\n".format(fname, index))

	safe_mkdir('train/')
	safe_mkdir('test/')

	for fname, _ in train_labels:
		os.rename('traintest/' + fname, 'train/' + fname)
	for fname, _ in test_labels:
		os.rename('traintest/' + fname, 'test/' + fname)

	os.rmdir('traintest/')


def resplit_using_labels():
	train_labels = []
	test_labels = []
	with open('train_labels.txt') as f:
		for line in f:
			fname, index = line.strip().split(' ')
			train_labels.append((fname, index))
	with open('test_labels.txt') as f:
		for line in f:
			fname, index = line.strip().split(' ')
			test_labels.append((fname, index))

	os.rename('train/', 'traintest/')
	for (dirpath, dirnames, filenames) in os.walk('test/'):
		for fname in filenames:
			os.rename('test/' + fname, 'traintest/' + fname)
	os.rmdir('test/')

	safe_mkdir('train/')
	safe_mkdir('test/')

	for fname, _ in train_labels:
		os.rename('traintest/' + fname, 'train/' + fname)
	for fname, _ in test_labels:
		os.rename('traintest/' + fname, 'test/' + fname)

	os.rmdir('traintest/')


def main():
	# split()
	# labels()
	# resplit()
	resplit_using_labels()

if __name__ == '__main__':
	main()