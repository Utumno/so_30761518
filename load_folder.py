import sys
import os.path
import imp
import glob

def _load_package(path, base):
    pkgDir = os.path.abspath(os.path.join(path, base))
    init = os.path.join(pkgDir, "__init__.py")
    if not os.path.exists(init):
        return None, None
    #
    # mod = sys.modules[base] = imp.new_module(base)
    # mod.__file__ = init
    # mod.__path__ = [filename]
    # #init file
    # initfile = os.path.join(filename,initfile+ext)
    # if os.path.exists(initfile):
    #     with open(initfile,'U') as fp:
    #         code = fp.read()
    #     exec compile(code, initfile, 'exec') in mod.__dict__
    file, pathname, description = imp.find_module(base, [path])
    print file, pathname, description
    pack = sys.modules.get(base, None)
    if pack is None:
        sys.modules[base] = pack = imp.load_module(base, file, pathname, description)
        # pack.__path__ = [pkgDir]
        print pack.sub
    return base, pack

def _load_module(path):
    code_file = os.path.basename(path)
    base = code_file.replace(".py", "")
    with open(path, 'rb') as fin:
        return base, imp.load_source(base, path, fin)

def load_folder(dir):
    sys.path.append(dir)
    mods = {}
    for p in glob.glob(dir + "/*/"):
        base = p.replace("\\", "").replace("/", "")
        base = base.replace(dir.replace("\\", "").replace("/", ""), "")
        hash, pack = _load_package(dir, base)
        if hash: mods[hash] = pack
    for m in glob.glob(dir + "/*.py"): ##: /*/*.py
        hash, mod = _load_module(m)
        mods[hash] = mod
    return mods

## My added code
print('Python %s on %s' % (sys.version, sys.platform))

root_ = r'C:\Dropbox\eclipse_workspaces\python\sandbox\root'

def depyc(root, _indent=''): # deletes .pyc which will end up being imported
    if not _indent: print '\nListing', root
    for p in os.listdir(root):
        name = _indent + p
        abspath = os.path.join(root, p)
        if os.path.isdir(abspath):
            print name + ':'
            depyc(abspath, _indent=_indent + '  ')
        else:
            name_ = name[-4:]
            if name_ == '.pyc':
                os.remove(abspath)
                continue
            print name
    if not _indent: print

depyc(root_)
load_folder(root_)
