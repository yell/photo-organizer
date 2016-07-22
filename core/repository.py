import os
import csv


class Repository(object):

	def __init__(self, filename='data.csv', num_classes=14):
		self._filename = filename
		self.num_classes = num_classes
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
				fname, data = row[0], row[1:]
				data = map(float, data)
				yield fname, data[:self.num_classes], data[self.num_classes:]


	def is_stored(self, img_path):
		''' check if specific image is stored '''
		if not os.path.isfile(self.filename):
			return False
		return bool(self.__getitem__(img_path))

	def store(self, img_path, probs, feats):
		''' add new entry if not present '''
		if self.is_stored(img_path):
			return
		if len(probs) != self.num_classes:
			raise ValueError("store_entry: `probs` has invalid size {0} != {1}".format(len(probs), self.num_classes))
		with open(self.filename, 'ab') as csvfile:
			writer = csv.writer(csvfile, **self.csvparams)
			writer.writerow([img_path] + probs + feats)

	def delete(self, img_path):
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

	def count(self):
		if not os.path.isfile(self.filename):
			return 0
		with open(self.filename, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			return len(list(reader))


	@property
	def filename(self):
		return self._filename