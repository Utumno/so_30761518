import sys
import os.path
import imp

def _load_(root, name):
    file, pathname, description = imp.find_module(name, [root])
    pack = sys.modules.get(name, None)
    try:
        if pack is None:
            pack = imp.load_module(name, file, pathname, description)
        else:
            print 'In cache', pack
    finally:
        if file is not None: file.close()
    return name, pack

def load_folder(root):
    # sys.path.append(root)
    mods = {}
    paths = [(_, os.path.join(root, _)) for _ in os.listdir(root)]
    packs = filter(
        lambda _: os.path.exists(os.path.join((_[1]), "__init__.py")), paths)
    pys = filter(lambda _: _[0][-3:] == '.py', paths)
    del paths
    # first import packages as in original - modules may import from them
    for path, _abspath in packs:
        print 'Importing', _abspath
        hash, mod = _load_(root, name=path) # will use pyc if available!
        mods[hash] = mod
    # then modules
    for path, _abspath in pys:
        print 'Importing', _abspath
        hash, mod = _load_(root, name=path[:-3])
        mods[hash] = mod
    return mods

def depyc(root, rmpyc, _indent=''):
    if not _indent: print '\nListing', root
    for p in os.listdir(root):
        name = _indent + p
        abspath = os.path.join(root, p)
        if os.path.isdir(abspath):
            print name + ':'
            depyc(abspath, rmpyc, _indent=_indent + '  ')
        else:
            if rmpyc and name[-4:] == '.pyc':
                os.remove(abspath)
                continue
            print name
    if not _indent: print

## Run ##
print('Python %s on %s' % (sys.version, sys.platform))
root_ = os.path.join(os.getcwdu(), u'root')
depyc(root_, False) # False will end up importing the pyc files !
load_folder(root_)
