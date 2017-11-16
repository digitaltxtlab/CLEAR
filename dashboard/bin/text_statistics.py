import glob, re, sys, math
from collections import Counter

metadata_filename = sys.argv[1]

punctuation_pattern = re.compile(r"([,\.\-\?\!;\"\'])")
file_count = 0

# Function to compute the word-level Shannon entropy of a list of tokens
def docEntropy(docArray):
  tokenFreqs = {}

  totalTokens = len(docArray)

  for token in docArray:
    if (token in tokenFreqs):
      tokenFreqs[token] += 1
    else:
      tokenFreqs[token] = 1

  entropy = 0

  for token in tokenFreqs:
    p_x = float(tokenFreqs[token])/totalTokens
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)

  return entropy

with open(metadata_filename, "r", encoding="UTF-8") as metadata_reader:
    header = metadata_reader.readline().rstrip()
    field_names = header.split("\t")

    print("{}\ttypes\ttokens\tratio\tentropy".format(header))

    for line in metadata_reader:
        line = line.rstrip()

        fields = line.split("\t")

        filename = "plain/{}.txt".format(fields[0])

        with open(filename, "r", encoding="UTF-8") as reader:

            counts = Counter()
            docTokens = []

            for text_line in reader:
                text_line = text_line.rstrip().lower()
                text_line = punctuation_pattern.sub(r" \1 ", text_line)
                lineTokens = text_line.split()

                docTokens = docTokens + lineTokens

                counts.update(lineTokens)

            entropy = docEntropy(docTokens)

            tokens = sum(counts.values())
            types = len(counts.keys())

            if tokens > 0:
                print("{}\t{}\t{}\t{:.5f}\t{:.5f}".format(line, types, tokens, float(types) / tokens, float(entropy)))
            else:
                print("{}\t{}\t{}\t{:.5f}\t{:.5f}".format(line, types, tokens, 0, 0))
        file_count += 1
        #if file_count > 100:
        #    break
