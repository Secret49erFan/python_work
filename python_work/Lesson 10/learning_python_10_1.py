# practice 2/28/25
# chapter 10
# learning python

from pathlib import Path as p # import lib

path = p('learning_python.txt') # label the path to the file
contents = path.read_text() # reading whole file
print(contents)