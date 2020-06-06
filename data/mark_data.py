import re
import json

def load_document(filename):
	file = open(filename, mode="rt", encoding="utf-8")
	text = file.read()
	file.close()
	return text;

def clean_data(text):
	spaces_dash = re.compile("([\s+-])")
	only_chars = re.compile("([^а-я^А-Я ])")
	whitespaces = re.compile("\s+")

	sub = spaces_dash.sub(" ", text)
	sub = only_chars.sub("", sub)
	sub = whitespaces.sub(" ", sub)

	words = sub.split(" ")

	for i in range(len(words)):
		words[i] = words[i].lower()

	# words.insert(0, "<start>")
	# words.append("<end>")

	return words

def vectorText(textArray):
	counter = 0
	keys = []
	out = []

	for word in textArray:
		if word not in keys:
			out.append([word, counter])
			keys.append(word)
			counter += 1

	return out

def codeText(textArray, vector):
	def findCode(w):
		for arr in vector:
			if arr[0] == w:
				return arr[1]

	out = []
	for word in textArray:
		code = findCode(word)
		# if code is None:
		# 	print(word);
		out.append(code)

	return out

def markData(full, slim, out_file=None):	
	f = load_document(full)
	c = clean_data(f)
	v = vectorText(c)

	s  = load_document(slim)
	cs = clean_data(s)

	full_code = codeText(c, v)
	slim_code = codeText(cs, v)
	
	out = {
		"full": full_code,
		"slim": slim_code,
		"vector": v
	}

	if out_file is not None:
		F = open(out_file, "w")
		F.write(json.dumps(out, indent=4))
		F.close

	return out
# markData("source/1/full.txt", "source/1/slim.txt")
# print(markData("source/2/full.txt", "source/2/slim.txt", "marked/2.txt"))
# print(markData("source/1/full.txt", "source/1/slim.txt", "marked/1.txt"))