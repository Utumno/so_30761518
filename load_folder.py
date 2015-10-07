import sys
import os.path
import imp

def _load_package(root, name):
    file, pathname, description = imp.find_module(name, [root])
    print file, pathname, description
    pack = sys.modules.get(name, None)
    if pack is None:
        pack = imp.load_module(name, file, '', description)
        pack.__path__ = [pathname]
    else:
        print 'In cache', pack
    return name, pack

def _load_module(path):
    code_file = os.path.basename(path)
    base = code_file.replace(".py", "")
    pack = sys.modules.get(base, None)
    if pack is None:
        with open(path, 'rb') as fin:
            return base, imp.load_source(base, path, fin)
    return base, pack

def load_folder(root):
    # sys.path.append(root)
    mods = {}
    paths = [(_, os.path.join(root, _)) for _ in os.listdir(root)]
    packs = filter(
        lambda _: os.path.exists(os.path.join((_[1]), "__init__.py")), paths)
    pys = filter(lambda _: _[0][-3:] == '.py', paths)
    del paths
    for path, _abspath in packs: # ['mod.py', 'mod.pyc', 'package', 'package2']
        print 'Importing', _abspath
        hash, mod = _load_package(root, name=path)
        mods[hash] = mod
    for path, _abspath in pys: # ['mod.py', 'mod.pyc', 'package', 'package2']
        print 'Importing', _abspath
        hash, mod = _load_module(_abspath) # will use pyc if available!
        mods[hash] = mod
    return mods

def depyc(root, rmpyc, _indent=''): # deletes .pyc which will end up being imported
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
depyc(root_, True) # False will end up importing the pyc files !
load_folder(root_)
# load_folder(root_)

# _= raw_input()
