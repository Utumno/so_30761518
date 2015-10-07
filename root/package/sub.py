print(__file__ + u' imported!')

print '__name__', '->', __name__
print '__package__', '->', __package__
# print '__path__', '->', __path__

# print 'let.s import mod'
# from .. import mod
# r"""
# Traceback (most recent call last):
#   File "C:/Users/MrD/.PyCharm40/config/scratches/load_folder.py", line 62, in <module>
#     load_folder(root_)
#   File "C:/Users/MrD/.PyCharm40/config/scratches/load_folder.py", line 39, in load_folder
#     hash, mod = _load_module(_abspath) # will use pyc if available!
#   File "C:/Users/MrD/.PyCharm40/config/scratches/load_folder.py", line 22, in _load_module
#     return base, imp.load_source(base, path, fin)
#   File "C:\Users\MrD\.PyCharm40\config\scratches\root\mod.py", line 2, in <module>
#     import package.sub
#   File "C:\Users\MrD\.PyCharm40\config\scratches\root\package\sub.py", line 8, in <module>
#     from .. import mod
# ValueError: Attempted relative import beyond toplevel package
# """
#
