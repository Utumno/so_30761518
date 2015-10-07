print(__file__ + u' imported!')

init_sub = 33

from package import sub as _sub

print _sub

print '__name__', '->', __name__
print '__package__', '->', __package__
try:
    print '__path__', '->', __path__
except NameError:
    print '__path__', '->', 'UNSET'
