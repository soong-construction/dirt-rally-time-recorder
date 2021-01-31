# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import sys

# Get name parameter from arguments
index = sys.argv.index('--name')
namearg = str(sys.argv[index + 1])

# Avoid Tk/Tcl dependency: https://github.com/pyinstaller/pyinstaller/wiki/Recipe-remove-tkinter-tcl
# sys.modules['FixTk'] = None
tkExcludes = []# ['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter']

stdlibExcludes = []# ['_bz2', '_ctypes', '_hashlib', '_lzma', '_ssl', 'pyexpat', 'lib2to3', 'asyncio']

a = Analysis(['timerecorder/timerecord.py'],
             pathex=['.'],
             binaries=[
                ('bin/*', '.')
             ],
             datas=[
             	('dirtrally-lb.db', '.'),
             	('LICENSE', '.'),
             	('THIRD_PARTY_LICENSES.txt', '.'),
             	('VERSION', '.'),
             	('resources/list-*', '.'),
             	('resources/export-*', '.'),
             	('README.md', '.'),
             	('docs/*', 'docs')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=stdlibExcludes+tkExcludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='timerecord',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

# Exclude Universal CRT to spare licensing issues
# a.binaries = [x for x in a.binaries if not x[0] == 'VCRUNTIME140.dll']
# a.binaries = [x for x in a.binaries if not x[0] == 'ucrtbase.dll']
# a.binaries = [x for x in a.binaries if not x[0].startswith('api-ms-win-core-')]
# a.binaries = [x for x in a.binaries if not x[0].startswith('api-ms-win-crt-')]

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=namearg)
