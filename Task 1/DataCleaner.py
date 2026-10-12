import re

input_file = "raw_corpus.txt"
output_file = "clean_corpus.txt"

with open(input_file, "r", encoding="utf-8") as f:
  raw_text = f.read()

french_pattern = r"[a-zA-ZàâäéèêëîïôöùûüçœæÀÂÄÉÈÊËÎÏÔÖÙÛÜÇŒÆ]+"

words = re.findall(french_pattern, raw_text)

words_lcs = [word.lower() for word in words]
corpus_100k = words_lcs[:100000]

with open(output_file, "w", encoding="utf-8") as f:
  f.write(" ".join(corpus_100k))

print(f"Ilosc slow {len(corpus_100k)}")