# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['final_sort.py'],
             pathex=['E:\\Projects\\Programming\\Python Scripts\\Echo_sort'],
             binaries=[],
             datas=[],
             hiddenimports=['pydicom.encoders.gdcm', 'pydicom.encoders.pylibjpeg'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='final_sort',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
