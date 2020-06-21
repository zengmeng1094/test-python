import os

print('k.py', os.getcwd())

# import j
# from test_python_import_issue.pacx import j
from . import j

# from test_python_import_issue.dirx import a

print('hello')


if __name__ == '__main__':
    j.add()