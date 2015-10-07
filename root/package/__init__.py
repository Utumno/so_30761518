print(__file__ + u' imported!')

sub = 33

print '__name__', '->', __name__
print '__package__', '->', __package__
try:
    print '__path__', '->', __path__
except NameError:
    print '__path__', '->', 'UNSET'
