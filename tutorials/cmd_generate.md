# Generating new folders with specific authors using the command line
In this tutorial we illustrate how to use the command line to generate a folder with the texts of a specific author using generate.py from CLEAR/tools/scripts.py.

If you have already cloned CLEAR to your local computer, skip steps 1 to 3.

Step 1: Open the command line window and start by making a new local directory.

```bash
mona@wintermute:~$ mkdir mycorpus
```

Step 2: Change the directory to this new directory.

```
mona@wintermute:~$ cd mycorpus
```

Step 3: Now clone CLEAR.

```
mona@wintermute:~/mycorpus$ git clone https://github.com/digitaltxtlab/CLEAR.git
# or
mona@wintermute:~/mycorpus$ git clone https://github.com/digitaltxtlab/CLEAR.git mycorpus
```

Step 4: Change the directory to CLEAR/tools/scripts.py

```
mona@wintermute:~/mycorpus$ cd CLEAR/tools/scripts_py
```

Step 5: Write "python generate.py AUTHOR'S LAST NAME" to make a folder containing the text of that author. Here is an example of how to generate a folder with Grundtvig's texts.

```
mona@wintermute:~/mycorpus/CLEAR/scripts_py$ python generate.py Grundtvig  
```

And here is an example of how to generate a folder with Nansen's texts.

```
mona@wintermute:~/mycorpus/CLEAR/scripts_py$ python generate.py Nansen
```

And likewise an example of how to generate a folder with Blicher's texts.

```
mona@wintermute:~/mycorpus/CLEAR/scripts_py$ python generate.py Blicher
```

The new folders can now be found in the main directory of CLEAR.


