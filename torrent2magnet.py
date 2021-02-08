import bencode
import hashlib
import os
import pyperclip
from urllib.parse import quote

data_dir = r"C:\Users\KING\Downloads"


torrent=[]
magnet=[]
 
def torrent_file_to_magnet(torrent_file):
    data =  open(torrent_file, 'rb').read()
    metadata = bencode.bdecode(data)
    name = metadata['info']['name']
    dn = quote(name)
    info_bts = bencode.bencode(metadata['info'])
    info_hash = hashlib.sha1(info_bts).hexdigest()
    return f'magnet:?xt=urn:btih:{info_hash}&dn={dn}'
 
'''
if __name__ == '__main__':
    print(torrent_file_to_magnet('[ThZu.Cc][ThZu.Cc]020421-001-carib-1080p.torrent'))
'''


"""--------------------------------------------------------
<<获取文件列表>>
(1) os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。只支持在
Unix, Windows 下使用。
(2) os.path.join(path1[, path2[, ...]])    把目录和文件名合成一个路径
---------------------------------------------------------"""



"""获取文件列表"""
def getRawFileList(path):
    """-------------------------
    files,names=getRawFileList(raw_data_dir)
    files: ['datacn/dialog/one.txt', 'datacn/dialog/two.txt']
    names: ['one.txt', 'two.txt']
    ----------------------------"""
    files = []
    names = []
    for f in os.listdir(path):
        if  not f.endswith("~") or not f == "" :      # 返回指定的文件夹包含的文件或文件夹的名字的列表
            files.append(os.path.join(path, f))     # 把目录和文件名合成一个路径
            names.append(f)
    return files, names

files,names = getRawFileList(data_dir)
'''print("files:", files)
print("names:", names)'''


for tf in files:
    if tf.endswith(".torrent"):
        torrent.append(tf)
'''print(torrent)'''

for to in torrent:
    magnet.append(torrent_file_to_magnet(to))
txt=""
for l in magnet:
    print(l)
    txt=l+'\n'+txt
print("共转换了",len(magnet),"个链接")
pyperclip.copy(txt)
os.system("pause")
for i in torrent:
    os.remove(i)
