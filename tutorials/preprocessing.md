
# Preprocessing with python #
In this tutorial we illustrate how to use the preprocessing module from tools/scripts_py

```python
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
```

Let us start by importing a plain text document (unicode) from the ADL collection ADL/plain.

```python
import io, os
os.chdir(os.path.expanduser('~/Documents/proj/clear_local/CLEAR'))# change this to your filepath to CLEAR
file = os.path.join('ADL','plain','22_2237.txt')# import 'Fyrtårnet' af H.C. Andersen
f = io.open(file,'r',encoding = 'utf8')
text = f.read()
```
Then we import the functions from the preprocessing module under the alias *pp*.
```python
os.chdir(os.path.expanduser('~/Documents/proj/clear_local/CLEAR/tools/scripts_py'))# go to scripts
import preprocessing as pp
```
And finally we can remove punctuation and other non-alphanumeric characters
```python
text_filter = pp.re_nalpha(text)
```
Before we tokenize at the word level
```python
text_token = pp.tokenizer(text_filter)
```
Remember that you can always use the *print* function to check your variable
```python
print text
print text_token[100]
```
Notice that the tokenizer allows for any n-gram size through the second parameter

```python
trigram = pp.tokenizer(text_filter,3)
print trigram[0]
```
