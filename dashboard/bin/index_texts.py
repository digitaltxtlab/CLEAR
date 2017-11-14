import glob, re
from collections import Counter

punctuation_pattern = re.compile(r"([,\.\-\?\!;\"\'\:])")

file_count = 0

word_counter = {}

file_output = open("workids.txt", "w", encoding="UTF-8")

for filename in glob.glob("plain/*"):
    
    counter = Counter()
    work_id = filename.replace("plain/", "").replace(".txt", "")
    
    file_output.write("{}\n".format(work_id))
    
    with open(filename, "r", encoding="UTF-8") as reader:
        for line in reader:
            line = line.rstrip().lower().replace("aa", "å")
            line = punctuation_pattern.sub(r" \1 ", line)
            
            counter.update(line.split())
    
    for word in counter.keys():
        if not word in word_counter:
            word_counter[word] = set()
        word_counter[word].add(file_count)
    
    file_count += 1
    #if file_count > 100:
    #    break

file_output.close()

for word in word_counter.keys():
    files = word_counter[word]
    if len(files) >= 5 and len(files) < file_count * 0.25:
        print("{}\t{}".format(word, "\t".join([str(x) for x in files])))