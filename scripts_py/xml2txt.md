```python

from xml.sax.handler import ContentHandler
import xml.sax
import sys

class textHandler(ContentHandler):
    def characters(self, ch):
        sys.stdout.write(ch.encode("UTF-8"))

parser = xml.sax.make_parser()
handler = textHandler()
parser.setContentHandler(handler)

filepath = "/home/kln/projects/CLEAR/data_lb/lb1202930.xml"
parser.parse(filepath)

orig_stdout = sys.stdout
f = file('lb1202930.txt', 'w')
sys.stdout = f

parser.parse(filepath)

sys.stdout = orig_stdout
f.close()​

```
