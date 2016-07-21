import os
import csv

class Repository(object):

	def __init__(self, filename='repo.csv', num_classes=14, num_feats=5):
		self._filename = filename
		self.num_classes = num_classes
		self.num_feats = num_feats
		self.csvparams = dict(
			delimiter=',', 
			quotechar='\'',
			quoting=csv.QUOTE_MINIMAL
		)
		if os.path.isfile(self.filename):
			return

	def __getitem__(self, img_path):
		with open(self.filename, 'rb') as csvfile:
			reader = csv.reader(csvfile, **self.csvparams)
			for row in reader:
				if img_path == row[0]:
					data = map(float, row[1:])
					return data[:self.num_classes], data[self.num_classes:]

	def __iter__(self):
		with open(self.filename, 'rb') as csvfile:
			reader = csv.reader(csvfile, **self.csvparams)
			for row in reader:
				yield row[0]


	def is_stored(self, img_path):
		''' check if specific image is stored '''
		return self.__getitem__(img_path)

	def store_entry(self, img_path, probs, feats):
		''' add new entry if not present '''
		if self.is_stored(img_path):
			return
		if len(probs) != self.num_classes:
			raise ValueError("store_entry: `probs` has invalid size {0} != {1}".format(len(probs), self.num_classes))
		if len(feats) != self.num_feats:
			raise ValueError("store_entry: `feats` has invalid size {0} != {1}".format(len(feats), self.num_feats))
		with open(self.filename, 'ab') as csvfile:
			writer = csv.writer(csvfile, **self.csvparams)
			writer.writerow([img_path] + probs + feats)

	def delete_entry(self, img_path):
		''' remove image if present '''
		if not self.is_stored(img_path):
			return
		rows = []
		with open(self.filename, 'rb') as csvfile:
			for row in csv.reader(csvfile):
				if row[0] != img_path:
					rows.append(row)
		with open(self.filename, 'wb') as csvfile:
			writer = csv.writer(csvfile, **self.csvparams)
			for row in rows:
				writer.writerow(row)


	@property
	def filename(self):
		return self._filename