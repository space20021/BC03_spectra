# -*- mode: python -*-
a = Analysis(['plot_spectra.py'],
             pathex=['/Users/judi/Desktop/BC03_spectra'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='plot_spectra',
          debug=False,
          strip=None,
          upx=True,
          console=True )
