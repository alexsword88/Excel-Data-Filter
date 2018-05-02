# -*- mode: python -*-
import os
import jsonrpcserver

block_cipher = None
#C:\\Users\\Alexsword\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\jsonrpcserver\\request-schema.json','jsonrpcserver')

def get_json_data():
	import jsonrpcserver
	return jsonrpcserver.__path__[0]+os.sep+"request-schema.json"

a = Analysis(['pyfunc\\api.py'],
             pathex=['./'],
             binaries=[],
             datas=[(get_json_data(),'jsonrpcserver')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
			 


	
def get_pandas_path():
    import pandas
    pandas_path = pandas.__path__[0]
    return pandas_path
dict_tree = Tree(get_pandas_path(), prefix='pandas', excludes=["*.pyc"])
print(dict_tree)
a.datas += dict_tree
a.binaries = filter(lambda x: 'pandas' not in x[0], a.binaries)	 
			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='api',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='api')
