# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Get name parameter from arguments
import sys
index = sys.argv.index('--name')
namearg = str(sys.argv[index + 1])

a = Analysis(['timerecorder/timerecord.py'],
             pathex=['.'],
             binaries=[
                ('bin/*', '.')
             ],
             datas=[
             	('dirtrally-lb.db', '.'),
             	('LICENSE', '.'),
             	('VERSION', '.'),
             	('resources/list-*', '.'),
             	('resources/export-*', '.'),
             	('README.md', '.'),
             	('docs/*', 'docs')
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=namearg)
