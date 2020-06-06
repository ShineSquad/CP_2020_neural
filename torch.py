import numpy
import string
import json

def word_to_tensor(word, words):
	count = len(words)
	tensor = numpy.zeros((1, count))
	word_index = words.index(word)
	tensor[0][word_index] = 1

	return tensor

def conver_to_tensors(file, out_file=None):
	mark = open(file, "r")
	data = json.loads(mark.read())
	mark.close()

	codes = []
	for c in data["vector"]:
		codes.append(c[1])

	full_tensors = []
	for code in data["full"]:
		if code is None:
			continue

		t = word_to_tensor(code, codes)
		full_tensors.append(t)

	slim_tensors = []
	for code in data["slim"]:
		if code is None:
			continue

		t = word_to_tensor(code, codes)
		slim_tensors.append(t)

	out = {
		"full": numpy.array(full_tensors).tolist(),
		"slim": numpy.array(slim_tensors).tolist()
	}

	print()

	if out_file is not None:
		F = open(out_file, "w")
		F.write(json.dumps(out, indent=4))
		F.close
	return out

conver_to_tensors("data/marked/1.txt", "data/tensors/1.txt")
conver_to_tensors("data/marked/2.txt", "data/tensors/2.txt")