# torrent2magnet
种子文件批量转换成磁力链

注册表可以直接关联 Torrent 文件
-----------------------------------

Windows Registry Editor Version 5.00


[HKEY_CLASSES_ROOT\.torrent]
@="Torrent.Document"


[HKEY_CLASSES_ROOT\Torrent.Document\shell\open\command]
@="\"C:\\Windows\\py.exe\" \"C:\\Users\\KING\\Desktop\\torrent2mag.py\" \"%1\""

---------------------------------------
