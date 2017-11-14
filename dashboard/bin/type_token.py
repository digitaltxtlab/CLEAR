import glob, re, sys
from collections import Counter

metadata_filename = sys.argv[1]

punctuation_pattern = re.compile(r"([,\.\-\?\!;\"\'])")
file_count = 0

with open(metadata_filename, "r", encoding="UTF-8") as metadata_reader:
    header = metadata_reader.readline().rstrip()
    field_names = header.split("\t")
    
    print("{}\ttypes\ttokens\tratio".format(header))
    
    for line in metadata_reader:
        line = line.rstrip()
        
        fields = line.split("\t")
        
        filename = "plain/{}.txt".format(fields[0])
        
        with open(filename, "r", encoding="UTF-8") as reader:
            
            counts = Counter()
            
            for text_line in reader:
                text_line = text_line.rstrip().lower()
                text_line = punctuation_pattern.sub(r" \1 ", text_line)
                
                counts.update(text_line.split())
            
            tokens = sum(counts.values())
            types = len(counts.keys())
            
            if tokens > 0:
                print("{}\t{}\t{}\t{:.5f}".format(line, types, tokens, float(types) / tokens))
            else:
                print("{}\t{}\t{}\t{:.5f}".format(line, types, tokens, 0))
        file_count += 1
        #if file_count > 100:
        #    break
