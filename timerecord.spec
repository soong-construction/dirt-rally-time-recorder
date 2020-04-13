# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['timerecorder/timerecord.py'],
             pathex=['.'],
             binaries=[],
             datas=[
             	('config.yml', '.'),
             	('dirtrally-lb.db', '.'),
             	('bin/sqlite3.exe', '.'),
             	('LICENSE', '.'),
             	('VERSION', '.'),
             	('list-*', '.'),
             	('resources/list-*', '.'),
             	('export-*', '.'),
             	('resources/export-*', '.'),
             	('README.md', '.')
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
               name='timerecorder')
