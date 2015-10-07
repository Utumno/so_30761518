# from package import sub
import package.sub

print(__file__ + u' imported!')

print '__name__', '->', __name__
print '__package__', '->', __package__
try:
    print '__path__', '->', __path__
except NameError:
    print '__path__', '->', 'UNSET'

# _ = raw_input()
