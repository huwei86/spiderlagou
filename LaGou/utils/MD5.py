#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/6/9 15:57'
import hashlib

def get_md5(url):
    if isinstance(url,str):
        url=url.encode("utf-8")
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()