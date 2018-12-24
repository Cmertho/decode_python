import string
import secrets

russian_big = "".join(map(chr, range(1040, 1072)))
russian_small = "".join(map(chr, range(1072, 1104)))
ALL_NAME = russian_small + russian_big + string.printable
key = list(map(ord, secrets.SystemRandom().sample(ALL_NAME, 5)))
text_code = ""
with open("generate.key", "w", encoding="utf-8") as key_file:
	key_file.write(str(key)[1:-1])

with open("text.txt", encoding="utf-8") as file:
	text = file.read()
	for i in text:
		text_code += chr(ord(i) + secrets.SystemRandom().choice(key))
