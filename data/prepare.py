import os
import sys
import csv


def dot():
	sys.stdout.write('.'); sys.stdout.flush()

def safe_mkdir(dirpath):
	try:
	    os.stat(dirpath)
	except:
	    os.mkdir(dirpath)

def main(filepath='actions.csv', train_ratio=0.9):
	safe_mkdir('index/')
	safe_mkdir('train/')
	safe_mkdir('test/')

	with open(filepath, 'rb') as csvfile:
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


if __name__ == '__main__':
	main()