# practice 2/28/25
# chapter 10
# learning python
import os
from pathlib import Path as p # import lib
print(os.getcwd())
path = p('python_work/Lesson 10/learning_python.txt') # Specify the relative path
contents = path.read_text() # reading whole file
print(contents)